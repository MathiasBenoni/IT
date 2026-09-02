const boxes = document.getElementsByClassName("object");

let pos = getComputedStyle(boxes[0]).left;
console.log(pos);
