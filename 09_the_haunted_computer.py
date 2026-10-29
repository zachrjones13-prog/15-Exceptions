import random
import time

scary_messages = [
    "Who is standing behind you?",
    "Your files are disappearing...",
    "I know what you did.",
    "Something just moved.",
    "Do not shut me down."
]

for attempt in range(10):
    try:
        index = random.randint(0, 5)
        print(scary_messages[index])

    except IndexError:
        print("ERROR: Something is trying to communicate...")

    finally:
        print("The computer is watching you.")

    time.sleep(1)