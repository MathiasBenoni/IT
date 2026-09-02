const player = document.getElementById("player");

const distance_moved = 10;
let x = 100;
let y = 100;

document.addEventListener("keydown", function (event) {
  if (event.key === "w" || event.key === "W") {
    y -= distance_moved;
    console.log("Forward");
  }
  if (event.key === "a" || event.key === "A") {
    x -= distance_moved;
    console.log("Left");
  }
  if (event.key === "s" || event.key === "S") {
    y += distance_moved;
    console.log("Back");
  }
  if (event.key === "d" || event.key === "D") {
    x += distance_moved;
    console.log("Right");
  }

  player.style.left = `${x}px`;
  player.style.top = `${y}px`;
});
