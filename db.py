from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

debug_collection = db["debug_history"]
autofix_collection = db["autofix_history"]
generate_collection = db["generate_history"]
