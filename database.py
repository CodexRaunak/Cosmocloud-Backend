from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
if not MONGO_DB_URL:
    raise ValueError("MongoDB URL is not set in the environment variables.")

client = AsyncIOMotorClient(MONGO_DB_URL)
db = client["Student-Management-System"]  
students_collection = db["students"]