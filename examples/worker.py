"""Run with PLAINQ_ADDR and PLAINQ_QUEUE_ID set after installing plainq-sdk."""
import os
from plainq import Client, v1

with Client(os.environ.get("PLAINQ_ADDR", "localhost:8080")) as client:
    try:
        while True:
            response = client.receive(v1.ReceiveRequest(
                queue_id=os.environ["PLAINQ_QUEUE_ID"], batch_size=10, wait_time_seconds=20,
            ))
            for message in response.messages:
                print(message.id, message.body)  # replace with successful processing
                result = client.delete(v1.DeleteRequest(
                    queue_id=os.environ["PLAINQ_QUEUE_ID"], message_ids=[message.id],
                ))
                if result.failed:
                    raise RuntimeError(str(result.failed))
    except KeyboardInterrupt:
        pass
