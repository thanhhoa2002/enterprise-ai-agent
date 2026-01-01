from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "Enterprise AI Agent"
    
settings = Settings()