// Get the canvas from the HTML page/file
var canvas = document.getElementById("my-canvas");

// get a drawing context
var ctx = canvas.getContext("2d");

// draw a rectangular frame 
ctx.beginPath();
ctx.strokeStyle = "blue";
ctx.rect(0, 0, canvas.width, canvas.height);
ctx.stroke();

var message = "Hej allihopa!";

// set the font (Verdana) and font size (20px)
ctx.font = "20px Verdana";

// Set the color
//ctx.fillStyle = "green";

// Set the text justification / alignment
ctx.textAlign = "center";

// print the message at the center of the canvas
ctx.fillText(message, canvas.width / 2, canvas.height / 2);


