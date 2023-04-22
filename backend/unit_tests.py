from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_question():
    response = client.post(
        "/questions",
        json={
            "text": "What is your favorite color?",
            "choices": ["Red", "Green", "Blue"]
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Question 0 created successfully"}


def test_create_question_with_less_than_two_choices():
    response = client.post(
        "/questions",
        json={
            "text": "What is your favorite color?",
            "choices": ["Red"]
        }
    )
    assert response.status_code == 400


def test_get_questions():
    response = client.get("/questions")
    assert response.status_code == 200
    assert len(response.json()["questions"]) == 1


def test_add_vote():
    response = client.post(
        "/votes",
        json={
            "question_id": 0,
            "choice": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Vote cast successfully"}


def test_add_vote_with_invalid_question_id():
    response = client.post(
        "/votes",
        json={
            "question_id": 1,
            "choice": 1
        }
    )
    assert response.status_code == 404


def test_add_vote_with_invalid_choice():
    response = client.post(
        "/votes",
        json={
            "question_id": 0,
            "choice": 3
        }
    )
    assert response.status_code == 400
