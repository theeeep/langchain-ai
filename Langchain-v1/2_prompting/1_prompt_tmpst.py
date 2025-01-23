from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning that {qualifications} are required and {skills} are strength. The email should be 4 lines long max."

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke(
    {
        "tone": "Professional",
        "company": "LangChain",
        "position": "Software Engineer",
        "qualifications": "Bachelor's degree in Computer Science",
        "skills": "Python, SQL, Git",
    }
)

response = llm.invoke(prompt)

print(response.content)
