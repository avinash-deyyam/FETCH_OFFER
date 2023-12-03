**Project Overview:**
The ChatGPT + PostgreSQL application is a powerful tool designed to streamline offer searches within a postgreSQL database on GCP using LangChain. Leveraging advanced language models and embeddings, it empowers users to explore relevant offers effortlessly based on product categories, brands, or retailers.

**Approach and Methodology:**
The project orchestrates a seamless marriage between cutting-edge language models and structured PostgreSQL databases to facilitate smart and efficient offer retrieval. The integration of Large Language Model (LLM) capabilities enriches the system's querying prowess. Through the langchain, this integration bridges the gap between the language model and the PostrgreSQL database, enabling sophisticated interactions. A critical aspect involves crafting precise prompts that guide the LM in executing optimized database queries. Rigorous iterations and fine-tuning sessions are undertaken to curate the most effective prompt structure. I proceeded with one-shot inference.

**Data Management:**
At the core of the system lies a meticulously constructed PostgreSQL database, meticulously organized from raw data contained in CSV files housed within the data directory. This creation process is orchestrated using a blend of sqlalchemy and pandas libraries. The integration of PostgreSQL database helps to scale the application. 

**Docker and API**
The entire application can be accessed through an API which is placed in a docker. Dockerizing an API streamlines deployment and management by encapsulating the entire application within containers. This approach ensures consistent operation across diverse environments, simplifies collaboration, and enables seamless scaling through container orchestration. By providing a standardized runtime environment, Docker enhances portability, accelerates development cycles, and fosters robust CI/CD pipelines, optimizing the efficiency and reliability of API deployment.

**Relevance Assessment:**
To gauge the relevance of fetched results concerning user queries, the application employs cosine similarity comparisons. The OPENAI embeddings feature plays a pivotal role in generating embeddings for this purpose, ultimately aiding in result ranking.

**User Interface:**
The final output materializes into an intuitive Streamlit-based interface. Seamlessly parsing and presenting LM-driven insights, this UI empowers users with interactive, user-friendly offer search functionalities.

File Structure

api.py This file contains POST API built using FastAPI. This can be accessed from streamlit or browser or commandline.

model.py This module contains offer generation and scoring the generated offers functions. These functions are used in the API to return the final output. 

stream.py This module helps to create UI and search offers for different categories, brands and retailors.

tables.py  This module helps to creat tables in postgresql and insert csv data into the tables. 

requirements.txt This file contains the necessary packages required for this project.

Dockerfile This file contains build instructions for API deployment using Docker.

data/ This folder contains all raw data in csv format.

Usage:

There are few things that are mandatory to have to run the application.

(1) PostgreSQL host address and credentials
(2) OPENAI API key

These are stored as environmental variables in .env file.


