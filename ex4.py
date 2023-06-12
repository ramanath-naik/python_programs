import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["#", ";"]
)
print(response['choices'][0]['text'])