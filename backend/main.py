from fastapi import FastAPI, HTTPException
from survey import Survey, Question, Vote
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# Allow requests from http://localhost:3000
origins = [
    "http://localhost:3000",
]

# Add the CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
survey = Survey()


@app.post("/questions")
async def create_question(question: Question):
    if len(question.choices) < 2:
        raise HTTPException(status_code=400, detail="Question must have at least two choices")
    survey.add_question(question)
    question_id = len(survey.questions) - 1
    return {"message": f"Question {question_id} created successfully"}


@app.get("/questions")
async def get_questions():
    try:
        questions = survey.get_questions()
        return {"questions": [{"id": i, **q.dict()} for i, q in enumerate(questions)]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/votes")
async def create_vote(vote: Vote):
    try:
        survey.add_vote(vote)
        return {"message": "Vote cast successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
