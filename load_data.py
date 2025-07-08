import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

df = pd.read_json("data/sample_data.json")
data_dict = df.to_dict("records")

batch_size = 1000
for i in range(0, len(data_dict), batch_size):
    batch = data_dict[i:i+batch_size]
    collection.insert_many(batch)

print("Data imported successfully!")
