from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
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

# Output parser
parser = StrOutputParser()


# Chains
chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({"topic": "Black holes"})

print(result)
