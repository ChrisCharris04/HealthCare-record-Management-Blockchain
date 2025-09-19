import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="Healthcare Blockchain", layout="wide")

st.title("🏥 Healthcare Blockchain Record System")
st.write("This demo simulates a blockchain to store patient health records securely.")

# Form for adding records
st.header("➕ Add New Health Record")
with st.form("record_form"):
    patient_id = st.text_input("Patient ID")
    record_type = st.text_input("Record Type (e.g., Blood Test, Prescription)")
    details = st.text_area("Details")
    submitted = st.form_submit_button("Submit Record")

if submitted:
    if patient_id and record_type and details:
        response = requests.post(f"{API_URL}/records/new", json={
            "patient_id": patient_id,
            "record_type": record_type,
            "details": details
        })
        if response.status_code == 201:
            st.success(response.json()['message'])
        else:
            st.error("Error adding record")
    else:
        st.warning("Please fill all fields.")

# Mine new block
if st.button("⛏️ Mine Block"):
    response = requests.get(f"{API_URL}/mine")
    if response.status_code == 200:
        block = response.json()
        st.success(f"Block {block['index']} mined successfully!")
        st.json(block)
    else:
        st.error("Mining failed")

# Show blockchain
st.header("📜 Blockchain Records")
if st.button("🔄 Refresh Blockchain"):
    response = requests.get(f"{API_URL}/chain")
    if response.status_code == 200:
        chain = response.json()["chain"]
        st.write(f"Blockchain Length: {response.json()['length']}")
        for block in chain:
            with st.expander(f"Block {block['index']} (Prev: {block['previous_hash'][:10]}...)"):
                st.json(block)
