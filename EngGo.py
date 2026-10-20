<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EngGo - Aprende inglés</title>

<style>
:root {
  --green: #58cc02;
  --dark: #348000;
  --light: #e9f8d9;
  --text: #263238;
  --muted: #687782;
  --border: #dce5e9;
  --red: #e34b4b;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f5f9fc;
  color: var(--text);
}

header {
  background: white;
  border-bottom: 2px solid var(--border);
  padding: 20px;
  text-align: center;
}

header h1 {
  color: var(--dark);
  margin: 0;
  font-size: 32px;
}

header p {
  margin: 6px 0 0;
  color: var(--muted);
}

.container {
  max-width: 850px;
  margin: 24px auto;
  padding: 0 16px;
}

.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.stat {
  background: white;
  border: 2px solid var(--border);
  border-radius: 14px;
  padding: 12px 5px;
  text-align: center;
  font-weight: bold;
}

.stat span {
  display: block;
  font-size: 20px;
  margin-bottom: 5px;
}

.section-title { margin: 24px 0 12px; }

.levels {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.level-btn {
  border: 2px solid var(--border);
  background: white;
  color: var(--text);
  border-radius: 12px;
  padding: 14px 8px;
  min-height: 85px;
  cursor: pointer;
  font-size: 14px;
  font-weight: bold;
}

.level-btn.unlocked { border-color: var(--green); }
.level-btn.active { background: var(--light); border-color: var(--dark); }
.level-btn:disabled { opacity: .5; cursor: not-allowed; }
.level-btn small { display: block; margin-top: 7px; }

.game-card {
  background: white;
  border: 2px solid var(--border);
  border-radius: 18px;
  padding: 24px;
  margin-top: 22px;
}

.game-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  margin-bottom: 15px;
}

.tag {
  background: var(--light);
  color: var(--dark);
  padding: 7px 10px;
  border-radius: 8px;
  font-weight: bold;
}

.progress-track {
  width: 100%;
  height: 12px;
  background: #e7edf0;
  border-radius: 20px;
  overflow: hidden;
  margin-bottom: 24px;
}

.progress-fill {
  height: 100%;
  width: 0;
  background: var(--green);
  transition: width .25s;
}

#question {
  font-size: 24px;
  line-height: 1.4;
}

#translation { color: var(--muted); }

.options { display: grid; gap: 10px; }

.option {
  background: white;
  border: 2px solid var(--border);
  border-radius: 12px;
  padding: 14px;
  text-align: left;
  font-size: 16px;
  cursor: pointer;
}

.option:hover:not(:disabled) {
  background: #f2faeb;
  border-color: var(--green);
}

.option:disabled { cursor: default; }
.option.correct { border-color: var(--green); background: var(--light); }
.option.wrong { border-color: var(--red); background: #fff0f0; }

#feedback {
  display: none;
  margin-top: 16px;
  padding: 14px;
  border-radius: 10px;
  line-height: 1.5;
}

#feedback.good { display: block; background: var(--light); color: var(--dark); }
#feedback.bad { display: block; background: #fff0f0; color: #9c2222; }

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 20px;
}

.main-btn, .secondary-btn {
  border: none;
  border-radius: 12px;
  padding: 13px 18px;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
}

.main-btn { background: var(--green); color: white; flex: 1; }
.main-btn:hover:not(:disabled) { background: var(--dark); }
.main-btn:disabled { opacity: .45; cursor: not-allowed; }
.secondary-btn { background: #edf1f4; color: var(--text); }

#result { display: none; text-align: center; padding: 24px 10px; }
#result h2 { font-size: 28px; }
#result p { line-height: 1.6; }

.badges { display: flex; flex-wrap: wrap; gap: 10px; margin: 14px 0 28px; }
.badge { background: white; border: 2px solid var(--border); border-radius: 12px; padding: 12px; }
.badge.earned { background: #fff7d6; border-color: #f0c84b; }

footer { text-align: center; color: var(--muted); padding: 24px; font-size: 13px; }

@media (max-width: 520px) {
  .levels { grid-template-columns: repeat(2, 1fr); }
  .game-card { padding: 16px; }
  #question { font-size: 21px; }
  .stat span { font-size: 16px; }
}
</style>
</head>

<body>
<header>
  <h1>🚀 EngGo</h1>
  <p>¡Aprendé inglés jugando!</p>
</header>

<main class="container">
  <section class="stats">
    <div class="stat">
      <span id="hearts">❤️❤️❤️❤️❤️</span>
      Vidas
      <div id="lifeCount">5 / 5</div>
    </div>
    <div class="stat">
      <span>⭐ <b id="points">0</b></span>
      Puntos
    </div>
    <div class="stat">
      <span>🔥 <b id="streak">0</b></span>
      Racha
    </div>
  </section>

  <h2 class="section-title">📚 Elegí tu nivel</h2>
  <section class="levels" id="levels"></section>

  <section class="game-card">
    <div id="game">
      <div class="game-top">
        <span class="tag" id="levelName">Starter</span>
        <span id="questionNumber">Pregunta 1 de 5</span>
      </div>

      <div class="progress-track">
        <div class="progress-fill" id="progress"></div>
      </div>

      <h2 id="question">Preparando pregunta...</h2>
      <p id="translation">Elegí la respuesta correcta.</p>
      <div class="options" id="options"></div>
      <div id="feedback" aria-live="polite"></div>

      <div class="actions">
        <button class="main-btn" id="continueBtn" disabled>Comprobar respuesta</button>
        <button class="secondary-btn" id="restartBtn">🔄 Reiniciar</button>
      </div>
    </div>

    <div id="result">
      <h2 id="resultTitle">¡Nivel completado!</h2>
      <p id="resultText"></p>
      <div class="badges" id="badges"></div>
      <button class="main-btn" id="replayBtn">Volver a jugar</button>
    </div>
  </section>
</main>

<footer>EngGo · Aprendé inglés a tu ritmo 🌱</footer>

<script>
"use strict";

// Cada pregunta tiene un texto, opciones, respuesta correcta y explicación.
const levels = [
  {
    name: "Starter",
    questions: [
      { q: "What does 'I' mean?", options: ["Yo", "Él", "Ella", "Nosotros"], answer: 0, why: "'I' significa yo." },
      { q: "Complete: I _ happy.", options: ["is", "are", "am", "be"], answer: 2, why: "Con I usamos am." },
      { q: "What does 'book' mean?", options: ["Mesa", "Libro", "Puerta", "Silla"], answer: 1, why: "'Book' significa libro." },
      { q: "Complete: She _ my friend.", options: ["am", "are", "is", "be"], answer: 2, why: "Con she usamos is." },
      { q: "What does 'cat' mean?", options: ["Perro", "Gato", "Pájaro", "Pez"], answer: 1, why: "'Cat' significa gato." }
    ]
  },
  {
    name: "Present Simple",
    questions: [
      { q: "I _ football every day.", options: ["plays", "play", "playing", "played"], answer: 1, why: "Con I usamos play." },
      { q: "She _ to school every morning.", options: ["go", "going", "goes", "gone"], answer: 2, why: "Con she, go cambia a goes." },
      { q: "_ you like pizza?", options: ["Does", "Do", "Are", "Is"], answer: 1, why: "Para preguntas con you usamos do." },
      { q: "He doesn't _ coffee.", options: ["likes", "liked", "like", "liking"], answer: 2, why: "Después de doesn't usamos el verbo base." },
      { q: "They _ English at school.", options: ["studies", "study", "studying", "studied"], answer: 1, why: "Con they usamos study." }
    ]
  },
  {
    name: "Present Continuous",
    questions: [
      { q: "I am _ now.", options: ["study", "studies", "studying", "studied"], answer: 2, why: "Usamos am/is/are + verbo en -ing." },
      { q: "She _ watching TV.", options: ["am", "is", "are", "be"], answer: 1, why: "Con she usamos is." },
      { q: "They are _ football.", options: ["play", "plays", "played", "playing"], answer: 3, why: "Después de are usamos playing." },
      { q: "We _ studying English.", options: ["is", "am", "are", "be"], answer: 2, why: "Con we usamos are." },
      { q: "Choose the correct sentence.", options: ["He are running.", "He is running.", "He am running.", "He running."], answer: 1, why: "La forma correcta es he is running." }
    ]
  },
  {
    name: "Past Simple",
    questions: [
      { q: "Yesterday, I _ football.", options: ["play", "plays", "played", "playing"], answer: 2, why: "El pasado de play es played." },
      { q: "She _ to school yesterday.", options: ["go", "goes", "went", "going"], answer: 2, why: "Went es el pasado de go." },
      { q: "I didn't _ TV yesterday.", options: ["watched", "watch", "watches", "watching"], answer: 1, why: "Después de didn't usamos el verbo base." },
      { q: "They _ a movie last night.", options: ["see", "saw", "seeing", "sees"], answer: 1, why: "Saw es el pasado de see." },
      { q: "_ you play yesterday?", options: ["Do", "Does", "Did", "Are"], answer: 2, why: "Para preguntar en pasado usamos did." }
    ]
  },
  {
    name: "Past Continuous",
    questions: [
      { q: "I _ sleeping at 10 PM.", options: ["was", "were", "am", "are"], answer: 0, why: "Con I usamos was." },
      { q: "They were _ football.", options: ["play", "played", "playing", "plays"], answer: 2, why: "Usamos was/were + verbo en -ing." },
      { q: "She _ reading a book.", options: ["were", "was", "are", "be"], answer: 1, why: "Con she usamos was." },
      { q: "We were _ dinner.", options: ["eat", "ate", "eating", "eats"], answer: 2, why: "Después de were usamos eating." },
      { q: "Choose the correct sentence.", options: ["They was running.", "They were running.", "They is running.", "They running."], answer: 1, why: "Con they usamos were." }
    ]
  },
  {
    name: "Grammar Master",
    questions: [
      { q: "She _ English every day.", options: ["study", "studies", "studying", "studied"], answer: 1, why: "En Present Simple, con she usamos studies." },
      { q: "Look! The dog _ running.", options: ["is", "are", "was", "do"], answer: 0, why: "Para una acción que ocurre ahora usamos is running." },
      { q: "Yesterday, we _ pizza.", options: ["eat", "eats", "ate", "eating"], answer: 2, why: "Ate es el pasado de eat." },
      { q: "At 8 PM, I was _.", options: ["sleep", "slept", "sleeping", "sleeps"], answer: 2, why: "Was + sleeping forma el Past Continuous." },
      { q: "He doesn't _ football.", options: ["plays", "play", "playing", "played"], answer: 1, why: "Después de doesn't usamos el verbo base." }
    ]
  }
];

// Variables que guardan el progreso de la partida.
let currentLevel = 0;
let questionIndex = 0;
let lives = 10; // Diez mitades equivalen a cinco corazones.
let points = 0;
let streak = 0;
let unlockedLevel = 0;
let completed = [];
let answered = false;
let levelCorrect = 0;
let earnedBadges = new Set();
let gameOver = false;

const $ = id => document.getElementById(id);

function renderLevels() {
  const panel = $("levels");
  panel.innerHTML = "";

  levels.forEach((level, index) => {
    const button = document.createElement("button");
    button.className = "level-btn";

    if (index <= unlockedLevel) button.classList.add("unlocked");
    if (index === currentLevel) button.classList.add("active");

    button.disabled = index > unlockedLevel;
    button.innerHTML =
      ${index < completed.length && completed[index] ? "✅" : index <= unlockedLevel ? "🔓" : "🔒"} ${level.name} +
      <small>${index < completed.length && completed[index] ? "Completado" : index <= unlockedLevel ? "Disponible" : "Bloqueado"}</small>;

    button.addEventListener("click", () => {
      if (index <= unlockedLevel && !gameOver) {
        currentLevel = index;
        questionIndex = 0;
        levelCorrect = 0;
        answered = false;
        showGame();
      }
    });

    panel.appendChild(button);
  });
}

function updateStats() {
  const fullHearts = Math.floor(lives / 2);
  const halfHeart = lives % 2 === 1 ? "💔" : "";
  $("hearts").textContent = "❤️".repeat(fullHearts) + halfHeart + "🤍".repeat(5 - Math.ceil(lives / 2));
  $("lifeCount").textContent = (lives / 2).toFixed(1).replace(".0", "") + " / 5";
  $("points").textContent = points;
  $("streak").textContent = streak;
}

function showGame() {
  $("game").style.display = "block";
  $("result").style.display = "none";
  renderLevels();
  updateStats();

  if (lives <= 0) {
    showGameOver();
    return;
  }

  const level = levels[currentLevel];
  const question = level.questions[questionIndex];

  if (!question) {
    finishLevel();
    return;
  }

  answered = false;
  $("levelName").textContent = level.name;
  $("questionNumber").textContent = Pregunta ${questionIndex + 1} de ${level.questions.length};
  $("question").textContent = question.q;
  $("translation").textContent = "Elegí la respuesta correcta.";
  $("progress").style.width = ${questionIndex / level.questions.length * 100}%;
  $("feedback").className = "";
  $("feedback").textContent = "";
  $("continueBtn").textContent = "Comprobar respuesta";
  $("continueBtn").disabled = true;

  const optionsPanel = $("options");
  optionsPanel.innerHTML = "";

  question.options.forEach((option, index) => {
    const button = document.createElement("button");
    button.className = "option";
    button.textContent = ${String.fromCharCode(65 + index)}. ${option};

    button.addEventListener("click", () => selectAnswer(index, button));
    optionsPanel.appendChild(button);
  });
}

function selectAnswer(selected, selectedButton) {
  if (answered || lives <= 0) return;
  answered = true;

  const question = levels[currentLevel].questions[questionIndex];
  const buttons = [...$("options").querySelectorAll("button")];
  buttons.forEach(button => button.disabled = true);
  buttons[question.answer].classList.add("correct");

  const feedback = $("feedback");

  if (selected === question.answer) {
    points += 10;
    streak++;
    levelCorrect++;
    feedback.className = "good";
    feedback.textContent = ¡Correcto! +10 puntos. ${question.why};

    if (streak >= 5) earnedBadges.add("🔥 Racha de 5");
  } else {
    lives = Math.max(0, lives - 1);
    streak = 0;
    selectedButton.classList.add("wrong");
    feedback.className = "bad";
    feedback.textContent = Incorrecto. Perdiste medio corazón. La respuesta correcta era "${question.options[question.answer]}". ${question.why};
  }

  if (points >= 50) earnedBadges.add("⭐ 50 puntos");
  if (lives === 0) earnedBadges.add("💪 ¡Lo intentaste!");

  updateStats();
  $("progress").style.width = ${(questionIndex + 1) / levels[currentLevel].questions.length * 100}%;
  $("continueBtn").disabled = false;
  $("continueBtn").textContent = lives <= 0 ? "Ver resultado" :
    questionIndex === levels[currentLevel].questions.length - 1 ? "Terminar nivel" : "Siguiente pregunta";
}

function continueGame() {
  if (!answered) return;

  if (lives <= 0) {
    showGameOver();
    return;
  }

  questionIndex++;

  if (questionIndex >= levels[currentLevel].questions.length) {
    finishLevel();
  } else {
    showGame();
  }
}

function finishLevel() {
  completed[currentLevel] = true;

  if (levelCorrect === levels[currentLevel].questions.length) {
    earnedBadges.add("🏆 Nivel perfecto: " + levels[currentLevel].name);
  }

  if (currentLevel === unlockedLevel && unlockedLevel < levels.length - 1) {
    unlockedLevel++;
  }

  $("game").style.display = "none";
  $("result").style.display = "block";
  $("resultTitle").textContent = currentLevel === levels.length - 1
    ? "🎉 ¡Terminaste todos los niveles!"
    : "🏆 ¡Nivel completado!";

  $("resultText").textContent =
    `Nivel: ${levels[currentLevel].name}. ` +
    `Respuestas correctas: ${levelCorrect} de ${levels[currentLevel].questions.length}. ` +
    `Puntos totales: ${points}. ` +
    (currentLevel < levels.length - 1
      ? "¡El siguiente nivel está desbloqueado!"
      : "¡Sos un Grammar Master!");

  $("badges").innerHTML = "";
  earnedBadges.forEach(badge => {
    const element = document.createElement("div");
    element.className = "badge earned";
    element.textContent = badge;
    $("badges").appendChild(element);
  });

  $("replayBtn").textContent = currentLevel < levels.length - 1
    ? "Siguiente nivel ➜"
    : "Jugar desde el principio";

  renderLevels();
}

function showGameOver() {
  gameOver = true;
  $("game").style.display = "none";
  $("result").style.display = "block";
  $("resultTitle").textContent = "💪 ¡No te rindas!";
  $("resultText").textContent =
    `Te quedaste sin vidas. Conseguíste ${points} puntos. ` +
    "Podés reiniciar y volver a intentarlo.";
  $("badges").innerHTML = "";
  $("replayBtn").textContent = "🔄 Reiniciar partida";
}

function restartGame() {
  currentLevel = 0;
  questionIndex = 0;
  lives = 10;
  points = 0;
  streak = 0;
  unlockedLevel = 0;
  completed = [];
  levelCorrect = 0;
  answered = false;
  gameOver = false;
  earnedBadges = new Set();
  showGame();
}

$("continueBtn").addEventListener("click", continueGame);
$("restartBtn").addEventListener("click", restartGame);

$("replayBtn").addEventListener("click", () => {
  if (gameOver || currentLevel === levels.length - 1) {
    restartGame();
  } else {
    currentLevel++;
    questionIndex = 0;
    levelCorrect = 0;
    gameOver = false;
    showGame();
  }
});

renderLevels();
showGame();
</script>
</body>
</html>