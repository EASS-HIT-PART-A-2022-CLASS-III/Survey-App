# Survey App

A simple survey app built with FastAPI,React and Docker.
https://github.com/EASS-HIT-PART-A-2022-CLASS-III/Survey-App/assets/67056261/032ebbe5-fa00-4170-a63a-34504f47b9c0.mp4
### Installation




To run SurveyApp, you need to have Docker installed on your machine. Clone this repository and navigate to the project directory.

# if you want runnig all in One command:

navigate to the root directory

`docker-compose up --build .`

# Backend side:

Build the Docker image:
navigate to the Backend directory

`docker build -t Backend .`

Run the Docker container:

`docker run -it -p 8000:8000 Backend`

Visit http://localhost:8000 in your web browser to view the SurveyApp on Backend side .

### Usage

Once the app is running, you can create survey questions using the following endpoint:
POST /questions

    Request body:
    {
      "text": "What is your favorite color?",
      "choices": ["Red", "Blue", "Green"]
    }

You can retrieve a list of all survey questions using the following endpoint:
`GET /questions
`

To vote on a survey question, use the following endpoint:

    POST /votes

    Request body:
    {
      "question_id": 0,
      "choice": 1
    }

### To run the app locally for development

    pip install -r requirements.txt
    uvicorn main:app --reload

# Frontend side:

Build the Docker image:
navigate to the Frontend directory

`docker build -t frontend .`

Run the Docker container:

`docker run -it 3000:3000 frontend`

Visit http://localhost:3000 in your web browser to view the Survey App on the frontend side.

# logging microservice side:

Build the Docker image:
navigate to the logging-microservice directory

`docker build -t logging-microservice .`

Run the Docker container:

`docker run -it 8080:8080 logging-microservice`

### Usage

You can get a list of all logging using the following endpoint:
`GET /log`
