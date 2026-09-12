# Import libraries
from dotenv import load_dotenv
import os   
import certifi 
import requests 

# Load dotenv 
load_dotenv() 

# If there is path issue with SSL
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# Aviation api key 
AVIATION_API_KEY = os.getenv("AVIATION_API_KEY")

# Default origin International Air Transport Association
DEFAULT_ORIGIN_IATA = os.getenv("DEFAULT_ORIGIN_IATA","DEL")


# Create a function for search flights 
def search_flights(query:str): 
    try:
        url = "http://api.aviationstack.com/v1/flights"

        params = {
            "access_key": AVIATION_API_KEY,
            "limit": 5
        }

        # get response 
        response = requests.get(url=url, params=params)

        # store in json 
        data = response.json()

        # create final response list 
        flights = []

        if "data" in data: 
            for flight in data["data"][:5]:
                airline = flight.get("airline",{}).get("name","Unknown")
                departure = flight.get("departure",{}).get("airport","Unknown")
                arrival = flight.get("arrival",{}).get("airport","Unknown")
                status = flight.get("departure",{}).get("flight_status","Unknown")

                flights.append(f"""
                Airline:{airline}
                Departure: {departure})
                Arrival: {arrival})
                Status: {status}""")

        return "\n".join(flights)
    except Exception as e: 
        return {e}

if __name__ == "__main__":
    print(search_flights("7 days Japan trip from India"))
    print("\n" + "=" * 80 + "\n")