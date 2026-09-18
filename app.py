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

@app.get("/devices/hottest")
def get_hottest_reading():
    if not readings:
        raise HTTPException(status_code=404, detail="No readings available")
    
    hottest_reading = max(readings, key=lambda x: x["temp"])
    return hottest_reading

# Create a get request to return the average temperature of all readings

@app.get("/average")
def get_average_temperature():
    if not readings:
        raise HTTPException(status_code=404, detail="No readings available")
    
    average_temp = sum(reading["temp"] for reading in readings) / len(readings)
    return {"average_temperature": average_temp}

# Create a get request to return all online devices

@app.get("/devices/online")
def get_online_devices():
    online_devices = [reading for reading in readings if reading["online"]]
    return online_devices

# Create a get request to return a named device

@app.get("/devices/{name}")
def get_device_by_name(name: str):
    device = next((reading for reading in readings if reading["name"] == name), None)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

# Create a get request to return the average temperature of all devices

@app.get("/stats")
def get_average_temperature_of_devices():
    if not readings:
        raise HTTPException(status_code=404, detail="No readings available")
    
    average_temp = sum(reading["temp"] for reading in readings) / len(readings)
    return {"average_temperature": average_temp}

# Create a post request to add a new device with status 201

@app.post("/devices", status_code=201)
def add_device(device: dict):
    if not all(key in device for key in ("name", "room", "temp", "online")):
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    readings.append(device)
    return device

