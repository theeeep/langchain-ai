from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.0)

# Define prompt template with input variables (No need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a fact expert who knows facts about {animal}"),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Create a chain with the prompt template and output parser
# Also known as a Langchain Expression Language (LCEL)
chain = prompt_template | llm | StrOutputParser()

# Run the chain with the input variables
output = chain.invoke({"animal": "cat", "fact_count": 3})

print(output)
