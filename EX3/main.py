from fastapi import FastAPI 
from transformers import pipeline, set_seed
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI() 
generator = pipeline('text-generation', model='openai-gpt')
set_seed(42)

@app.get("/") 
async def root(): 
    return {"message": "Hello World, input your messege."}

@app.post("/generate/") 
def generate_text(item: Item): 
    return generator(item.text, max_length=20, num_return_sequences=5)
