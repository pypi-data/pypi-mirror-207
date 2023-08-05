from dotenv import load_dotenv
import os
from gpt4_openai import GPT4OpenAI

print(GPT4OpenAI.__file__)
load_dotenv()

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=os.environ["OPENAI_SESSION_TOKEN"], headless=False)
response = llm('How ')
print(response)

# from langchain import PromptTemplate, LLMChain

# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     SystemMessagePromptTemplate,
#     AIMessagePromptTemplate,
#     HumanMessagePromptTemplate,
# )

# from chatgpt_api import ChatGPT
# llm = ChatGPT(token=token)

# template="You are a helpful assistant that translates english to pirate."
# system_message_prompt = SystemMessagePromptTemplate.from_template(template)
# example_human = HumanMessagePromptTemplate.from_template("Hi")
# example_ai = AIMessagePromptTemplate.from_template("Argh me mateys")
# human_template="{text}"
# human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])
# chain = LLMChain(llm=llm, prompt=chat_prompt)
# print('chain run:', chain.run("My plants are not very impressed with the humidity in my room"))

