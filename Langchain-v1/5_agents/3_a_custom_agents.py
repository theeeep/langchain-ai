# import os

# from dotenv import load_dotenv
# from langchain.agents import AgentExecutor, create_openai_tools_agent
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.tools import tool
# from langchain_openai import ChatOpenAI

# # Load environment variables
# load_dotenv()

# # 1. Configuration (Example using a dictionary, but can be from a file or database)
# available_llms = {
#     "openai_gpt4o": {
#         "provider": "openai",
#         "model_name": "gpt-4o-mini",
#         "api_key": os.getenv("OPENAI_API_KEY"),
#     }
# }

# available_tools = {
#     "math": [add, multiply],
#     "email_summarization": [summarize_email],  # Assumes you have these defined
# }


# # 2. LLM Factory (Modified to load API key dynamically)
# class LLMFactory:
#     @staticmethod
#     def create_llm(llm_config: dict):
#         provider = llm_config["provider"]
#         model_name = llm_config["model_name"]
#         api_key = llm_config["api_key"]

#         if provider == "openai":
#             return ChatOpenAI(model_name=model_name, api_key=api_key)
#         else:
#             raise ValueError(f"Unsupported LLM provider: {provider}")


# # 3. Tool Definitions (As before)
# @tool
# def add(a: int, b: int) -> int:
#     """Add two numbers."""
#     return a + b


# @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers."""
#     return a * b


# @tool
# def summarize_email(email_content: str) -> str:
#     """
#     Summarizes the given email content.  This is a dummy tool and should be replaced with actual summarization logic.
#     """
#     # In a real application, this function would use an LLM or other method to summarize the email.
#     return "This is a dummy summary of the email."


# # 4. Prompt Factory
# class PromptFactory:
#     @staticmethod
#     def create_prompt(agent_purpose: str):
#         if agent_purpose == "email_summarizer":
#             system_message = """You are an Expert EMAIL SUMMARIZER. Your task is to CREATE a clear and CONCISE summary.
#             Follow these steps to summarize an email effectively:
#             1. READ the entire email thoroughly.
#             2. IDENTIFY the main topics and key points.
#             3. CONDENSE the information into a brief, coherent summary.
#             4. ENSURE the summary captures the essence of the email.
#             5. AVOID including unnecessary details or jargon.
#             """
#         elif agent_purpose == "code_generator":
#             system_message = "You are an expert code generator."
#         elif agent_purpose == "math_solver":
#             system_message = "You are an expert mathematical assistant. Use your tools to solve math problems."
#         else:
#             raise ValueError(f"Unsupported agent purpose: {agent_purpose}")

#         return ChatPromptTemplate.from_messages(
#             [
#                 ("system", system_message),
#                 MessagesPlaceholder("chat_history", optional=True),
#                 ("human", "{input}"),
#                 MessagesPlaceholder("agent_scratchpad"),
#             ]
#         )


# # 5. Agent Factory
# class AgentFactory:
#     @staticmethod
#     def create_agent(llm, tools, prompt, agent_type="openai_tools"):  # Added agent_type
#         if agent_type == "openai_tools":
#             agent = create_openai_tools_agent(llm, tools, prompt)
#         # Implement other agent types if needed
#         else:
#             raise ValueError(f"Unsupported agent type: {agent_type}")

#         return agent


# # 6. Main Function (Illustrative)
# async def create_and_run_agent(llm_name: str, agent_purpose: str, user_query: str):
#     # 1. Load configurations
#     llm_config = available_llms.get(llm_name)
#     if not llm_config:
#         return {"status": "error", "error": f"LLM not found: {llm_name}"}

#     # 2. Create LLM
#     llm = LLMFactory.create_llm(llm_config)

#     # 3. Select tools based on agent purpose (example)
#     if agent_purpose == "email_summarizer":
#         tools = available_tools["email_summarization"]
#     elif agent_purpose == "math_solver":
#         tools = available_tools["math"]
#     else:
#         return {
#             "status": "error",
#             "error": f"Tools not configured for agent purpose: {agent_purpose}",
#         }

#     # 4. Create Prompt
#     prompt = PromptFactory.create_prompt(agent_purpose)

#     # 5. Create Agent
#     agent = AgentFactory.create_agent(llm, tools, prompt)

#     # 6. Create Agent Executor
#     agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

#     # 7. Run Agent
#     try:
#         response = await agent_executor.ainvoke({"input": user_query})
#         return {
#             "status": "success",
#             "response": response["output"],
#             "thought_process": response.get("intermediate_steps", []),
#         }
#     except Exception as e:
#         return {"status": "error", "error": str(e)}


# # Example Usage
# async def main():
#     user_llm_choice = "openai_gpt4o"  # Example user choice
#     user_agent_purpose = "math_solver"  # Example agent purpose
#     user_query = "What is 1 + 1?"  # Example user query

#     result = await create_and_run_agent(user_llm_choice, user_agent_purpose, user_query)
#     print(result)


# if __name__ == "__main__":
#     import asyncio

#     asyncio.run(main())
