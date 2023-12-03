import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
mydatabase = os.getenv("mydatabase")

# Create the connection string for SQLAlchemy
conn_str = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{mydatabase}'

# Create SQLAlchemy Engine
engine = create_engine(conn_str)

# Write DataFrame to PostgreSQL
table_ids = ['offer_retailer','categories','brand_category']
for table_id in table_ids:
  try:
      df = pd.read_csv(f'{table_id}.csv')
      df.to_sql(table_id, engine, if_exists='replace', index=False)
      print(f"{table_id} DataFrame successfully inserted into PostgreSQL!")
  except Exception as e:
      print("Error:", e)