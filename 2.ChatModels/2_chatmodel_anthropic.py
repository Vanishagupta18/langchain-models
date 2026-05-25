from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022', temperature=0.9, max_tokens=10)

result=model.invoke("tell me a joke")

print(result.content)