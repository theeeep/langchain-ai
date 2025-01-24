from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o")

# Define prompt template for movie summary
movie_summary_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a movie summary and critic expert"),
        ("human", "Tell me a  brief summary of the movie {movie}"),
    ]
)


# Define plot analysis step
def analyze_plot(plot):
    plot_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a movie plot expert"),
            (
                "human",
                "Analyze the plot: {plot}. What are its strengths and weaknesses?",
            ),
        ]
    )
    return plot_template.format(plot=plot)


# Define character analyse step
def analyze_character(character):
    character_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a movie character expert"),
            (
                "human",
                "Analyze the character: {character}. What are their strengths and weaknesses?",
            ),
        ]
    )
    return character_template.format(character=character)


# Combine analyses into final verdict
def combined_verdict(plot_analysis, character_analysis):
    return (
        f"Plot Analysis:\n{plot_analysis}\n\nCharacter Analysis:\n{character_analysis}"
    )


# Simplify branches with LCEL
plot_branch_chain = RunnableLambda(lambda x: analyze_plot(x)) | llm | StrOutputParser()

character_branch_chain = (
    RunnableLambda(lambda x: analyze_character(x)) | llm | StrOutputParser()
)


# Create parallel chain
movie_summary_chain = (
    movie_summary_prompt_template
    | llm
    | StrOutputParser()
    | RunnableParallel(
        branches={"plot": plot_branch_chain, "character": character_branch_chain}
    )
    | RunnableLambda(
        lambda x: combined_verdict(x["branches"]["plot"], x["branches"]["character"])
    )
)

# Run the chain with the input variables
output = movie_summary_chain.invoke({"movie": "Creed"})

print(output)
