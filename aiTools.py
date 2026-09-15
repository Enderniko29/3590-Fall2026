from mellea import start_session

m = start_session()

response1 = m.instruct("Say hello in one sentence and an emoji.")
# print(response1)

response2 = m.instruct("What is capital of France?")
# print(response2)

response3 = m.instruct("Write a haiku about Python")
# print(response3)

response4 = m.instruct("Explain what a Python list is")
# print(response4)

# A better implementation - what Mellea can do
from mellea import generative


@generative
def write_haiku(topic: str) -> str:
    """Write a haiku about the given topic."""

print(write_haiku(m, topic="Python"))