from fastapi import FastAPI
from pydantic import BaseModel
from app.model import DummyTopicModel   # <--- absoluter Import

app = FastAPI()
model = DummyTopicModel()

class PostRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_topic(request: PostRequest):
    result = model.predict(request.text)
    return {"predictions": result}
