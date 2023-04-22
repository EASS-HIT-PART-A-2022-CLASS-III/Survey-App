# Survey App
A simple survey app built with FastAPI and docker.

### Installation 
To run SurveyApp, you need to have Docker installed on your machine. Clone this repository and navigate to the project directory.

Build the Docker image:
`docker build -t surveyapp .`
Run the Docker container:
`docker run -p 8000:8000 surveyapp`
Visit http://localhost:8000 in your web browser to view the SurveyApp.

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
    
