# Imports
import os
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Connect to the Ganache blockchain
w3 = Web3(Web3.HTTPProvider(os.getenv("HTTP://127.0.0.1:7545")))

# Step 1: Import Ethereum Transaction Functions into the KryptoJobs2Go Application

# Import functions from crypto_wallet.py
from crypto_wallet import generate_account, get_balance, send_transaction

# KryptoJobs2Go Candidate Information
# Database of KryptoJobs2Go candidates including their name, digital address, rating, and hourly cost per Ether.
candidate_database = {
    "Lane": [
        "Lane",
        "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",
        "4.3",
        0.20,
        "Images/lane.jpeg",
    ],
    "Ash": [
        "Ash",
        "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396",
        "5.0",
        0.33,
        "Images/ash.jpeg",
    ],
    "Jo": [
        "Jo",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.7",
        0.19,
        "Images/jo.jpeg",
    ],
    "Kendall": [
        "Kendall",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.1",
        0.16,
        "Images/kendall.jpeg",
    ],
}

# A list of the KryptoJobs2Go candidates' first names
people = ["Lane", "Ash", "Jo", "Kendall"]

def get_people():
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("KryptoJobs2Go Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

# Streamlit application headings
st.markdown("# KryptoJobs2Go!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

# Streamlit Sidebar Code - Start
st.sidebar.markdown("## Client Account Address and Ethereum Balance in Ether")

# Step 1 - Part 4: Create a variable named `account`
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Step 1 - Part 5: Display the balance of the customer’s account
balance = get_balance(w3, account.address)
st.sidebar.write(f"Balance: {balance} Ether")

# Create a select box to choose a FinTech Hire candidate
person = st.sidebar.selectbox("Select a Person", people)

# Create an input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]
# Write the KryptoJobs2Go candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[person][3]
# Write the KryptoJobs2Go candidate's hourly rate to the sidebar
st.sidebar.write(f"Hourly Rate: {hourly_rate} Ether")

# Identify the KryptoJobs2Go candidate's Ethereum Address
candidate_address = candidate_database[person][1]
# Write the KryptoJobs2Go candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

st.sidebar.markdown("## Total Wage in Ether")

# Step 2 - Part 1: Calculate the candidate’s wage
wage = hourly_rate * hours
# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(f"Total Wage: {wage} Ether")

# Step 2 - Part 2: Send the transaction and get the transaction hash
if st.sidebar.button("Send Transaction"):
    transaction_hash = send_transaction(w3, account, candidate_address, wage)
    
    st.sidebar.markdown("#### Validated Transaction Hash")
    st.sidebar.write(transaction_hash)

    st.balloons()

# Function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page
get_people()

