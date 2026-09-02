const boxes = document.getElementsByClassName("object");

let pos = getComputedStyle(boxes[0]).left;

const player = document.getElementById("player");
const player_size = parseInt(getComputedStyle(player).width);

const distance_moved = 10;
let x = 100;
let y = 500;
// Movenemt
// Forward
document.addEventListener("keydown", function (event) {
  if (event.key === "w" || event.key === "W") {
    let closest_y = null;

    for (let i = 0; i < boxes.length; i++) {
      const box_x = parseInt(getComputedStyle(boxes[i]).top);
      const box_y = parseInt(getComputedStyle(boxes[i]).left);

      if (box_y < y && box_x == x) {
        if (closest_y === null || box_y > closest_y) {
          closest_y = box_y;
        }
      }
    }

    console.log("Current Y:", y);
    console.log("Closest object in direction:", closest_y);
    y = closest_y + player_size;
    console.log("Y:", y);
  }
  // Left
  if (event.key === "a" || event.key === "A") {
    let closest_x = null;

    for (let i = 0; i < boxes.length; i++) {
      const box_x = parseInt(getComputedStyle(boxes[i]).left);
      const box_y = parseInt(getComputedStyle(boxes[i]).top);

      if (box_x < x && box_y == y) {
        if (closest_x === null || box_x > closest_x) {
          closest_x = box_x;
        }
      }
    }

    console.log("Current X:", x);
    console.log("Closest object in direction:", closest_x);
    x = closest_x + player_size;
    console.log("X:", x);
  }
  // Back
  if (event.key === "s" || event.key === "S") {
    let closest_y = null;

    for (let i = 0; i < boxes.length; i++) {
      const box_x = parseInt(getComputedStyle(boxes[i]).left);
      const box_y = parseInt(getComputedStyle(boxes[i]).top);

      if (box_y > y && box_x == x) {
        if (closest_y === null || box_y < closest_y) {
          closest_y = box_y;
        }
      }
    }
    console.log("Current Y:", y);
    console.log("Closest object in direction:", closest_y);
    y = closest_y - player_size;
    console.log("Y:", y);
  }
  if (event.key === "d" || event.key === "D") {
    x += distance_moved;
    console.log("Right");
  }

  player.style.left = `${x}px`;
  player.style.top = `${y}px`;
});
