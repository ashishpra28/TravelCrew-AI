# Import libraries
from dotenv import load_dotenv
import os   
import certifi 
import requests 

# Load dotenv 
load_dotenv() 

# Aviation api key 
AVIATION_API_KEY = os.getenv("AVIATION_API_KEY")

# Default origin International Air Transport Association
DEFAULT_ORIGIN_IATA = os.getenv("DEFAULT_ORIGIN_IATA","DEL")



