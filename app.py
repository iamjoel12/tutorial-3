from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]
# Create a get request for all devices

@app.get("/devices")
async def get_devices():
    return readings

# Create a get request to return the hottest reading

@app.get("/hottest")
def get_hottest_reading():
    if not readings:
        raise HTTPException(status_code=404, detail="No readings available")
    
    hottest_reading = max(readings, key=lambda x: x["temp"])
    return hottest_reading

#create a get request to return the average temperature of all readings

@app.get("/average")
def get_average_temperature():
    if not readings:
        raise HTTPException(status_code=404, detail="No readings available")
    
    average_temp = sum(reading["temp"] for reading in readings) / len(readings)
    return {"average_temperature": average_temp}

