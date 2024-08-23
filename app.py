from fastapi import FastAPI 
from pydantic import BaseModel
import uvicorn



app = FastAPI()

class Body(BaseModel):
    text: str

# get, post, put, and delete

@app.get("/") 
def welcome():
    return {"message": "Welcome to  AI Application"}

@app.get("/home") 
def welcome():
    return {"message": "welcome home"}

if __name__ == "__main__":
    print("HELLO")
    uvicorn.run(app,host="0.0.0.0",port=80)