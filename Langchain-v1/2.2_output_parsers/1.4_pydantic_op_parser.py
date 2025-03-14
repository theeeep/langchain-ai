from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o")


class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(description="The age of the person")
    address: str = Field(description="The address of the person")


parser = PydanticOutputParser(pydantic_object=Person)

prompt = PromptTemplate(
    template="Give me the name,age and address of a frictional person \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = prompt | llm | parser

result = chain.invoke({"topic": "Black holes"})

print(result)
print(result.name)
print(result.age)
print(result.address)
