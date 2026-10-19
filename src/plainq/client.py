"""Small sync and asyncio clients preserving native gRPC errors and options."""
from __future__ import annotations

from collections.abc import Sequence
from typing import Any
import grpc
from .v1 import schema_pb2 as v1
from .v1.schema_pb2_grpc import PlainQServiceStub

Metadata = Sequence[tuple[str, str | bytes]]
ChannelOptions = Sequence[tuple[str, Any]]

class Client:
    """Native gRPC client. Plaintext by default; supply credentials for TLS.

    RPC timeouts are in seconds and default to 30. Pass None for no deadline.
    Calls preserve grpc.RpcError (or grpc.aio.AioRpcError) status and metadata.
    """

    def __init__(
        self, address: str, *, credentials: grpc.ChannelCredentials | None = None,
        options: ChannelOptions = (), user_agent: str | None = None,
    ) -> None:
        if not address.strip():
            raise ValueError("plainq: address is required")
        channel_options = list(options)
        if user_agent:
            channel_options.append(("grpc.primary_user_agent", user_agent))
        self.channel = (
            grpc.secure_channel(address, credentials, options=channel_options)
            if credentials is not None else
            grpc.insecure_channel(address, options=channel_options)
        )
        self.service_client = PlainQServiceStub(self.channel)

    def close(self) -> None:
        self.channel.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def list_queues(
        self, request: v1.ListQueuesRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.ListQueuesResponse:
        return self.service_client.ListQueues(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def describe_queue(
        self, request: v1.DescribeQueueRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.DescribeQueueResponse:
        return self.service_client.DescribeQueue(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def create_queue(
        self, request: v1.CreateQueueRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.CreateQueueResponse:
        return self.service_client.CreateQueue(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def purge_queue(
        self, request: v1.PurgeQueueRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.PurgeQueueResponse:
        return self.service_client.PurgeQueue(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def delete_queue(
        self, request: v1.DeleteQueueRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.DeleteQueueResponse:
        return self.service_client.DeleteQueue(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def send(
        self, request: v1.SendRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.SendResponse:
        return self.service_client.Send(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def receive(
        self, request: v1.ReceiveRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.ReceiveResponse:
        return self.service_client.Receive(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def delete(
        self, request: v1.DeleteRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.DeleteResponse:
        return self.service_client.Delete(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def list_topics(
        self, request: v1.ListTopicsRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.ListTopicsResponse:
        return self.service_client.ListTopics(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def create_topic(
        self, request: v1.CreateTopicRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.CreateTopicResponse:
        return self.service_client.CreateTopic(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def delete_topic(
        self, request: v1.DeleteTopicRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.DeleteTopicResponse:
        return self.service_client.DeleteTopic(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def subscribe(
        self, request: v1.SubscribeRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.SubscribeResponse:
        return self.service_client.Subscribe(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def unsubscribe(
        self, request: v1.UnsubscribeRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.UnsubscribeResponse:
        return self.service_client.Unsubscribe(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    def publish(
        self, request: v1.PublishRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.PublishResponse:
        return self.service_client.Publish(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )


class AsyncClient:
    """Native gRPC client. Plaintext by default; supply credentials for TLS.

    RPC timeouts are in seconds and default to 30. Pass None for no deadline.
    Calls preserve grpc.RpcError (or grpc.aio.AioRpcError) status and metadata.
    """

    def __init__(
        self, address: str, *, credentials: grpc.ChannelCredentials | None = None,
        options: ChannelOptions = (), user_agent: str | None = None,
    ) -> None:
        if not address.strip():
            raise ValueError("plainq: address is required")
        channel_options = list(options)
        if user_agent:
            channel_options.append(("grpc.primary_user_agent", user_agent))
        self.channel = (
            grpc.aio.secure_channel(address, credentials, options=channel_options)
            if credentials is not None else
            grpc.aio.insecure_channel(address, options=channel_options)
        )
        self.service_client = PlainQServiceStub(self.channel)

    async def close(self) -> None:
        await self.channel.close()

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.close()

    async def list_queues(
        self, request: v1.ListQueuesRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.ListQueuesResponse:
        return await self.service_client.ListQueues(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def describe_queue(
        self, request: v1.DescribeQueueRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.DescribeQueueResponse:
        return await self.service_client.DescribeQueue(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def create_queue(
        self, request: v1.CreateQueueRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.CreateQueueResponse:
        return await self.service_client.CreateQueue(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def purge_queue(
        self, request: v1.PurgeQueueRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.PurgeQueueResponse:
        return await self.service_client.PurgeQueue(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def delete_queue(
        self, request: v1.DeleteQueueRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.DeleteQueueResponse:
        return await self.service_client.DeleteQueue(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def send(
        self, request: v1.SendRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.SendResponse:
        return await self.service_client.Send(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def receive(
        self, request: v1.ReceiveRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.ReceiveResponse:
        return await self.service_client.Receive(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def delete(
        self, request: v1.DeleteRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.DeleteResponse:
        return await self.service_client.Delete(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def list_topics(
        self, request: v1.ListTopicsRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.ListTopicsResponse:
        return await self.service_client.ListTopics(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def create_topic(
        self, request: v1.CreateTopicRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.CreateTopicResponse:
        return await self.service_client.CreateTopic(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def delete_topic(
        self, request: v1.DeleteTopicRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.DeleteTopicResponse:
        return await self.service_client.DeleteTopic(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def subscribe(
        self, request: v1.SubscribeRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.SubscribeResponse:
        return await self.service_client.Subscribe(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def unsubscribe(
        self, request: v1.UnsubscribeRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.UnsubscribeResponse:
        return await self.service_client.Unsubscribe(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )

    async def publish(
        self, request: v1.PublishRequest, *, timeout: float | None = 30.0,
        metadata: Metadata | None = None, wait_for_ready: bool | None = None,
    ) -> v1.PublishResponse:
        return await self.service_client.Publish(
            request, timeout=timeout, metadata=metadata, wait_for_ready=wait_for_ready,
        )
