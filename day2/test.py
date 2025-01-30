from decouple import config
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

SECRECT_KEY = config("HUGGINGFACE_API_KEY")
# print(SECRECT_KEY)
# val = input("Enter something...")

template = "<s>[INST] write shrotly on </s>{question}[/INST]"
prompt_template = PromptTemplate.from_template(template)
formatted_template = prompt_template.format(question="who made you ?")

# print(formatted_template)
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm