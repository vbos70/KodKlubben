// Get the canvas from the HTML page/file
var canvas = document.getElementById("my-canvas");

// get a drawing context
var ctx = canvas.getContext("2d");

// draw a rectangular frame 
ctx.beginPath();
ctx.strokeStyle = "blue";
ctx.rect(0, 0, canvas.width, canvas.height);
ctx.stroke();

// Get the current time (and date)
var now = new Date();

// set the font (Verdana) and font size (20px)
ctx.font = "20px Verdana";

// Set the color
//ctx.fillStyle = "green";

// Set the text justification / alignment
ctx.textAlign = "center";

var hour = now.getHours();
var min = now.getMinutes();

// make the message
var message1 = hour.toString() + ":" + min.toString();

// print the message at the center of the canvas
ctx.fillText(message1, canvas.width / 2, canvas.height / 2);

var message2 = ''
// add leading 0 before hours if needed
if ( hour<10 ) {
    message2 = '0';
}
// add hours
message2 = message2 + hour.toString();

// add ':' to separate hours from minutes.
message2 = message2 + ':'

// add leading 0 before minutes if needed.
if (min<10) {
    message2 = message2 + '0';
}
// add minutes
message2 = message2 + min.toString();



// print the message at the center of the canvas
ctx.fillText(message2, canvas.width / 2, canvas.height * 3 / 4);
