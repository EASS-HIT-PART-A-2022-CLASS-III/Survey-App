import React, { useState } from "react";
import './Question.css';

function QuestionForm() {
  const [text, setText] = useState('');
  const [choices, setChoices] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();

    if (text.trim() === '') {
      alert('Please enter a question text.');
      return;
    }

    if (choices.some(choice => choice.trim() === '')) {
      alert('Please enter a choice text for all choices.');
      return;
    }

    const data = { text, choices };
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    };

    fetch('http://localhost:8000/questions', requestOptions)
      .then(response => response.json())
      .then(data => {
        alert(data.message);
        setText('');
        setChoices([]);
      })
      .catch(error => {
        alert(error.message);
      });
  }

  const handleAddChoice = (event) => {
    event.preventDefault();

    setChoices([...choices, '']);
  }

  const handleChoiceChange = (event, index) => {
    const newChoices = [...choices];
    newChoices[index] = event.target.value;
    setChoices(newChoices);
  }

  return (
    <form className="question-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <label className="form-label">Question Text:</label>
        <input className="form-input" type="text" value={text} onChange={(event) => setText(event.target.value)} />
      </div>
      <div className="form-group">
        <label className="form-label">Choices:</label>
        {choices.map((choice, index) => (
          <div key={index} className="choice-group">
            <input className="choice-input" type="text" value={choice} onChange={(event) => handleChoiceChange(event, index)} />
          </div>
        ))}
        <button className="add-choice-btn" onClick={handleAddChoice}>Add Choice</button>
      </div>
      <button className="submit-btn" type="submit">Create Question</button>
    </form>
  );
}

export default QuestionForm;
