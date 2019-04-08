// Get the canvas from the HTML page/file
var canvas = document.getElementById("my-canvas");

// get a drawing context
var ctx = canvas.getContext("2d");

// print the time every second (1 second = 1000 milliseconds)
setInterval(printTime, 1000);

function printTime() {

    // clear the canvas to remove old time
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
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


    // draw a green filled rectangle
    ctx.fillStyle = "green";
    ctx.fillRect(canvas.width / 4,
		 canvas.height / 4,
		 canvas.width / 2,
		 canvas.height / 2);

    // change the color for the message
    ctx.fillStyle = "black";    
    // print the message at the center of the canvas
    ctx.fillText(message1, canvas.width / 2, canvas.height / 2);
}
