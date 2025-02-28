"""
    
"""
from langchain.schema.output_parser import StrOutputParser
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from neogpt.prompts.prompt import few_shot_prompt, stepback_prompt
from langchain.schema.runnable import RunnableLambda
from langchain.chains import RetrievalQA
import logging

search = DuckDuckGoSearchAPIWrapper(max_results=4)

def retriever(query):
    return search.run(query)

def stepback(llm,db):
    general_prompt = few_shot_prompt()
    question_gen = general_prompt | llm | StrOutputParser()
    # question = "was chatgpt around while trump was president?"
    # print(retriever(question_gen.invoke({"question": question})))
    prompt, memory = stepback_prompt()
    
    chain = {
        "normal_context": RunnableLambda(lambda x: x['question']) | retriever,
        "step_back_context": question_gen | retriever,
        "question": lambda x: x["question"]
    } | prompt | llm | StrOutputParser() 
    logging.info("Stepback Prompting Retriever Loaded Successfully")
    

    return chain
    # return x


    

