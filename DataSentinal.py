"""
Data Sentinel API with Firebase Integration
This version verifies user identity using Firebase ID tokens.
Useful for integration with React Native apps using Firebase Authentication.
"""

# Step 1: Create a Flask web application
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, auth
import os
import requests
import json
from difflib import get_close_matches

app = Flask(__name__)

cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "firebase_credentials.json")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

def verify_firebase_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        return None

def is_request_suspicious(request_data):
    def load_knowledge_base(file_path: str) -> dict:
        with open (file_path,"r") as file:
            data: dict = json.load(file)
            return data

    def save_kwoledge_base(file_path:str,data:dict):
        with open(file_path,"w") as file:
            json.dump(data,file,indent=2)


    def find_best_match(client_call:str,question:list[str]) -> str|None:
        # Cut off is the accurecy:0.6 is the best
        matches:list = get_close_matches(client_call,question,n=1,cutoff=0.6)
        return matches[0] if matches else None

    def get_answer_for_question(Client_Call:str,knowledge_base:dict) -> str|None:
        for q in knowledge_base["questions"]:
            if q["Client_Call"] == Client_Call:
                return bool(q["answer"])
        return None

   
    knowledge_base:dict = load_knowledge_base("knowledge_base.json")

    best_match:str|None = find_best_match(request_data,[q["question"] for q in knowledge_base["questions"]])

    if best_match:
        answer:str = get_answer_for_question(best_match,knowledge_base)
        return bool(answer)
    else:
       return False

@app.route("/validate", methods=["POST"])
def validate_client_call():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Missing Authorization header"}), 401

    token = auth_header.replace("Bearer ", "")
    user = verify_firebase_token(token)
    if not user:
        return jsonify({"error": "Invalid or expired token"}), 401

    data = request.json

    if is_request_suspicious(data):
        return jsonify({"status": "blocked", "reason": "Suspicious request detected"}), 403

    firebase_url = "https://firestore.googleapis.com/v1/projects/gamecode-5c399/databases/(default)/documents/users"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    try:
        firebase_response = requests.post(firebase_url, headers=headers, json=data)
        return jsonify(firebase_response.json()), firebase_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "running"})

if __name__ == "__main__":
    app.run(debug=True)