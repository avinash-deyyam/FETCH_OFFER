import streamlit as st
import requests
from streamlit_extras.add_vertical_space import add_vertical_space
import os

# Sidebar contents

def main():
    with st.sidebar:
        st.title('🤗 Fetch Offers')
        st.title('Wanted to know more about us!!!')
        st.title('Visit https://fetch.com/')
        add_vertical_space(5)
    st.header("Offers Retrieval")
    # Accept user questions/query
    query = st.text_input("Search for brand/category/retailer")

    if query:
        # URL of your FastAPI endpoint
        url = "http://0.0.0.0:8080/offers?text=query"  # Replace with your API endpoint URL

        # Send POST request to the FastAPI endpoint
        response = requests.post(url)

        # Print the response
        output = response.json()
        if 'text' in output:          
            st.write(output['text'])
        else:
            st.write(output)

if __name__ == '__main__':
    main()