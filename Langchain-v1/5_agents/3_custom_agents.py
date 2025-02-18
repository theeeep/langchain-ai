import os

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Define agent role and instructions
agent_role = "You are an Expert EMAIL SUMMARIZER. Your task is to CREATE a clear and CONCISE summary."
agent_instructions = """Your task is to follow these steps to summarize an email effectively:
1. READ the entire email thoroughly.
2. IDENTIFY the main topics and key points.
3. CONDENSE the information into a brief, coherent summary.
4. ENSURE the summary captures the essence of the email.
5. AVOID including unnecessary details or jargon.
"""

# Define a dummy tool to simulate processing the email


@tool
def summarize_email(email_content: str) -> str:
    """
    Summarizes the given email content.  This is a dummy tool and should be replaced with actual summarization logic.
    """
    # In a real application, this function would use an LLM or other method to summarize the email.
    return "This is a dummy summary of the email."


# Create the Language Model Instance
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")

# Create the Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            f"{agent_role}\n{agent_instructions}",
        ),  # Incorporate role and instructions
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

# Define the tools
toolkit = [summarize_email]

# Create the Agent
agent = create_openai_tools_agent(llm, toolkit, prompt)

# Set up the Agent Executor
agent_executor = AgentExecutor(agent=agent, tools=toolkit, verbose=True)

# Run the Agent
email_content = "Subject: Project Update\n\nHi Team,\n\nThis email is to provide an update on the ongoing project.  We've completed phase 1, but we're slightly behind schedule due to unforeseen issues.  Phase 2 is expected to start next week.  Please review the attached report for full details.\n\nThanks,\nJohn"
result = agent_executor.invoke(
    {"input": f"Please summarize the following email: {email_content}"}
)
print(result["output"])
