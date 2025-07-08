from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import List, Optional
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import os
from dotenv import load_dotenv
from app.schemas import SensorData  # You already have this

from pydantic import BaseModel, Field

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

app = FastAPI(
    title="Sensor Monitoring API",
    description="API to monitor environmental sensor data and alerts.",
    version="1.0.0",
)

# New output schema with string id
class SensorDataOut(BaseModel):
    id: str = Field(..., alias="_id")
    sensor_id: Optional[str]
    type: Optional[str]
    value: Optional[float]
    timestamp: Optional[datetime]

# Helper function to convert document to Pydantic model
def sensor_doc_to_model(doc) -> SensorDataOut:
    doc["_id"] = str(doc["_id"])
    return SensorDataOut(**doc)

@app.get("/")
async def root():
    return {"message": "Hello from Sensor API!"}

@app.get("/measurements", response_model=List[SensorDataOut])
async def get_measurements(limit: int = 10):
    try:
        docs = await collection.find().sort("timestamp", -1).to_list(length=limit)
        return [sensor_doc_to_model(doc) for doc in docs]
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.post("/sensors/batch")
async def add_sensor_data(data: List[SensorData]):
    docs = [d.dict() for d in data]
    await collection.insert_many(docs)
    return {"status": "success", "inserted": len(docs)}

@app.get("/sensors/latest", response_model=List[SensorDataOut])
async def get_latest_data():
    pipeline = [
        {"$sort": {"timestamp": -1}},
        {"$group": {"_id": "$sensor_id", "doc": {"$first": "$$ROOT"}}},
        {"$replaceRoot": {"newRoot": "$doc"}}
    ]
    docs = await collection.aggregate(pipeline).to_list(length=None)
    return [sensor_doc_to_model(doc) for doc in docs]

@app.get("/sensors/history", response_model=List[SensorDataOut])
async def get_history(
    sensor_type: Optional[str] = None,
    start: Optional[datetime] = None,
    end: Optional[datetime] = None
):
    query = {}
    if sensor_type:
        query["type"] = sensor_type
    if start and end:
        query["timestamp"] = {"$gte": start, "$lte": end}
    docs = await collection.find(query).to_list(length=1000)
    return [sensor_doc_to_model(doc) for doc in docs]

@app.get("/sensors/alerts", response_model=List[SensorDataOut])
async def get_alerts():
    thresholds = {
        "temperature": 35.0,
        "humidity": 80.0,
        "smoke": 50.0
    }
    query = {
        "$or": [
            {"type": "temperature", "value": {"$gt": thresholds["temperature"]}},
            {"type": "humidity", "value": {"$gt": thresholds["humidity"]}},
            {"type": "smoke", "value": {"$gt": thresholds["smoke"]}}
        ]
    }
    docs = await collection.find(query).to_list(length=500)
    return [sensor_doc_to_model(doc) for doc in docs]

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "An unexpected error occurred."})
