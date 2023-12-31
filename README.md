**Project Overview:**
The ChatGPT + PostgreSQL application is a powerful tool designed to streamline offer searches within a postgreSQL database using LangChain. Leveraging advanced language models and embeddings, it empowers users to explore relevant offers effortlessly based on product categories, brands, or retailers.

**Approach and Methodology:**
This project harmonizes advanced language models with structured PostgreSQL databases to enhance offer retrieval efficiency. The integration of Large Language Model (LLM) capabilities enriches the system's querying prowess. Through the langchain, this integration bridges the gap between the language model and the PostrgreSQL database, enabling sophisticated interactions. A critical aspect involves crafting precise prompts that guide the LLM in executing optimized database queries. Rigorous iterations and fine-tuning sessions are undertaken to curate the most effective prompt structure. I proceeded with one-shot inference.

**Data Management:**
At the core of the system lies a meticulously constructed PostgreSQL database, meticulously structured from raw data contained in CSV files housed within the data directory. This creation process is orchestrated using a blend of sqlalchemy and pandas libraries. The integration of PostgreSQL database helps to scale the application. 

**Relevance Assessment:**
To gauge the relevance of fetched results concerning user queries, the application employs cosine similarity comparisons. The OPENAI embeddings feature plays a pivotal role in generating embeddings for this purpose, ultimately aiding in result ranking.

**User Interface:**
The entire application can be accessed through an API. The final output materializes into an intuitive Streamlit-based interface. Seamlessly parsing and presenting LLM-driven insights, this UI empowers users with interactive, user-friendly offer search functionalities.


**File Structure:**

[src/api.py](api.py) This module contains POST API built using FastAPI. This can be accessed from streamlit or browser or commandline.

[src/model.py](model.py) This module contains offer generation and scoring the generated offers functions. These functions are used in the API to return the final output. 

[src/stream.py](stream.py) This module helps to create UI and search offers for different categories, brands and retailors.

[src/tables.py](tables.py)  This module helps to create tables in postgresql and insert csv data into the tables. 

[requirements](requirements.txt) This file contains the necessary packages required for this project.

[data/](data/) This folder contains all raw data in csv format.


**Usage:**

Following are the steps required to follow to run the application smoothly.

* Create a virtual environment and activate it
```python
python3 -m venv fetch
source fetch/bin/activate 
```

* Clone the repository
```bash
git clone https://github.com/avinash-deyyam/FETCH_OFFER
cd fetch_offer
```

* Upgrade the libraries
```bash
pip install --upgrade pip
pip install --upgrade setuptools
```

* Install the packages from requirements file
```bash
pip install -r requirements.txt
```
  
There are few things that are mandatory to give to run the application.

(1) PostgreSQL host address and credentials

(2) OPENAI API key

These are stored as environmental variables in .env file.

* Use [src/tables.py](src/tables.py) to dump data from csv into tables

* Run [src/app.py](src/app.py) to start the API
```bash
cd src
python3 app.py
```

* Run [src/stream.py](src/stream.py) to start the web app
```bash
cd src
streamlit run stream.py
```

* API can also be accessed from commandline
```bash
curl -X POST 'http://0.0.0.0:8080/offers?text=query' -H 'Content-Type: application/json'
```  
Replace query with your search word

<img width="975" alt="Screenshot 2023-12-03 at 9 32 05 PM" src="https://github.com/avinash-deyyam/FETCH_OFFER/assets/45258206/e41f44fb-e31a-49d1-a5ac-3a37b05067ee">


**Sample Results:**

<img width="1339" alt="Screenshot 2023-12-03 at 9 20 05 PM" src="https://github.com/avinash-deyyam/FETCH_OFFER/assets/45258206/23cee607-2370-4f29-a653-1739a8885445">


<img width="1331" alt="Screenshot 2023-12-03 at 9 20 52 PM" src="https://github.com/avinash-deyyam/FETCH_OFFER/assets/45258206/d4d7ed1a-4f8b-427a-9be3-80e539c44537">


<img width="1289" alt="Screenshot 2023-12-03 at 9 27 00 PM" src="https://github.com/avinash-deyyam/FETCH_OFFER/assets/45258206/134def56-e045-4cf5-85b1-57cb1e9b317c">
