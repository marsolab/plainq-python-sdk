import os
from uuid import uuid4
import pytest
from plainq import Client, v1

@pytest.mark.integration
def test_real_broker():
    assert os.environ.get('PLAINQ_ADDR'), 'PLAINQ_ADDR must identify a disposable broker'
    name = f'py-{uuid4()}'
    queue_id = topic_id = None
    with Client(os.environ['PLAINQ_ADDR']) as client:
        try:
            queue_id = client.create_queue(v1.CreateQueueRequest(queue_name=name)).queue_id
            assert queue_id
            assert client.describe_queue(v1.DescribeQueueRequest(queue_id=queue_id)).queue_name == name
            assert client.list_queues(v1.ListQueuesRequest(queue_prefix=name)).queues[0].queue_id == queue_id
            payload = b'\x00\x01\x80\xff'
            sent = client.send(v1.SendRequest(queue_id=queue_id, messages=[v1.SendMessage(body=payload)]))
            received = client.receive(v1.ReceiveRequest(queue_id=queue_id, batch_size=10, wait_time_seconds=1))
            assert [m.id for m in received.messages] == list(sent.message_ids)
            assert received.messages[0].body == payload
            deleted = client.delete(v1.DeleteRequest(queue_id=queue_id, message_ids=sent.message_ids))
            assert deleted.successful == sent.message_ids and not deleted.failed
            topic_id = client.create_topic(v1.CreateTopicRequest(topic_name=name)).topic_id
            subscription = client.subscribe(v1.SubscribeRequest(topic_id=topic_id, queue_id=queue_id))
            assert any(t.topic_id == topic_id for t in client.list_topics(v1.ListTopicsRequest()).topics)
            published = client.publish(v1.PublishRequest(topic_id=topic_id, messages=[v1.PublishMessage(body=payload)]))
            assert published.delivered_count == 1 and list(published.queue_ids) == [queue_id]
            assert client.receive(v1.ReceiveRequest(queue_id=queue_id)).messages[0].body == payload
            client.unsubscribe(v1.UnsubscribeRequest(topic_id=topic_id, subscription_id=subscription.subscription_id))
            client.send(v1.SendRequest(queue_id=queue_id, messages=[v1.SendMessage(body=payload)]))
            assert client.purge_queue(v1.PurgeQueueRequest(queue_id=queue_id)).messages_count >= 1
            assert not client.receive(v1.ReceiveRequest(queue_id=queue_id)).messages
        finally:
            try:
                if topic_id: client.delete_topic(v1.DeleteTopicRequest(topic_id=topic_id))
            finally:
                if queue_id: client.delete_queue(v1.DeleteQueueRequest(queue_id=queue_id, force=True))
