const former = [
  "square",
  "triangle",
  "arrow",
  "circle",
  "cross",
  "heart",
  "hexagon",
  "pentagon",
  "rombus",
  "star",
];
let left_button = document.getElementById("L");
let right_button = document.getElementById("R");
let display = document.querySelector(".display");
let current = 0;

function update_alt() {
  photo.alt = former[current];
}

function show_photo() {
  //photo.src = former[current];
  photo.src = `media/${former[current]}.png`;
  update_alt();
}

function left() {
  if (current <= 0) {
    current = former.length - 1;
  }
  current--;
  show_photo();
}
function right() {
  if (current >= former.length) {
    current = 0;
  }
  current++;
  show_photo();
}
