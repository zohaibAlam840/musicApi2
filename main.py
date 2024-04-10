import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


from models import RecommendationScheme, Music
from music_recommender import MusicRecommender

app = FastAPI()

# Allow all origins in this example, but you can customize it based on your needs
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/recommend')
async def recommend(value: RecommendationScheme):
    recommender = MusicRecommender(value)
    recommendations: list[Music] = recommender()
    return {"recommendations": recommendations}


@app.get('/')
async def main(request: Request):
    return {"status": True}


if __name__ == "__main__":
    uvicorn.run(app)