let questions = [];
        let currentQuestionIndex = 0;
        let score = 0;
        let timer;
        let answered = false;
        const quesTime = 15;
        const categoryNames = {
            "9": "General Knowledge",
            "21": "Sports",
            "23": "History",
            "18": "Science",
            "11": "Movies",
            "17": "Nature",
            "22": "Geography",
            "24": "Politics",
            "25": "Art",
            "27": "Animals"
        };

        function startQuiz() {
            const category = document.getElementById("categories").value;
            const difficulty = document.getElementById("difficulty-levels").value;
            document.getElementById("selected-category-display").textContent = `Category: ${categoryNames[category]}`;
            document.getElementById("selected-difficulty-display").textContent = `Difficulty: ${difficulty.charAt(0).toUpperCase() + difficulty.slice(1)}`;
            fetch(`https://opentdb.com/api.php?amount=15&category=${category}&difficulty=${difficulty}&type=multiple`)
                .then(response => response.json())
                .then(data => {
                    questions = data.results;
                    document.getElementById("screen1").style.display = "none";
                    document.getElementById("screen2").style.display = "block";
                    showQuestion();
                });
        }

        function showQuestion() {
            if (currentQuestionIndex >= questions.length) {
                endQuiz();
                return;
            }
            answered = false;
            const questionData = questions[currentQuestionIndex];
            document.getElementById("question-num").textContent = `Question ${currentQuestionIndex + 1} / 15`;
            document.getElementById("question").textContent = decodeEntities(questionData.question);
            
            const optionsDiv = document.getElementById("options");
            optionsDiv.innerHTML = "";
            let options = [...questionData.incorrect_answers, questionData.correct_answer];
            options.sort(() => Math.random() - 0.5);
            
            options.forEach(option => {
                const button = document.createElement("button");
                button.textContent = decodeEntities(option);

                button.onclick = () => {
                    if (!answered) {
                        answered = true;
                        checkAnswer(button, option, questionData.correct_answer);
                    }
                };
                optionsDiv.appendChild(button);
            });
            
            startTimer();
        }

        function startTimer() {
            let timeLeft = quesTime;
            document.getElementById("timer").textContent = `Time left: ${timeLeft}s`;
            clearInterval(timer);
            timer = setInterval(() => {
                timeLeft--;
                document.getElementById("timer").textContent = `Time left: ${timeLeft}s`;
                if (timeLeft <= 0) {
                    clearInterval(timer);
                    revealAnswer();
                    setTimeout(nextQuestion, 2000);
                }
            }, 1000);
        }

        function checkAnswer(button, selected, correct) {
            clearInterval(timer);
            if (selected === correct) {
                score++;
                document.getElementById("score").textContent = score;
                button.style.backgroundColor = "green";
                button.textContent += " ✅";
            } else {
                button.style.backgroundColor = "red";
                button.textContent += " ❌";
                revealAnswer();
            }
            setTimeout(nextQuestion, 2000);
        }

        function revealAnswer() {
            document.querySelectorAll("#options button").forEach(btn => {
                if (btn.textContent.includes("✅") || btn.textContent.includes("❌")) return;
                if (btn.textContent.trim() === questions[currentQuestionIndex].correct_answer) {
                    btn.style.backgroundColor = "green";
                    btn.textContent += " ✅";
                }
            });
        }

        function nextQuestion() {
            currentQuestionIndex++;
            showQuestion();
        }

        function endQuiz() {
            document.getElementById("screen2").style.display = "none";
            document.getElementById("screen3").style.display = "block";
            document.getElementById("finalScore").textContent = `${score} / 15`;
        }

        function restartQuiz() {
            location.reload();
        }

        function decodeEntities(encodedString) {
            const textArea = document.createElement("textarea");
            textArea.innerHTML = encodedString;
            return textArea.value;
        }