key  ="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"

from openai import OpenAI
client = OpenAI(api_key=key)

response = client.chat.completions.create(
  model="gpt-o1",
  messages=[
        {
            "role": "user",
            "content": "complete this chat: Jack: Hey; Jill: How are you?; Jack: now what?; Jill:  ",
        }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


for choice in response.choices:
    print(choice.message.content)
