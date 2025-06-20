from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
from models.appointment import Appointment
from models.medicine_order import MedicineOrder
from llm import generate_response
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    context: Optional[Dict] = {}

class ChatResponse(BaseModel):
    response: str
    context: Dict

available_slots = ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"]

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    message = request.message.strip()
    context = request.context or {}
    response_text = ""
    
    logger.info(f"Received message: {message}, Context: {context}")

    try:
        if context.get("action") == "book_appointment":
            logger.info(f"Processing book_appointment step: {context.get('step')}")
            if context.get("step") == "name":
                if not message:
                    response_text = "Please provide a valid name for the appointment."
                    return ChatResponse(response=response_text, context=context)
                context["patient_name"] = message
                context["step"] = "date"
                response_text = "Please specify the date for your appointment (e.g., 2025-07-01)."
                return ChatResponse(response=response_text, context=context)
            elif context.get("step") == "date":
                try:
                    datetime.fromisoformat(message)
                    context["date"] = message
                    context["step"] = "time"
                    response_text = f"Please choose a time slot: {', '.join(available_slots)}."
                    return ChatResponse(response=response_text, context=context)
                except ValueError:
                    response_text = "Invalid date format. Please use YYYY-MM-DD (e.g., 2025-07-01)."
                    return ChatResponse(response=response_text, context=context)
            elif context.get("step") == "time":
                if message in available_slots:
                    context["time"] = message
                    context["step"] = "address"
                    response_text = "Please provide your address for the appointment confirmation."
                    return ChatResponse(response=response_text, context=context)
                else:
                    response_text = f"Invalid time slot. Please choose from: {', '.join(available_slots)}."
                    return ChatResponse(response=response_text, context=context)
            elif context.get("step") == "address":
                if not message:
                    response_text = "Please provide a valid address."
                    return ChatResponse(response=response_text, context=context)
                context["address"] = message
                appointment_data = {
                    "patient_name": context["patient_name"],
                    "date": context["date"],
                    "time": context["time"],
                    "address": context["address"],
                }
                appointment_id = Appointment.create_appointment(appointment_data)
                response_text = (
                    f"Appointment booked for {context['patient_name']} on {context['date']} "
                    f"at {context['time']}. Confirmation sent to {context['address']}."
                )
                logger.info(f"Appointment created: {appointment_id}")
                return ChatResponse(response=response_text, context={})

        elif context.get("action") == "order_medicine":
            logger.info(f"Processing order_medicine step: {context.get('step')}")
            if context.get("step") == "medicines":
                try:
                    medicines = []
                    for item in message.split(","):
                        parts = item.strip().split()
                        if len(parts) != 2 or not parts[1].isdigit():
                            raise ValueError("Invalid format")
                        medicines.append({"name": parts[0], "quantity": int(parts[1])})
                    context["medicines"] = medicines
                    context["step"] = "name"
                    response_text = "Please provide your name for the order."
                    return ChatResponse(response=response_text, context=context)
                except ValueError:
                    response_text = (
                        "Please list medicines and quantities as a comma-separated list "
                        "(e.g., 'Paracetamol 10, Ibuprofen 5')."
                    )
                    return ChatResponse(response=response_text, context=context)
            elif context.get("step") == "name":
                if not message:
                    response_text = "Please provide a valid name for the order."
                    return ChatResponse(response=response_text, context=context)
                context["patient_name"] = message
                context["step"] = "address"
                response_text = "Please provide your delivery address."
                return ChatResponse(response=response_text, context=context)
            elif context.get("step") == "address":
                if not message:
                    response_text = "Please provide a valid address."
                    return ChatResponse(response=response_text, context=context)
                context["address"] = message
                order_data = {
                    "medicines": context["medicines"],
                    "patient_name": context["patient_name"],
                    "address": context["address"],
                }
                order_id = MedicineOrder.create_order(order_data)
                medicines_str = ", ".join([f"{m['name']} x{m['quantity']}" for m in context["medicines"]])
                response_text = (
                    f"Medicine order placed for {context['patient_name']}. "
                    f"Medicines: {medicines_str}. Will be delivered to {context['address']}."
                )
                logger.info(f"Medicine order created: {order_id}")
                return ChatResponse(response=response_text, context={})

        # Handle general queries and action triggers
        llm_response = generate_response(message, context)
        response_text = llm_response

        if "book appointment" in message.lower():
            response_text = "Please provide your name to start booking an appointment."
            context = {"action": "book_appointment", "step": "name"}
        elif "order medicine" in message.lower() or "buy medicine" in message.lower():
            response_text = (
                "Please list the medicines and quantities you need as a comma-separated list "
                "(e.g., 'Paracetamol 10, Ibuprofen 5')."
            )
            context = {"action": "order_medicine", "step": "medicines"}
        else:
            context = {}

        logger.info(f"Sending response: {response_text}, Context: {context}")
        return ChatResponse(response=response_text, context=context)

    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")