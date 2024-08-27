from fastapi import FastAPI 
from pydantic import BaseModel
import uvicorn
from transformers import pipeline


app = FastAPI()

class Body(BaseModel):
    text: str

# get, post, put, and delete

@app.get("/") 
def welcome():
    return {"message": "Welcome to  AI Application"}

@app.get("/home") 
def welcome():
    return {"message": "Welcome to  AI Application"}

@app.post("/textclassify")
def classify(prompt: Body):
    classifier = pipeline('text-classification')
    output = classifier(prompt.text)
    return {"class": output[0]['label']}


@app.post("/generate")
def generation(prompt: Body):
    generator =  pipeline('text-generation', model = 'gpt2', max_length=200)
    output = generator(prompt.text)
    return output[0]['generated_text']



if __name__ == "__main__":
    
    uvicorn.run(app,host="0.0.0.0",port=80)