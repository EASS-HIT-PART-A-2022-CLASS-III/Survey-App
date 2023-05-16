import QuestionForm from './QuestionForm';
import VoteForm from './VoteForm';

import { useState } from 'react';

function QuestionList({ questions, onQuestionUpdate }) {
  return (
    <div className="question-list">
      {questions.map(question => (
        <div key={question.id} className="question">
          <h2 className="question-text">{question.id+1}. {question.text}</h2>
          <VoteForm question={question} onVote={onQuestionUpdate} questionId={question.id} />
        </div>
      ))}
    </div>
  );
}

export default QuestionList;
