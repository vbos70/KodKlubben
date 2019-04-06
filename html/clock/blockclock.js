
// Read parameters (defined in html <script> tag)
var width = document.currentScript.getAttribute("data-width");
var height = document.currentScript.getAttribute("data-height"); 
var canvas = document.getElementById(
    document.currentScript.getAttribute("canvas-id"));

// get a drawing context
var ctx = canvas.getContext("2d");

// refresh the clock every second (1000 milliseconds)
setInterval(drawClock, 1000);

function drawBlocks(curTime, x, y, bw, bh, numx, numy, color1, color2, bgcolor) {
    var tick;
    var grd;
    for (tick = 0; tick < (numx*numy); tick++) {
	cy = y + bh * Math.floor(tick / numx);
	cx = x + bw * (tick % numx);
	grd = ctx.createLinearGradient(cx, cy, cx+bw, cy+bh);
	grd.addColorStop(0, color1);
	grd.addColorStop(1, color2);
	if ( tick < curTime ) {
	    ctx.fillStyle = grd;
	} else {
	    ctx.fillStyle = bgcolor;
	}
	ctx.fillRect(cx, cy, bw, bh);
    }

    ctx.font = "120px Verdana";
    ctx.fillStyle = bgcolor;
    ctx.fillText(curTime.toString(), x+(numx * bw), y+(height / 4));
}

function drawClock() {

    var now = new Date();
    var second = now.getSeconds();
    var minute = now.getMinutes();
    var hour = now.getHours();
    var x = 0;
    var y = 0;
    var w = width * (3 / 4);
    var h = height / 3;
    var cols = 6;
    var rows = 4;
    var bw = w / cols;
    var bh = h / rows;

    // remove the previous blocks
    ctx.clearRect(0, 0, width, height);

    // draw the hour blocks on top 1/3rd of the area
    drawBlocks(hour, x, y, bw, bh, cols, rows, "white", "blue", "#4444AA");

    // draw the minute blocks in the middle 1/3rd of the area
    x = 0;
    y = height / 3;
    
    cols = 12;    // 12 blocks per row
    rows = 5;     // 5 rows
    bw = w / cols;
    bh = h / rows;
    drawBlocks(minute, x, y, bw, bh, cols, rows, "white", "red", "#AA4444");    

    // draw the seconds on the lower 1/3rd of the area.
    // using only the right half
    x = w / 2;
    y = 2 * y; // now, y == 2/3 * height

    w = width * (3 / 4) / 2; // use only half of the area width
    cols = 6;      // 6 blocks per row.
    rows = 10;     // 10 rows
    bw = w / cols;
    bh = h / rows;
    
    drawBlocks(second, x, y, bw, bh, cols, rows, "white", "green", "#44AA44");    
}

