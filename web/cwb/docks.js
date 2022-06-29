var state = {width: 0, height: 0, saved: null};
var text = {top: null, mid: null, bid: null, bottom: null};
function getCanvasCtx(){
    let c = document.querySelector("#docks");
    let ctx = /** @type {CanvasRenderingContext2D} */ c.getContext("2d");
    state.height = c.height;
    state.width = c.width;
    return ctx;
}

function clearHere(start_x, start_y, width, height) {
    // https://stackoverflow.com/questions/2142535/how-to-clear-the-canvas-for-redrawing
    let ctx = getCanvasCtx();
    ctx.clearRect(start_x,start_y,width,height);
}

function clear() {
    clearHere(0,0,state.width,state.height)
}

function addTopText(){
    let input = document.querySelector("#toptext");
    addText(input.value, 50, 50);
}

function addMidText(){
    let input = document.querySelector("#midtext");
    addText(input.value, 50, 200);
}

function addBidText(){
    let input = document.querySelector("#bidtext");
    addText(input.value, 50, 350);
}
function addBottomText(){
    let input = document.querySelector("#bottomtext");
    addText(input.value, 50, 500);
}

function addText(text, start_x, start_y) {
    let ctx = getCanvasCtx();
    // can't put it at 0,0
    // LOOKS awful by default
    // could use fill text 
    ctx.strokeStyle = "black"
    ctx.fillStyle = "white"
    // 36 pt vs 3 px
    ctx.font = "36pt Impact"
    //ctx.strokeText(text, start_x, start_y);
    // TODO how to do both
    ctx.fillText(text, start_x, start_y);
}

// Clear the canvas and add the image
function addImage(image_src) {
    var ctx = /** @type {CanvasRenderingContext2D} */ getCanvasCtx();
    clear();
    var image = new Image();
    image.onload = function() {
        console.log("loaded image");
        ctx.drawImage(image, 0, 0, state.width, state.height)
        //var savedImage = c.toDataUrl();
        //window.open(savedImage)

    }

    image.src = image_src;
}

function testAddImage() {
    addImage("gb_template.jpg")
}

// Upload a new meme image to use
function upload(){
    var img = document.querySelector("#meme");
    var file = null;
    if(img.files != null && img.files.length == 1)
    {
        file = img.files[0].name;
    }
    if(file != null) {
        console.log(file);
        addImage(file);
    }
}

// default siliiness
function docks(){
    let ctx = /** @type {CanvasRenderingContext2D} */ getCanvasCtx();
    // 50,50 150, 150
    ctx.strokeRect(50,50, 100, 100)
    // 75,75 125, 125, 125, 75
    // absolute instead of relative
    // TODO: what does beginpath do
    //ctx.beginPath();
    ctx.moveTo(75,75)
    ctx.lineTo(125,75)
    ctx.lineTo(125,125)
    ctx.lineTo(75,75)
    ctx.fill()

    addText("LOLLOLOLOL", 50, 50);
    
}
window.onload = docks;