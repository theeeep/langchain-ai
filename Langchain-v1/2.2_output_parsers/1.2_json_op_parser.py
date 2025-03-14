from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o")


parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name,age and address of a frictional person \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | llm | parser

result = chain.invoke({"topic": "Black holes"})

print(result)
