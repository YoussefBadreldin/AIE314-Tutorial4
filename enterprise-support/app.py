from fastapi import FastAPI
from main import EnterpriseSupportSystem

app = FastAPI()
support_system = EnterpriseSupportSystem()

@app.post("/support")
async def handle_support_request(query: str):
    return support_system.handle_query(query)