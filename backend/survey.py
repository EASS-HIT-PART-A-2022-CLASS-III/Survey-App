from typing import List
from pydantic import BaseModel
from fastapi import HTTPException


class Question(BaseModel):
    text: str
    choices: List[str]
    vote_counts: List[int] = None


class Vote(BaseModel):
    question_id: int
    choice: int


class Survey:
    def __init__(self):
        self.questions = []

    def add_question(self, question: Question):
        question.vote_counts = [0] * len(question.choices)
        self.questions.append(question)

    def get_questions(self):
        return self.questions

    def add_vote(self, vote: Vote):
        if vote.question_id < 0 or vote.question_id >= len(self.questions):
            raise HTTPException(status_code=404, detail="Question not found")
        question = self.questions[vote.question_id]
        if vote.choice < 0 or vote.choice >= len(question.choices):
            raise HTTPException(status_code=400, detail="Invalid choice")
        question.vote_counts[vote.choice] += 1
