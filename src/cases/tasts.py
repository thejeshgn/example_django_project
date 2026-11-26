from dramatiq import actor


@actor
def hello_message():
    print("hello as part of tasks")
