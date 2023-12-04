from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
import os
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import ast
import numpy as np
import pandas as pd
from functools import reduce

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
username = os.getenv("username")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
mydatabase = os.getenv("mydatabase")

def flatten_lst(ls):
  return reduce(lambda x,y:x+y, ls)

def prompt(question):
    # Set up langchain
    pg_uri = f"postgresql+psycopg2://{username}:{password}@{host}/{mydatabase}"
    db = SQLDatabase.from_uri(pg_uri)
    llm = OpenAI(temperature=0, verbose=True)
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)

    PROMPT = """Task Description: Retrieve relevant offers from the 'offer_retailer' table based on a query. Check the tables independently and then merge if needed to extract the offers.
    If no offers are found then return 'No offers found'. The offers in the output are seperated by &&.

    Examples:
    Example 1:
    Query: Red Pasta Sauce
    SQL Query:
    SELECT "OFFER" FROM offer_retailer
    INNER JOIN brand_category ON offer_retailer."BRAND" = brand_category."BRAND"
    INNER JOIN categories ON brand_category."BRAND_BELONGS_TO_CATEGORY" = categories."PRODUCT_CATEGORY"
    WHERE categories."PRODUCT_CATEGORY" ILIKE '%Red Pasta Sauce%' OR brand_category."BRAND" ILIKE '%Red Pasta Sauce%' OR offer_retailer."RETAILER" ILIKE '%Red Pasta Sauce%' LIMIT 3;
    SQL Result:
    [('Barilla® pasta, select varieties, buy 2',),
    ('Barilla® pasta, select varieties, buy 4',),
    ('Barilla® pasta, select varieties, buy 3',)]
    Expected Output:
    Barilla® pasta, select varieties, buy 2&&Barilla® pasta, select varieties, buy 4&&Barilla® pasta, select varieties, buy 3

    The question: {question}"""
    output = db_chain.run(PROMPT.format(question=question))
    return output

def scores(output,question):
    embeddings = OpenAIEmbeddings()
    if output == 'No offers found' or output == 'No offers found.':
        return output
    elif 'Answer' in output:
        offer_list = ast.literal_eval(output.split('Answer')[0].strip())
        scores = []
        input_embedding = np.asarray(embeddings.embed_query(question))
        offer_list = flatten_lst(offer_list)
        for offer in offer_list:
            offer_embedding = np.asarray(embeddings.embed_query(offer))
            scores.append(offer_embedding.dot(input_embedding))
    else:
        offer_list = output.split('&&')
        scores = []
        input_embedding = np.asarray(embeddings.embed_query(question))
        for offer in offer_list:
            offer_embedding = np.asarray(embeddings.embed_query(offer))
            scores.append(offer_embedding.dot(input_embedding))

    sorted_scores = pd.DataFrame({'score':scores,'offer':offer_list}).sort_values(by = ['score'], ascending = False).reset_index(drop = True)
    return sorted_scores



