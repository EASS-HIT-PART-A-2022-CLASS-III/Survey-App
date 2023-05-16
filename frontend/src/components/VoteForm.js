import { useState, useEffect } from 'react';
import axios from 'axios';

function VoteForm({ question, onVote }) {
  const [choice, setChoice] = useState('');
  const [showResults, setShowResults] = useState(false);
  const [hasVoted, setHasVoted] = useState(false);

  useEffect(() => {
    // Check if the user has already voted
    const userHasVoted = localStorage.getItem(question.id) !== null;
    setHasVoted(userHasVoted);

    // If the user has already voted, show the results by default
    if (userHasVoted) {
      setShowResults(true);
    }
  }, [question.id]);

  const handleChoiceChange = (event) => {
    setChoice(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (question.id === undefined) {
        alert('Question not found!');
        return;
      }

    // Check if the user has already voted
    if (localStorage.getItem(question.id) !== null) {
      alert('You have already voted!');
      return;
    }

    const data = {
      question_id: question.id,
      choice,
    };
    axios.post('http://localhost:8000/votes', data)
      .then(response => {
        const updatedQuestion = response.data;
        onVote(updatedQuestion);

        // Mark the question as voted by the current user
        localStorage.setItem(question.id, 'true');

        // Show the results
        setHasVoted(true);
        setShowResults(true);
      })
      .catch(error => {
        alert(error.message);
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          {question.choices.map((choiceOption, index) => (
            <div key={index}>
              <label>
                <input type="radio" name="choice" value={index} checked={choice === String(index)} onChange={handleChoiceChange} required disabled={hasVoted} />
                {choiceOption}
              </label>
            </div>
          ))}
        </div>
        <button type="submit" disabled={hasVoted}>Vote</button>
      </form>
      {showResults && (
        <div>
          <h3>Results:</h3>
          <ul>
            {question.choices.map((choiceOption, index) => (
              <li key={index}>{choiceOption}: {question.vote_counts[index]}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default VoteForm;
