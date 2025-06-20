import os
from pymongo import MongoClient
from datetime import datetime

client = MongoClient(os.getenv("MONGODB_URI"))
db = client.get_database("medical_chatbot")

class MedicineOrder:
    collection = db["medicine_orders"]

    @staticmethod
    def create_order(data):
        order = {
            "medicines": data["medicines"],
            "patient_name": data["patient_name"],
            "address": data["address"],
            "created_at": datetime.utcnow(),
        }
        result = MedicineOrder.collection.insert_one(order)
        return str(result.inserted_id)