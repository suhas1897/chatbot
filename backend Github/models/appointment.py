import os
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

client = MongoClient(os.getenv("MONGODB_URI"))
db = client.get_database("medical_chatbot")

class Appointment:
    collection = db["appointments"]

    @staticmethod
    def create_appointment(data):
        appointment = {
            "patient_name": data["patient_name"],
            "date": data["date"],
            "time": data["time"],
            "address": data["address"],
            "created_at": datetime.utcnow(),
        }
        result = Appointment.collection.insert_one(appointment)
        return str(result.inserted_id)