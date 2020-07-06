import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random

cred = credentials.Certificate("/Users/arnavshah/Documents/ParkSmart/firebase-sdk.json")
data = {"pir1": {"id": 1, "location": "43.7131°N, 79.3671°W", "state": 0}}

firebase_admin.initialize_app(
    cred, {"databaseURL": "https://smart-parking-db-d2fba.firebaseio.com/"}
)

ref = db.reference("/")
ref.set(data)

current_pir_state = 0
previous_pir_state = 0


def update_firebase():
    global current_pir_state
    global previous_pir_state
    current_pir_state = random.choice([0, 1])  # PIR input
    if current_pir_state != previous_pir_state:
        ref.child("pir1").update({"state": current_pir_state})
    previous_pir_state = current_pir_state


def retrieve_data():
    # TODO: get firebase values
    return ref.get()
