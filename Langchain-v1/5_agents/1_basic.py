import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor, tool

load_dotenv()


@tool
def get_current_time(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Return the current date and time in the specified format."""
    current_time = datetime.datetime.now().strftime(format)
    return current_time


llm = ChatOpenAI(model_name="gpt-4o")

query = "What is current time? Just show the time."

prompt_template = hub.pull("hwchase17/react")

tools = [get_current_time]

agent = create_react_agent(llm, tools, prompt_template)

# agent_executor = AgentExecutor.from_agent_and_tools(agent, tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({"input": query})
