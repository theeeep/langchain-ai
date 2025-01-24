from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o")

# Define prompt template with input variables (No need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a fact expert who knows facts about {animal}"),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Create invididual Runnable chains for each input variable
# formats a prompt using the ChatPromptTemplate.
format_prompt = RunnableLambda(lambda x: prompt_template.format(**x))
# send the formatted prompt to the language model (LLM).
# Modify the invoke_llm to handle string input correctly
invoke_llm = RunnableLambda(lambda x: llm.invoke([{"role": "user", "content": x}]))
# extract the content from the LLM's response
parse_output = RunnableLambda(lambda x: x.content)

# Create the RunnableSequence chain (Similiar to LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_llm], last=parse_output)

response = chain.invoke({"animal": "cat", "fact_count": 2})

print(response)
