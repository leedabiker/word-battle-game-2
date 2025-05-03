from firebase_admin import credentials, firestore, initialize_app
import json, pathlib, os

cred = credentials.Certificate("creds/wordbattle-game-poc-firebase-adminsdk-fbsvc-82886dde08.json")
initialize_app(cred, {"projectId": "wordbattle-game-poc"})
db = firestore.client()

print("Trying to write …")
db.collection("debug").document("ping").set({"ok": True})
print("✅  write succeeded")