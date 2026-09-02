const boxes = document.getElementsByClassName("object");

let pos = getComputedStyle(boxes[0]).left;

const player = document.getElementById("player");
const player_size = parseInt(getComputedStyle(player).width);

const distance_moved = 10;
let x = 100;
let y = 500;
// Movenemt
document.addEventListener("keydown", function (event) {
  if (event.key === "w" || event.key === "W") {
    let closest_y = null;

    for (let i = 0; i < boxes.length; i++) {
      const box_x = parseInt(getComputedStyle(boxes[i]).top);
      const box_y = parseInt(getComputedStyle(boxes[i]).left);

      if (box_y < y) {
        if (closest_y === null || box_y > closest_y) {
          closest_y = box_y;
        }
      }
    }

    console.log("Forward");
    console.log("Current Y:", y);
    console.log("Closest object in direction:", closest_y);
    y = closest_y + player_size;
    console.log(y);
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
