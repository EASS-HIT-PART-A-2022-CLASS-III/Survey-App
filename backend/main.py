from fastapi import FastAPI, HTTPException
from survey import Survey, Question, Vote
from fastapi.middleware.cors import CORSMiddleware
import requests
app = FastAPI()
# Allow requests from http://localhost:3000
origins = [
    "http://localhost:3000",
    "http://localhost:8080",

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


def log_message(message: str):
    try:
        response = requests.post('http://logging:8080/log', json={'message': message})
        # This will raise an exception for 4xx and 5xx status codes
        print(response.raise_for_status())
        print(message)  # Print the received log message
    except requests.exceptions.RequestException as e:
        print(f"Failed to log message. Error: {e}")
        print(message)  # Print the message anyway



@app.post("/questions")
async def create_question(question: Question):
    if len(question.choices) < 2:
        raise HTTPException(status_code=400, detail="Question must have at least two choices")
    survey.add_question(question)
    question_id = len(survey.questions) - 1
    log_message(f"Question {question_id} created successfully")
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
        log_message(f"Vote cast successfully")
        return {"message": "Vote cast successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
