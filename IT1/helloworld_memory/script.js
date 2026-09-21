const grid_x = 5;
const grid_y = 2;

const TARGET_LETTERS = ["H", "e", "l", "l", "o", "w", "o", "r", "l", "d"];

let solution;
let next_index = 0;
let busy = false;

function create_element(n) {
  let box = document.createElement("div");
  box.className = "box";
  box.id = n;
  box.addEventListener("click", click);
  document.getElementById("board").appendChild(box);
}

function create_board() {
  for (let k = 0; k < grid_x * grid_y; k++) {
    create_element(k);
  }
  document.getElementById("board").style.gridTemplateColumns =
    `repeat(${grid_x}, var(--size))`;
}

function scramble_content(the_list) {
  return [...the_list].sort(() => Math.random() - 0.5);
}

function click(box_clicked) {
  if (busy) {
    return;
  }

  const box = box_clicked.target;
  if (box.classList.contains("solved")) {
    return;
  }

  const letter = solution[box.id];
  box.innerHTML = `<h1>${letter}</h1>`;

  if (letter === TARGET_LETTERS[next_index]) {
    box.classList.add("solved");
    if (next_index === 5) {
      document.getElementById("found_word").innerHTML += " ";
    }
    document.getElementById("found_word").innerHTML += letter;
    next_index++;

    if (next_index === TARGET_LETTERS.length) {
      win();
    }
  } else {
    busy = true;
    setTimeout(() => {
      box.innerHTML = "";
      busy = false;
    }, 700);
  }
}

function win() {
  document.getElementById("win_message").style.display = "block";
  document.getElementById("restart_button").style.display = "";
}

function reset_game() {
  document.getElementById("win_message").style.display = "none";
  document.getElementById("restart_button").style.display = "none";
  document.getElementById("found_word").innerHTML = "";
  next_index = 0;
  busy = false;
  document.getElementById("board").innerHTML = "";
  update_game();
}

document.getElementById("restart_button").addEventListener("click", reset_game);

function update_game() {
  solution = scramble_content(TARGET_LETTERS);
  create_board();
}

update_game();
