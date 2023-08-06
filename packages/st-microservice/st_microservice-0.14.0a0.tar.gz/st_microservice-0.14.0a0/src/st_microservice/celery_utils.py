import asyncio
import celery
from celery.result import AsyncResult
from redis.asyncio import Redis


def get_run_async_function():
    loop = asyncio.get_event_loop_policy().get_event_loop()

    def run_async(future):
        return loop.run_until_complete(future)

    return run_async


def get_send_message_function(task_self: celery.Task, redis: Redis):
    def send_message(message: str):
        redis.publish(f'celery-task-updates-{task_self}', message)

    return send_message


async def wait_and_receive_messages(task_result: AsyncResult, redis: Redis):
    # Todo: Check if will lose message if waiting for too long
    sub = redis.pubsub(ignore_subscribe_messages=True)
    await sub.subscribe(f'celery-task-updates-{task_result.task_id}')
    while not task_result.ready():
        await asyncio.sleep(0.5)
        while (message_raw := await sub.get_message()) is not None:
            yield message_raw['data']


def create_celery_app(redis_uri: str):
    app = celery.Celery('tasks', broker=redis_uri, backend=redis_uri)
    app.conf.task_serializer = 'pickle'
    return app
