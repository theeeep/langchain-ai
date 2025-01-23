from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm_model = ChatOpenAI(model_name="gpt-4o")

messages = [
    SystemMessage(content="You are an expert in social media content strategy."),
    HumanMessage(content="Give a short tip to create more engagement on social media."),
]

response = llm_model.invoke(messages)

print(response.content)
