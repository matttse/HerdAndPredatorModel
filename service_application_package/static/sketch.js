var preysAmount = $("#numberOfGenerations").val();
var theGrassAmount = 70;
var watersAmount = 70;
var poisonsAmount = 50;

var spawnBorder = 40;

var drawPerception=true;

var mutationRate = 0.05;
var preys = [];
var foods = [];
var maxMult = 5;
var maxPerc = 200;

var maxspeed = 3.5;
var maxTurnForce = 0.15;

function setup() {
	createCanvas(windowWidth,windowHeight);
	
	addPreys(preysAmount);
	resetResources();
}

function draw() {
	background(51);

	drawInfo();

	updatePreys();
	drawPreys();

	drawFoods();
	drawPoisons();
	drawWaters();

	resupplyResources();

	populate();
}

function mousePressed() { drawPerception = !drawPerception; }
function keyPressed() { if (keyCode===32) { noLoop(); } }

function drawInfo() {
	var preysAlive = countAlive();
	fill(0, 102, 153);
	textSize(32);
	text(preysAlive, 10, 40);
	text(floor(frameRate()), width-50, 40);

	var w = width/preysAlive;
	var h = 15;
	var ii=0;
	for(var i=0; i<preys.length; i++) {
		var v = preys[i];
		if (v.dead==false) {
			var health = map(v.health, 0, 1, 0, w);
			var thirst = map(v.thirst, 0, 1, 0, w);

			fill(0,255,0, 50); 	rect(ii*w, (height-3*h), w*0.95, h);
			fill(0,255,0); 		rect(ii*w, (height-3*h), health*0.95, h);
			fill(0,0,255, 50);	rect(ii*w, (height-1.5*h), w*0.95, h);
			fill(0,0,255);	rect(ii*w, (height-1.5*h), thirst*0.95, h);
			ii++;
		}
		
	}
}