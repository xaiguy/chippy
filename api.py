from typing import List
from pydantic import BaseModel

import uvicorn
from fastapi import FastAPI

from transformers import GPTNeoXForCausalLM, AutoTokenizer

import argparse

parser = argparse.ArgumentParser(description='FastAPI for testing the chip_1.4B_instruct_alpha model.')
parser.add_argument('--host', type=str, default="127.0.0.1", help='Host IP address')
parser.add_argument('--port', type=int, default=8000, help='Host port')

class Data(BaseModel):
    input_prompt: str

# Creating an instance of the app
app = FastAPI(title="Fast Chippy", description="FastAPI for testing the chip_1.4B_instruct_alpha model.")

model = GPTNeoXForCausalLM.from_pretrained(
    "Rallio67/chip_1.4B_instruct_alpha",
    device_map="auto", 
    #load_in_8bit=True
)

tokenizer = AutoTokenizer.from_pretrained(
    "Rallio67/chip_1.4B_instruct_alpha"
)

@app.get('/health')
async def service_health():
    """Return service health"""
    return {
        "ok"
    }

@app.post('/predict')
async def model_predict(data: Data):
    inputs = tokenizer("User: " + data.input_prompt, return_tensors="pt").to("cuda")
    tokens = model.generate(**inputs, 
                            top_p=0.95,
                            temperature=0.5,
                            top_k=4, 
                            repetition_penalty=1.03,
                            max_length=100,
                            early_stopping=True
    )

    output = tokenizer.decode(tokens[0])
    return output.replace("<|endoftext|>", "")

if __name__ == '__main__':
    args = parser.parse_args()
    uvicorn.run(app, host=args.host,port=args.port)