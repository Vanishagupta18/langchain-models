from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.9, max_tokens=10)

result=model.invoke("tell me a joke")

print(result.content)