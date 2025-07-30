// This file contains the JavaScript code for client-side functionality.

// Function to handle form submission for the quiz
function submitQuiz() {
    const answers = {};
    const questionElements = document.querySelectorAll('.question');

    questionElements.forEach((questionElement) => {
        const questionId = questionElement.dataset.id;
        const selectedAnswer = questionElement.querySelector('input[type="radio"]:checked');
        if (selectedAnswer) {
            answers[questionId] = selectedAnswer.value;
        }
    });

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answers }),
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => {
        console.error('Error submitting quiz:', error);
    });
}

// Function to display quiz results
function displayResults(data) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    const scoreElement = document.createElement('h2');
    scoreElement.textContent = `Your Score: ${data.score}`;
    resultsContainer.appendChild(scoreElement);

    data.results.forEach(result => {
        const resultElement = document.createElement('div');
        resultElement.textContent = `Question ID: ${result.question_id}, Your Answer: ${result.selected}, Correct Answer: ${result.correct}, Correct: ${result.is_correct}`;
        resultsContainer.appendChild(resultElement);
    });
}

// Event listener for quiz form submission
document.getElementById('quiz-form').addEventListener('submit', function(event) {
    event.preventDefault();
    submitQuiz();
});