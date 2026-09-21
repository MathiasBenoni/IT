const grid_x = 7;
const grid_y = 2;

const TARGET_WORD = "Hello world";
const UNIQUE_LETTERS = ["H", "e", "l", "o", "w", "r", "d"];

let solution;
let found_letters = new Set();
let counter = 0;
let stored_box_1 = null;
let stored_box_2 = null;
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

function render_found_word() {
  const found_word = document.getElementById("found_word");
  found_word.innerHTML = TARGET_WORD.split("")
    .map((char) => (char === " " || found_letters.has(char) ? char : "_"))
    .join("");
}

function click(box_clicked) {
  if (busy) {
    return;
  }

  const box = box_clicked.currentTarget;
  if (box.classList.contains("solved") || box.id == stored_box_1) {
    return;
  }

  box.innerHTML = `<h1>${solution[box.id]}</h1>`;
  counter++;

  if (counter === 1) {
    stored_box_1 = box.id;
  } else if (counter === 2) {
    stored_box_2 = box.id;
    const box_1 = document.getElementById(stored_box_1);
    const box_2 = document.getElementById(stored_box_2);

    if (solution[stored_box_1] === solution[stored_box_2]) {
      box_1.classList.add("solved");
      box_2.classList.add("solved");
      found_letters.add(solution[stored_box_1]);
      render_found_word();
      counter = 0;
      stored_box_1 = null;
      stored_box_2 = null;

      if (found_letters.size === UNIQUE_LETTERS.length) {
        win();
      }
    } else {
      busy = true;
      setTimeout(() => {
        box_1.innerHTML = "";
        box_2.innerHTML = "";
        counter = 0;
        stored_box_1 = null;
        stored_box_2 = null;
        busy = false;
      }, 700);
    }
  }
}

function win() {
  document.getElementById("win_message").style.display = "block";
  document.getElementById("restart_button").style.display = "";
}

function reset_game() {
  document.getElementById("win_message").style.display = "none";
  document.getElementById("restart_button").style.display = "none";
  found_letters = new Set();
  counter = 0;
  stored_box_1 = null;
  stored_box_2 = null;
  busy = false;
  document.getElementById("board").innerHTML = "";
  update_game();
}

document.getElementById("restart_button").addEventListener("click", reset_game);

function update_game() {
  solution = scramble_content(UNIQUE_LETTERS.flatMap((letter) => [letter, letter]));
  create_board();
  render_found_word();
}

update_game();
