import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("../bocaue-app-firebase-adminsdk-fbsvc-be95cf3ad5.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def create_post(content):
    db.collection('posts').add({'content': content})

def send_message(content):
    db.collection('messages').add({'content': content})