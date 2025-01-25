from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o")

# Define feedback template for feedback
positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a response for this positive feedback: {feedback}."),
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a response addressing this negative feedback: {feedback}."),
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a request for more details for this neutral feedback: {feedback}.",
        ),
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a message to escalate this feedback to a human agent: {feedback}.",
        ),
    ]
)

# Define the feedback classification template
classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}.",
        ),
    ]
)

# Define the runnable branches fro handling feedback
feedback_chain = RunnableBranch(
    (
        lambda x: "positive" in x,
        positive_feedback_template | llm | StrOutputParser(),  # Positive feedback chain
    ),
    (
        lambda x: "negative" in x,
        negative_feedback_template | llm | StrOutputParser(),  # Negative feedback chain
    ),
    (
        lambda x: "neutral" in x,
        neutral_feedback_template | llm | StrOutputParser(),  # Neutral feedback chain
    ),
    escalate_feedback_template | llm | StrOutputParser(),  # Escalate feedback chain
)


# Create the classification chain
classification_chain = classification_template | llm | StrOutputParser()


# Combine the classification chain and the feedback chain
final_chain = classification_chain | feedback_chain


review = "I'm not sure about the product yet. Can you tell me more about its features and benefits?"

result = final_chain.invoke({"feedback": review})

print(result)
