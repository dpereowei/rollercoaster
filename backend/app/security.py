import os
from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def verify_api_key(x_api_key: str = Header(...)):
    """
    Purpose: Verify API key in Header
    """
    if not x_api_key:
        return {"status": 400, "message": "Missing API key"}
    
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return True
# end def