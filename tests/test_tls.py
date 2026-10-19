import asyncio
from concurrent.futures import ThreadPoolExecutor
import subprocess
import grpc
from plainq import Client, AsyncClient, v1
from plainq.v1.schema_pb2_grpc import PlainQServiceServicer, add_PlainQServiceServicer_to_server


def test_tls_credentials(tmp_path):
    key, cert = tmp_path / 'key.pem', tmp_path / 'cert.pem'
    subprocess.run(['openssl', 'req', '-x509', '-newkey', 'rsa:2048', '-nodes', '-days', '1',
        '-subj', '/CN=localhost', '-addext', 'subjectAltName=DNS:localhost',
        '-keyout', str(key), '-out', str(cert)], check=True, capture_output=True)
    class Service(PlainQServiceServicer):
        def ListQueues(self, request, context):
            return v1.ListQueuesResponse(total_count=42)
    server = grpc.server(ThreadPoolExecutor(max_workers=2))
    add_PlainQServiceServicer_to_server(Service(), server)
    port = server.add_secure_port('127.0.0.1:0', grpc.ssl_server_credentials(((key.read_bytes(), cert.read_bytes()),)))
    server.start()
    credentials = grpc.ssl_channel_credentials(root_certificates=cert.read_bytes())
    try:
        with Client(f'localhost:{port}', credentials=credentials) as client:
            assert client.list_queues(v1.ListQueuesRequest()).total_count == 42
        async def run():
            async with AsyncClient(f'localhost:{port}', credentials=credentials) as client:
                assert (await client.list_queues(v1.ListQueuesRequest())).total_count == 42
        asyncio.run(run())
    finally:
        server.stop(0).wait()
