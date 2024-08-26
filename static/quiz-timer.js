document.addEventListener('DOMContentLoaded', function() {
    const timerDisplay = document.getElementById('time');
    const quizForm = document.getElementById('quizForm');
    const submitButton = quizForm.querySelector('button[type="submit"]');

    const quizDuration = 10 * 60; // 10 minutes in seconds
    let timeLeft;
    let timerInterval;

    function initializeTimer() {
        const storedEndTime = localStorage.getItem('quizEndTime');
        const now = Math.floor(Date.now() / 1000); // Current time in seconds

        if (storedEndTime) {
            timeLeft = Math.max(0, storedEndTime - now);
            if (timeLeft === 0) {
                submitQuiz();
                return;
            }
        } else {
            timeLeft = quizDuration;
            localStorage.setItem('quizEndTime', now + quizDuration);
        }

        updateTimerDisplay();
        startTimer();
    }

    function startTimer() {
        timerInterval = setInterval(function() {
            timeLeft--;
            updateTimerDisplay();

            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                submitQuiz();
            }
        }, 1000);
    }

    function updateTimerDisplay() {
        const minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;
        seconds = seconds < 10 ? '0' + seconds : seconds;
        timerDisplay.textContent = `${minutes}:${seconds}`;
    }

    function submitQuiz() {
        localStorage.removeItem('quizEndTime');
        submitButton.click();
    }

    quizForm.addEventListener('submit', function() {
        clearInterval(timerInterval);
        localStorage.removeItem('quizEndTime');
    });

    initializeTimer();
});