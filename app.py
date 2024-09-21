from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from custom_tools import ( 
                           get_all_products, 
                           get_product_by_id, 
                           get_products_by_category, 
                           get_products_by_price_range, 
                           get_products_by_stock
                         )

app = FastAPI()

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class ChatInput(BaseModel):
    query: str

list_of_tools = [
    get_all_products,
    get_product_by_id,
    get_products_by_category,
    get_products_by_price_range,
    get_products_by_stock
]

llm = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    tools=list_of_tools
)

chat = llm.start_chat(enable_automatic_function_calling=True)

@app.post("/chat/")
async def chat_bot(input_data: ChatInput):
    query = input_data.query
    response = chat.send_message(query)
    return {"Response": response.text}
