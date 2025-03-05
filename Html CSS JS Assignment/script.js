let currentScore = 0;  // variable for storing current score
let savedScores = [0, 0];  //list for storing saved scores of players
let currentPlayer = 0;  //variable for storing current player's scores.


//this is the function for rolling the dice
function rollingDice() {
    let diceEle = document.getElementById("dice");
    let diceVoice = document.getElementById("diceVoice");
    diceVoice.play();
    diceEle.classList.add("rolling");
    setTimeout(() => {
        let diceRolling = Math.floor(Math.random() * 6) + 1;
        diceEle.textContent = "🎲 " + diceRolling;
        diceEle.classList.remove("rolling");

        if (diceRolling === 1) {
            currentScore = 0;
            switchingTurn();
        } else {
            currentScore += diceRolling;
        }
        document.getElementById("currentScore").textContent = currentScore;
    }, 500);
}


//this is the function for saving the score in the saved score of the players.
function savingScore() {
    savedScores[currentPlayer] += currentScore;
    document.getElementById(`savedScore${currentPlayer + 1}`).textContent = savedScores[currentPlayer];
    currentScore = 0;
    document.getElementById("currentScore").textContent = currentScore;

    if (savedScores[currentPlayer] >= 100) {
        document.getElementById("winner").textContent = document.getElementById(`player${currentPlayer + 1}`).value + " Wins!";
        return;
    }
    switchingTurn();
}


//function for switching the turns of players.
function switchingTurn() {
    currentPlayer = currentPlayer === 0 ? 1 : 0;
}

//function for resetting the game.
function reset() {
    currentScore = 0;
    savedScores = [0, 0];
    currentPlayer = 0;
    document.getElementById("currentScore").textContent = 0;
    document.getElementById("savedScore1").textContent = 0;
    document.getElementById("savedScore2").textContent = 0;
    document.getElementById("winner").textContent = "";
    document.getElementById("dice").textContent = "🎲";
}