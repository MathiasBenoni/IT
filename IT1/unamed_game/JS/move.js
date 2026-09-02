const player = document.getElementById("player");

let x = 100;
let y = 100;

document.addEventListener("keydown", function (event) {
  if (event.key === "w" || event.key === "W") {
    y -= 10;
    console.log("Forward");
  }
  if (event.key === "a" || event.key === "A") {
    x -= 10;
    console.log("Left");
  }
  if (event.key === "s" || event.key === "S") {
    y += 10;
    console.log("Back");
  }
  if (event.key === "d" || event.key === "D") {
    x += 10;
    console.log("Right");
  }

  player.style.left = `${x}px`;
  player.style.top = `${y}px`;
});
