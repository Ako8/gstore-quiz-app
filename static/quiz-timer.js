document.addEventListener('DOMContentLoaded', function() {
    const timerDisplay = document.getElementById('time');
    const quizForm = document.getElementById('quizForm');
    const submitButton = quizForm.querySelector('button[type="submit"]');

    let timeLeft = 5 * 60;

    function updateTimer() {
        const minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;
        seconds = seconds < 10 ? '0' + seconds : seconds;
        timerDisplay.textContent = `${minutes}:${seconds}`;

        if (timeLeft === 0) {
            clearInterval(timerInterval);
            submitQuiz();
        } else {
            timeLeft--;
        }
    }

    function submitQuiz() {
        submitButton.click();
    }

    const timerInterval = setInterval(updateTimer, 1000);

    quizForm.addEventListener('submit', function() {
        clearInterval(timerInterval);
    });
});