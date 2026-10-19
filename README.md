# PlainQ Python SDK

Synchronous and asyncio clients for [PlainQ](https://github.com/marsolab/plainq),
covering the same 14 native gRPC operations as the [Go SDK](https://github.com/marsolab/plainq-go-sdk).
Requires Python 3.10+. Uses the broker's **gRPC address**, not a PlainQ Cloud HTTP endpoint.

## Install

```sh
pip install plainq-sdk
```

Until the first PyPI publication, install the wheel from this repository's GitHub release:

```sh
pip install ./plainq_sdk-0.1.0-py3-none-any.whl
```

## Quick start

```python
from plainq import Client, v1

with Client("localhost:8080") as client:
    queue_id = client.create_queue(v1.CreateQueueRequest(queue_name="orders")).queue_id
    client.send(v1.SendRequest(queue_id=queue_id, messages=[v1.SendMessage(body=b'{"order":123}')]))
    response = client.receive(v1.ReceiveRequest(queue_id=queue_id, batch_size=10, wait_time_seconds=20))
    for message in response.messages:
        print(message.id, message.body)
        # Acknowledge only after processing succeeds.
        result = client.delete(v1.DeleteRequest(queue_id=queue_id, message_ids=[message.id]))
        if result.failed:
            raise RuntimeError(str(result.failed))
```

## Asyncio

```python
import asyncio
from plainq import AsyncClient, v1

async def main():
    async with AsyncClient("localhost:8080") as client:
        queues = await client.list_queues(v1.ListQueuesRequest(limit=20))
        print(queues)

asyncio.run(main())
```

Create and use `AsyncClient` on the same event loop. Cancelling the asyncio task
cancels its pending RPC. The sync client can be shared across threads; close either
client when finished, or use its context manager.

## API

Each method takes a generated protobuf request and returns its generated response.
All methods accept keyword options `timeout` (seconds; default 30; `None` disables),
`metadata`, and `wait_for_ready`.

| Group | Methods |
| --- | --- |
| Queues | `list_queues`, `describe_queue`, `create_queue`, `purge_queue`, `delete_queue` |
| Messages | `send`, `receive`, `delete` |
| Topics | `list_topics`, `create_topic`, `delete_topic`, `subscribe`, `unsubscribe`, `publish` |

Messages and enum constants live in `plainq.v1.schema_pb2` (also exported as `v1`).
Generated gRPC stubs live in `plainq.v1.schema_pb2_grpc`. `.pyi` files and `py.typed`
are included. `client.service_client` and `client.channel` expose the underlying API.
Bytes remain `bytes`, 64-bit values remain Python `int`, and timestamps retain
protobuf seconds and nanoseconds. Queue listing preserves `next_cursor` and `has_more`.

```python
topic_id = client.create_topic(v1.CreateTopicRequest(topic_name="events")).topic_id
client.subscribe(v1.SubscribeRequest(topic_id=topic_id, queue_id=queue_id))
result = client.publish(v1.PublishRequest(topic_id=topic_id, messages=[v1.PublishMessage(body=b"hello")]))
print(result.delivered_count)
```

## TLS, metadata, errors

Plaintext is the default, matching the Go SDK. Supply credentials for TLS.

```python
import os
import grpc
from plainq import Client, v1

with Client("broker.example:443", credentials=grpc.ssl_channel_credentials(),
            user_agent="orders-worker/1.0") as client:
    queues = client.list_queues(v1.ListQueuesRequest(), timeout=5,
        metadata=[("authorization", f"Bearer {os.environ['PLAINQ_TOKEN']}")])
```

Pass native gRPC channel settings via `options`. Errors preserve `grpc.RpcError`
(or `grpc.aio.AioRpcError`) status, details, and metadata. The SDK adds no application
retries: retrying writes after ambiguous transport failures can duplicate messages.
Use a deadline longer than the requested long poll (server maximum: 20 seconds).

## Development

```sh
uv sync --python 3.13
uv run python scripts/generate.py
uv run pytest
PLAINQ_ADDR=127.0.0.1:18080 uv run pytest -m integration
uv build
uv run twine check dist/*
```

The integration test requires a **disposable broker**, creates and removes its own
queue and topic, and fails when its address is missing. [SCHEMA.md](SCHEMA.md) records
the immutable protocol pin. [PUBLISHING.md](PUBLISHING.md) explains releases.
See [examples/worker.py](examples/worker.py) for a long-polling worker.

## License

[MIT](LICENSE).
