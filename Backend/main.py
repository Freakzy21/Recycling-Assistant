#imports FASTAPI Framework
from fastapi import FastAPI

#creates instance of the FastAPI app (Holds Endpoints)
app = FastAPI()

#Ensures the backend is running (Root endpoint)
@app.get("/")
def home():
    return {"message": "Backend running"}


#data recieved from flutterflow (Scan endpoint)
@app.post("/scan")
async def scan():
    #Data generated from openAI Vision API

    return {"object": "Plastic water bottle",
            "material": "PET #1",
            "recommendation": "recycle",
            "confidence": "98%",
            "instruction": "Empty the bottle and put in recycle bin"
            }