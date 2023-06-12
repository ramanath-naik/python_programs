import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response['choices'][0]['text'])