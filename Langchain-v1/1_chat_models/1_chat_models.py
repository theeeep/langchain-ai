from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm_model = ChatOpenAI(model_name="gpt-4o")

response = llm_model.invoke("What is 2+2 ?")

print(response.content)
