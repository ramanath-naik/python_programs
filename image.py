
import openai

openai.api_key="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"

response = openai.Image.create_edit(
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']




