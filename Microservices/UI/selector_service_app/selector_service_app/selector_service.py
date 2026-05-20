from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load JSON
with open("data.json") as f:
    data = json.load(f)

@app.get("/sources")
def get_sources():
    return list(data["sources"].keys())

@app.get("/interfaces/{source}")
def get_interfaces(source: str):
    return data["sources"][source]["interface"]

@app.get("/resolutions/{source}")
def get_resolutions(source: str):
    return data["sources"][source]["resolution"]

@app.get("/serializers/{source}")
def get_serializers(source: str):
    return list(data["sources"][source]["serializers"].keys())

@app.get("/deserializers/{source}/{serializer}")
def get_deserializers(source: str, serializer: str):
    return data["sources"][source]["serializers"][serializer]

@app.get("/sink/{source}")
def get_sink(source: str):
    return data["sources"][source]["sink"]
