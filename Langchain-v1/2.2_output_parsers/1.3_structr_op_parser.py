from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o")

# Define the schema for the output
schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

# Create the parser
parser = StructuredOutputParser.from_response_schemas(schema)

# Create the prompt template
prompt = PromptTemplate(
    template="Give me 3 facts about {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Create the chain
chain = prompt | llm | parser

# Run the chain
result = chain.invoke({"topic": "Black holes"})

print(result)
