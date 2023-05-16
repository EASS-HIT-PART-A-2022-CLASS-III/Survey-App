import { useState, useEffect } from 'react';
import useFetch from './useFetch';
import QuestionList from './components/QuestionList';
import Navbar from './components/Navbar';

import QuestionForm from './components/QuestionForm';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  const [questions, setQuestions] = useState([]);
  

  const { data, isPending, error } = useFetch('http://localhost:8000/questions');

  const handleQuestionSubmit = (question) => {
    setQuestions([...questions, question]);
  }

  const handleQuestionUpdate = (updatedQuestion) => {
    const index = questions.findIndex(q => q.id === updatedQuestion.id);
    const newQuestions = [...questions];
    newQuestions[index] = updatedQuestion;
    setQuestions(newQuestions);
  }

  useEffect(() => {
    if (data) {
      setQuestions(data.questions);
    }
  }, [data]);

  return (
    <BrowserRouter>
      <div>
        <Navbar />
        <div className="container">
          <Routes>
            <Route path="/" element={<QuestionList questions={questions} onQuestionUpdate={handleQuestionUpdate} />} />
            <Route path="/add" element={<QuestionForm onQuestionSubmit={handleQuestionSubmit} />} />
          </Routes>
        </div>
        {error && <div>{error}</div>}
        {isPending && <div>Loading...</div>}
      </div>
    </BrowserRouter>
  );
}

export default App;
