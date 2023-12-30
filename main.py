from typing import List,Dict,Optional
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentiment import sentiment_analysis
origins = ["*"]
class Review(BaseModel):
    review: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/get_sentiment")
def sentiment(review:Review):
    return {"sentiment":sentiment_analysis.get_ten_var(review.review),"positive":sentiment_analysis.get_sentiment(review.review)}
