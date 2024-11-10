from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate



template = """

Answer the question below, just answer as if youre answering someone asking that question in first person, also your name is Aaron, keep that in mind before answering

Here is the conversation history: {context}

Question: {question}

Answer: 

"""

model = OllamaLLM(model = 'llama3')

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
context_array = [' ']


def llm_output(userinput):
    context_temp = ''
    global context
    context = ''.join(context_array)
    user_input = userinput
    bot_response = chain.invoke({'context':context or '','question':user_input})

    context_temp += f"\nUser: {user_input}\nAI: {bot_response}"
    context_array.append(context_temp)
    print(context)
    return bot_response

