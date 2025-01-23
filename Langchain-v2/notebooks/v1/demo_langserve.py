from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-pro")
message = [HumanMessage(content="You are a nice Bot. What is Langchain?")]
response = model.invoke(message)
print(response.content)
