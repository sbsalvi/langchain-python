from decouple import config
from langchain_openai import OpenAI
SECRECT_KEY = config("OPENAI_API_KEY")

# TO use llm openai
llm = OpenAI("SECRECT_KEY")
response = llm.invoke("What is your favourite number ?")
print(response)