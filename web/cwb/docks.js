var state = {width: 0, height: 0, ctx: null, image: null, startx: null, starty: null};
var text = {top: null, mid: null, bid: null, bottom: null};
function getCanvasCtx(){
    if (state.ctx == null) {
        let c = document.querySelector("#docks");
        // setting this on the html element doesn't seem to work 
        // 1. can you provide the event as an arg
        // 2. can you set it in html without the ()? doesn't seem to work for the button
        c.addEventListener('click', canvasClick);
        let ctx = /** @type {CanvasRenderingContext2D} */ c.getContext("2d");
        state.height = c.height;
        state.width = c.width;
        state.ctx = ctx;
    }

    return state.ctx;
}

function canvasClick(event) {
    state.startx = event.pageX;
    state.starty = event.pageY;
    let input = document.querySelector("#toptext");
    input.focus();
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

function clearWrite() {
    state.startx = null;
    state.starty = null;
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
    if (state.startx != null) {
        start_x = state.startx;
        start_y = state.starty;
    }
    ctx.fillText(text, start_x, start_y);
    ctx.strokeText(text, start_x, start_y);
}

function saveImage() { 
    var ctx = /** @type {CanvasRenderingContext2D} */ getCanvasCtx();
    var savedImage = c.toDataUrl();
    window.open(savedImage)
}

function reset() {
    if(state.image != null){
        state.ctx.drawImage(state.image, 0, 0, state.width, state.height);
    }
}

// Clear the canvas and add the image
function addImage(image_src) {
    var ctx = /** @type {CanvasRenderingContext2D} */ getCanvasCtx();
    clear();
    var image = new Image();
    image.onload = function() {
        console.log("loaded image");
        ctx.drawImage(image, 0, 0, state.width, state.height);
        state.image = image;
        // saveImage()
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
    // what does beginpath do?
    // Answer: allows you to close the path after to make sure nothing else affects things
    ctx.beginPath();
    ctx.moveTo(75,75)
    ctx.lineTo(125,75)
    ctx.lineTo(125,125)
    ctx.closePath()
    ctx.fill()

    addText("LOLLOLOLOL", 50, 50);
}

window.onload = docks;
