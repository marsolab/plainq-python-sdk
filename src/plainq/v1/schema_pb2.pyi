import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvictionPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVICTION_POLICY_UNSPECIFIED: _ClassVar[EvictionPolicy]
    EVICTION_POLICY_DROP: _ClassVar[EvictionPolicy]
    EVICTION_POLICY_DEAD_LETTER: _ClassVar[EvictionPolicy]
    EVICTION_POLICY_REORDER: _ClassVar[EvictionPolicy]
EVICTION_POLICY_UNSPECIFIED: EvictionPolicy
EVICTION_POLICY_DROP: EvictionPolicy
EVICTION_POLICY_DEAD_LETTER: EvictionPolicy
EVICTION_POLICY_REORDER: EvictionPolicy

class SendMessage(_message.Message):
    __slots__ = ("body",)
    BODY_FIELD_NUMBER: _ClassVar[int]
    body: bytes
    def __init__(self, body: _Optional[bytes] = ...) -> None: ...

class ReceiveMessage(_message.Message):
    __slots__ = ("id", "body", "receipt_handle", "delivery_attempt", "lease_expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    LEASE_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    body: bytes
    receipt_handle: str
    delivery_attempt: int
    lease_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., body: _Optional[bytes] = ..., receipt_handle: _Optional[str] = ..., delivery_attempt: _Optional[int] = ..., lease_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListQueuesRequest(_message.Message):
    __slots__ = ("queue_prefix", "limit", "cursor", "order_by", "sort_by")
    class OrderBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORDER_BY_ID: _ClassVar[ListQueuesRequest.OrderBy]
        ORDER_BY_NAME: _ClassVar[ListQueuesRequest.OrderBy]
        ORDER_BY_CREATED_AT: _ClassVar[ListQueuesRequest.OrderBy]
    ORDER_BY_ID: ListQueuesRequest.OrderBy
    ORDER_BY_NAME: ListQueuesRequest.OrderBy
    ORDER_BY_CREATED_AT: ListQueuesRequest.OrderBy
    class SortBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SORT_BY_ASC: _ClassVar[ListQueuesRequest.SortBy]
        SORT_BY_DESC: _ClassVar[ListQueuesRequest.SortBy]
    SORT_BY_ASC: ListQueuesRequest.SortBy
    SORT_BY_DESC: ListQueuesRequest.SortBy
    QUEUE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    queue_prefix: str
    limit: int
    cursor: str
    order_by: ListQueuesRequest.OrderBy
    sort_by: ListQueuesRequest.SortBy
    def __init__(self, queue_prefix: _Optional[str] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ..., order_by: _Optional[_Union[ListQueuesRequest.OrderBy, str]] = ..., sort_by: _Optional[_Union[ListQueuesRequest.SortBy, str]] = ...) -> None: ...

class ListQueuesResponse(_message.Message):
    __slots__ = ("queues", "next_cursor", "has_more", "total_count")
    QUEUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    queues: _containers.RepeatedCompositeFieldContainer[DescribeQueueResponse]
    next_cursor: str
    has_more: bool
    total_count: int
    def __init__(self, queues: _Optional[_Iterable[_Union[DescribeQueueResponse, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., has_more: bool = ..., total_count: _Optional[int] = ...) -> None: ...

class DescribeQueueRequest(_message.Message):
    __slots__ = ("queue_id", "queue_name")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    queue_name: str
    def __init__(self, queue_id: _Optional[str] = ..., queue_name: _Optional[str] = ...) -> None: ...

class DescribeQueueResponse(_message.Message):
    __slots__ = ("queue_id", "queue_name", "created_at", "retention_period_seconds", "visibility_timeout_seconds", "max_receive_attempts", "eviction_policy", "dead_letter_queue_id")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_RECEIVE_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    EVICTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    queue_name: str
    created_at: _timestamp_pb2.Timestamp
    retention_period_seconds: int
    visibility_timeout_seconds: int
    max_receive_attempts: int
    eviction_policy: EvictionPolicy
    dead_letter_queue_id: str
    def __init__(self, queue_id: _Optional[str] = ..., queue_name: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., retention_period_seconds: _Optional[int] = ..., visibility_timeout_seconds: _Optional[int] = ..., max_receive_attempts: _Optional[int] = ..., eviction_policy: _Optional[_Union[EvictionPolicy, str]] = ..., dead_letter_queue_id: _Optional[str] = ...) -> None: ...

class CreateQueueRequest(_message.Message):
    __slots__ = ("queue_name", "retention_period_seconds", "visibility_timeout_seconds", "max_receive_attempts", "eviction_policy", "dead_letter_queue_id")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_RECEIVE_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    EVICTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    retention_period_seconds: int
    visibility_timeout_seconds: int
    max_receive_attempts: int
    eviction_policy: EvictionPolicy
    dead_letter_queue_id: str
    def __init__(self, queue_name: _Optional[str] = ..., retention_period_seconds: _Optional[int] = ..., visibility_timeout_seconds: _Optional[int] = ..., max_receive_attempts: _Optional[int] = ..., eviction_policy: _Optional[_Union[EvictionPolicy, str]] = ..., dead_letter_queue_id: _Optional[str] = ...) -> None: ...

class CreateQueueResponse(_message.Message):
    __slots__ = ("queue_id",)
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    def __init__(self, queue_id: _Optional[str] = ...) -> None: ...

class PurgeQueueRequest(_message.Message):
    __slots__ = ("queue_id",)
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    def __init__(self, queue_id: _Optional[str] = ...) -> None: ...

class PurgeQueueResponse(_message.Message):
    __slots__ = ("messages_count",)
    MESSAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    messages_count: int
    def __init__(self, messages_count: _Optional[int] = ...) -> None: ...

class DeleteQueueRequest(_message.Message):
    __slots__ = ("queue_id", "force")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    force: bool
    def __init__(self, queue_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class DeleteQueueResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendRequest(_message.Message):
    __slots__ = ("queue_id", "messages")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    messages: _containers.RepeatedCompositeFieldContainer[SendMessage]
    def __init__(self, queue_id: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[SendMessage, _Mapping]]] = ...) -> None: ...

class SendResponse(_message.Message):
    __slots__ = ("message_ids",)
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    message_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ReceiveRequest(_message.Message):
    __slots__ = ("queue_id", "batch_size", "wait_time_seconds")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    batch_size: int
    wait_time_seconds: int
    def __init__(self, queue_id: _Optional[str] = ..., batch_size: _Optional[int] = ..., wait_time_seconds: _Optional[int] = ...) -> None: ...

class ReceiveResponse(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[ReceiveMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[ReceiveMessage, _Mapping]]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("queue_id", "message_ids")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    message_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, queue_id: _Optional[str] = ..., message_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("successful", "failed")
    SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    successful: _containers.RepeatedScalarFieldContainer[str]
    failed: _containers.RepeatedCompositeFieldContainer[DeleteFailure]
    def __init__(self, successful: _Optional[_Iterable[str]] = ..., failed: _Optional[_Iterable[_Union[DeleteFailure, _Mapping]]] = ...) -> None: ...

class DeleteFailure(_message.Message):
    __slots__ = ("message_id", "error")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    error: str
    def __init__(self, message_id: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class Topic(_message.Message):
    __slots__ = ("topic_id", "topic_name", "created_at", "subscriptions")
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    topic_name: str
    created_at: _timestamp_pb2.Timestamp
    subscriptions: _containers.RepeatedCompositeFieldContainer[Subscription]
    def __init__(self, topic_id: _Optional[str] = ..., topic_name: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., subscriptions: _Optional[_Iterable[_Union[Subscription, _Mapping]]] = ...) -> None: ...

class Subscription(_message.Message):
    __slots__ = ("subscription_id", "topic_id", "queue_id", "queue_name", "created_at")
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    topic_id: str
    queue_id: str
    queue_name: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, subscription_id: _Optional[str] = ..., topic_id: _Optional[str] = ..., queue_id: _Optional[str] = ..., queue_name: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PublishMessage(_message.Message):
    __slots__ = ("body",)
    BODY_FIELD_NUMBER: _ClassVar[int]
    body: bytes
    def __init__(self, body: _Optional[bytes] = ...) -> None: ...

class ListTopicsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTopicsResponse(_message.Message):
    __slots__ = ("topics",)
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[Topic]
    def __init__(self, topics: _Optional[_Iterable[_Union[Topic, _Mapping]]] = ...) -> None: ...

class CreateTopicRequest(_message.Message):
    __slots__ = ("topic_name",)
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    def __init__(self, topic_name: _Optional[str] = ...) -> None: ...

class CreateTopicResponse(_message.Message):
    __slots__ = ("topic_id",)
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ...) -> None: ...

class DeleteTopicRequest(_message.Message):
    __slots__ = ("topic_id",)
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ...) -> None: ...

class DeleteTopicResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("topic_id", "queue_id")
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    queue_id: str
    def __init__(self, topic_id: _Optional[str] = ..., queue_id: _Optional[str] = ...) -> None: ...

class SubscribeResponse(_message.Message):
    __slots__ = ("subscription_id",)
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ...) -> None: ...

class UnsubscribeRequest(_message.Message):
    __slots__ = ("topic_id", "subscription_id")
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    subscription_id: str
    def __init__(self, topic_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class UnsubscribeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PublishRequest(_message.Message):
    __slots__ = ("topic_id", "messages")
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    messages: _containers.RepeatedCompositeFieldContainer[PublishMessage]
    def __init__(self, topic_id: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[PublishMessage, _Mapping]]] = ...) -> None: ...

class PublishResponse(_message.Message):
    __slots__ = ("topic_id", "queue_ids", "message_ids", "delivered_count")
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_IDS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_COUNT_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    queue_ids: _containers.RepeatedScalarFieldContainer[str]
    message_ids: _containers.RepeatedScalarFieldContainer[str]
    delivered_count: int
    def __init__(self, topic_id: _Optional[str] = ..., queue_ids: _Optional[_Iterable[str]] = ..., message_ids: _Optional[_Iterable[str]] = ..., delivered_count: _Optional[int] = ...) -> None: ...

class QueueDeliveryReceipt(_message.Message):
    __slots__ = ("message_id", "receipt_handle")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    receipt_handle: str
    def __init__(self, message_id: _Optional[str] = ..., receipt_handle: _Optional[str] = ...) -> None: ...

class QueueDeliveryFailure(_message.Message):
    __slots__ = ("message_id", "code", "message")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    code: str
    message: str
    def __init__(self, message_id: _Optional[str] = ..., code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class QueueNackDelivery(_message.Message):
    __slots__ = ("receipt", "available_after_seconds", "reason")
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_AFTER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    receipt: QueueDeliveryReceipt
    available_after_seconds: int
    reason: str
    def __init__(self, receipt: _Optional[_Union[QueueDeliveryReceipt, _Mapping]] = ..., available_after_seconds: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class QueueExtendDelivery(_message.Message):
    __slots__ = ("receipt", "extension_seconds")
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    receipt: QueueDeliveryReceipt
    extension_seconds: int
    def __init__(self, receipt: _Optional[_Union[QueueDeliveryReceipt, _Mapping]] = ..., extension_seconds: _Optional[int] = ...) -> None: ...

class QueueExtendedDelivery(_message.Message):
    __slots__ = ("message_id", "receipt_handle", "lease_expires_at")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    LEASE_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    receipt_handle: str
    lease_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, message_id: _Optional[str] = ..., receipt_handle: _Optional[str] = ..., lease_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AcknowledgeQueueRequest(_message.Message):
    __slots__ = ("queue_id", "receipts")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIPTS_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    receipts: _containers.RepeatedCompositeFieldContainer[QueueDeliveryReceipt]
    def __init__(self, queue_id: _Optional[str] = ..., receipts: _Optional[_Iterable[_Union[QueueDeliveryReceipt, _Mapping]]] = ...) -> None: ...

class AcknowledgeQueueResponse(_message.Message):
    __slots__ = ("successful_message_ids", "failed")
    SUCCESSFUL_MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    successful_message_ids: _containers.RepeatedScalarFieldContainer[str]
    failed: _containers.RepeatedCompositeFieldContainer[QueueDeliveryFailure]
    def __init__(self, successful_message_ids: _Optional[_Iterable[str]] = ..., failed: _Optional[_Iterable[_Union[QueueDeliveryFailure, _Mapping]]] = ...) -> None: ...

class NackQueueRequest(_message.Message):
    __slots__ = ("queue_id", "deliveries")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERIES_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    deliveries: _containers.RepeatedCompositeFieldContainer[QueueNackDelivery]
    def __init__(self, queue_id: _Optional[str] = ..., deliveries: _Optional[_Iterable[_Union[QueueNackDelivery, _Mapping]]] = ...) -> None: ...

class NackQueueResponse(_message.Message):
    __slots__ = ("successful_message_ids", "failed")
    SUCCESSFUL_MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    successful_message_ids: _containers.RepeatedScalarFieldContainer[str]
    failed: _containers.RepeatedCompositeFieldContainer[QueueDeliveryFailure]
    def __init__(self, successful_message_ids: _Optional[_Iterable[str]] = ..., failed: _Optional[_Iterable[_Union[QueueDeliveryFailure, _Mapping]]] = ...) -> None: ...

class ExtendQueueLeaseRequest(_message.Message):
    __slots__ = ("queue_id", "deliveries")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERIES_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    deliveries: _containers.RepeatedCompositeFieldContainer[QueueExtendDelivery]
    def __init__(self, queue_id: _Optional[str] = ..., deliveries: _Optional[_Iterable[_Union[QueueExtendDelivery, _Mapping]]] = ...) -> None: ...

class ExtendQueueLeaseResponse(_message.Message):
    __slots__ = ("extended", "failed")
    EXTENDED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    extended: _containers.RepeatedCompositeFieldContainer[QueueExtendedDelivery]
    failed: _containers.RepeatedCompositeFieldContainer[QueueDeliveryFailure]
    def __init__(self, extended: _Optional[_Iterable[_Union[QueueExtendedDelivery, _Mapping]]] = ..., failed: _Optional[_Iterable[_Union[QueueDeliveryFailure, _Mapping]]] = ...) -> None: ...
