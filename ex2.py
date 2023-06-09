import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Translate this into 1. portuguese:\n\nWhat is your name?\n\n1.",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response['choices'][0]['text'])