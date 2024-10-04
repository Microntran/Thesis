from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import re
from dotenv import load_dotenv

# Database connection details (used for MySQL integration)
load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Checking
if None in [db_user, db_password, db_host, db_port, db_name]:
    raise ValueError("One or more environment variables for database connection are not set")

db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create the database engine and import dataset
engine = create_engine(db_url)
query = "SELECT * FROM customer_churn"
df = pd.read_sql(query, engine)

# Define a prompt template for the chatbot with more context and few-shot examples
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a data analyst assistant. You help with analyzing customer churn data. "
                   "The dataset contains information about customers, including their "
                   "complaints, call failures, and whether they churned. " 
		   "Use this context to answer questions."),
        ("user", "How many customers have churned?"),
        ("assistant", "The number of customers who have churned is 150."),
        ("user", "What is the average tenure of customers?"),
        ("assistant", "The average tenure of customers is 24.5 months."),
        ("user", "List all customers who have churned."),
        ("assistant", "Here is the list of all customers who have churned: [List of customers]"),
        ("user", "Question: {question}")
    ]
)

# Set up the Streamlit framework
st.title('Langchain Chatbot With LLAMA3 model by Gabriele Ometo')

# Initialize the Ollama model
llm = Ollama(model="llama3.1:8b")

# Create a chain that combines the prompt and the Ollama model
chain = prompt | llm

# Function to parse natural language questions into SQL queries
def parse_question_to_sql(question):
    if "how many customers have churned" in question.lower():
        return "SELECT COUNT(*) FROM customer_churn WHERE churn=1"
    elif "what is the average tenure of customers" in question.lower():
        return "SELECT AVG(tenure) FROM customer_churn"
    elif "list all customers who have churned" in question.lower():
        return "SELECT * FROM customer_churn WHERE churn=1"
    elif "which feature is most related to churn" in question.lower():
        return "SELECT * FROM customer_churn"  # Placeholder for a more complex analysis
    # Add more rules as needed
    return None

# Initialize the chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to process input and query the database
def queryDB(question):
    sql_query = parse_question_to_sql(question)
    if sql_query:
        try:
            result_df = pd.read_sql(sql_query, engine)
            if not result_df.empty:
                if "count" in sql_query.lower():
                    response = f"The number of customers who have churned is {result_df.iloc[0, 0]}."
                elif "avg" in sql_query.lower():
                    response = f"The average tenure of customers is {round(result_df.iloc[0, 0], 2)} months."
                else:
                    response = result_df.to_string(index=False)
            else:
                response = "No results found."
        except Exception as e:
            response = f"Error executing query: {e}"
    else:
        response = chain.invoke({"question": question})
    return response

# Initialize the chat messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Streamlit's chat input handling
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display the chat history using Streamlit's chat_message
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Process and respond to the last user input
if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = queryDB(prompt) 
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Example of Prompt that I used in thesis: Build the best machine learning model based on binomial variable 'churn' and then execute it to predict churn rate.
