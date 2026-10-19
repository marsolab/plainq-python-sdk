import asyncio
from concurrent.futures import ThreadPoolExecutor
import re
import threading
import grpc
import pytest
from plainq import Client, AsyncClient, v1

@pytest.fixture
def address():
    server = grpc.server(ThreadPoolExecutor(max_workers=4))
    handlers = {}
    def handler(method):
        def run(request, context):
            metadata = dict(context.invocation_metadata())
            if 'fail' in metadata:
                context.abort(grpc.StatusCode.PERMISSION_DENIED, 'denied')
            if 'delay' in metadata:
                stopped = threading.Event()
                context.add_callback(stopped.set)
                stopped.wait(2)
            response_type = getattr(v1, method.output_type.name)
            if method.name == 'Send':
                return response_type(message_ids=[request.messages[0].body.hex()])
            if method.name == 'ListQueues':
                return response_type(total_count=9007199254740993)
            if method.name == 'DescribeQueue':
                return response_type(queue_name=metadata.get('authorization', ''), retention_period_seconds=18446744073709551615)
            return response_type()
        return run
    for method in v1.DESCRIPTOR.services_by_name['PlainQService'].methods:
        request_type = getattr(v1, method.input_type.name)
        handlers[method.name] = grpc.unary_unary_rpc_method_handler(handler(method), request_deserializer=request_type.FromString, response_serializer=lambda msg: msg.SerializeToString())
    server.add_generic_rpc_handlers((grpc.method_handlers_generic_handler('v1.PlainQService', handlers),))
    port = server.add_insecure_port('127.0.0.1:0')
    server.start()
    yield f'127.0.0.1:{port}'
    server.stop(0).wait()

def test_all_rpcs(address):
    with Client(address) as client:
        for method in v1.DESCRIPTOR.services_by_name['PlainQService'].methods:
            request = getattr(v1, method.input_type.name)()
            if method.name == 'Send': request.messages.add(body=b'\x00\xff\x80')
            name = re.sub(r'(?<!^)(?=[A-Z])', '_', method.name).lower()
            assert getattr(client, name)(request) is not None

def test_bytes_int64_metadata_and_errors(address):
    with Client(address) as client:
        assert client.send(v1.SendRequest(messages=[v1.SendMessage(body=b'\x00\xff\x80')])).message_ids == ['00ff80']
        assert client.list_queues(v1.ListQueuesRequest()).total_count == 9007199254740993
        queue = client.describe_queue(v1.DescribeQueueRequest(), metadata=[('authorization', 'Bearer test')])
        assert queue.queue_name == 'Bearer test'
        assert queue.retention_period_seconds == 18446744073709551615
        with pytest.raises(grpc.RpcError) as err:
            client.list_queues(v1.ListQueuesRequest(), metadata=[('fail', 'yes')])
        assert err.value.code() == grpc.StatusCode.PERMISSION_DENIED
        with pytest.raises(grpc.RpcError) as err:
            client.receive(v1.ReceiveRequest(), timeout=0.05, metadata=[('delay', 'yes')])
        assert err.value.code() == grpc.StatusCode.DEADLINE_EXCEEDED

def test_async_rpcs_and_cancellation(address):
    async def run():
        async with AsyncClient(address) as client:
            for method in v1.DESCRIPTOR.services_by_name['PlainQService'].methods:
                request = getattr(v1, method.input_type.name)()
                if method.name == 'Send': request.messages.add(body=b'async')
                name = re.sub(r'(?<!^)(?=[A-Z])', '_', method.name).lower()
                assert await getattr(client, name)(request) is not None
            with pytest.raises(grpc.aio.AioRpcError) as err:
                await client.receive(v1.ReceiveRequest(), timeout=0.05, metadata=[('delay', 'yes')])
            assert err.value.code() == grpc.StatusCode.DEADLINE_EXCEEDED
            task = asyncio.create_task(client.receive(v1.ReceiveRequest(), metadata=[('delay', 'yes')]))
            await asyncio.sleep(0.02)
            task.cancel()
            with pytest.raises(asyncio.CancelledError): await task
    asyncio.run(run())

def test_validation_and_close():
    for cls in (Client, AsyncClient):
        with pytest.raises(ValueError): cls(' ')
    client = Client('127.0.0.1:1')
    client.close()
    client.close()
