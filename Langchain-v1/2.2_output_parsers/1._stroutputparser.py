from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o")

# 1st Prompt -> Detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

# 2nd Prompt ->  summary
template2 = PromptTemplate(
    template="Write a 5 lines summary on the following text. /n {text}",
    input_variables=["text"],
)

prompt1 = template1.invoke({"topic": "Black holes"})

result1 = llm.invoke(prompt1)

prompt2 = template2.invoke({"text": result1.content})

result2 = llm.invoke(prompt2)

print(result2.content)
