from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o")

memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

conversation.predict(input="Hi, my name is Deepak")
conversation.predict(input="What is 1+1?")
conversation.predict(input="What is my name?")
