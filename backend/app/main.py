from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import Base, engine
from app.routers.interaction_router import router as interaction_router
from app.routers.ai_router import router as ai_router

# Create FastAPI app FIRST
app = FastAPI(title="HCP AI CRM")

# Then add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(interaction_router)
app.include_router(ai_router)

@app.get("/")
def home():
    return {"message": "HCP AI CRM Backend Running"}