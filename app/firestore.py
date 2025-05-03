import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

# Use the path to your JSON key from env
cred_path = os.getenv("FIREBASE_CREDENTIALS_JSON")

# Check if the path exists
if not os.path.exists(cred_path):
    raise Exception(f"Credential file not found at {cred_path}")

# Load the JSON and print a key
with open(cred_path, "r") as f:
    cred_data = json.load(f)
    print("Service Account Project ID:", cred_data.get("project_id"))

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()