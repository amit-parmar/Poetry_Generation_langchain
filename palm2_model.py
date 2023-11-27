import os
from lang_key import lang_key, palm_key
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain .chains import SequentialChain
palm_key = palm_key

llm = GooglePalm(google_api_key=palm_key, temperature=0.7)

def generate_shayaris(poet_name):
    prompt_template = PromptTemplate(
        input_variables = ['poet_name'],
        template = "Create a shayari like {poet_name}"
    )

    shayri_chain = LLMChain(llm=llm, prompt = prompt_template, output_key = 'shayari')

    chain = SequentialChain(
        chains = [shayri_chain],
        input_variables = ['poet_name'],
        output_variables = ["shayari"]
    )
    
    response = chain({'poet_name':poet_name})

    return response


# if __name__ == '__main__':

#     generate_shayaris('faiz ahmed faiz')

