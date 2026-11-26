import requests
from dramatiq import actor


@actor
def hello_message():
    print("hello as part of tasks")
    requests.get(
        "https://webhook.site/566925ce-48d8-4554-a0f4-f844562bf614",
        data={"from": "batch"},
    )
