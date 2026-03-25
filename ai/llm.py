from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
import os

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
 
def ask_ai(prompt):
    response = model.invoke(prompt)
    return response.content
