var preysAmount = $("#numberOfGenerations").val();
var numberOfGenerations = $("#numberOfGenerations").val();
var theGrassAmount = 70;
var watersAmount = 70;
var poisonsAmount = 50;

var spawnBorder = 40;

var drawPerception=true;

var mutationRate = 0.05;

var predators = [];
var maxMult = 5;
var maxPerc = 200;

var maxspeed = 3.5;
var maxTurnForce = 0.15;
var generationCounter = 0;
function setup() {
	createCanvas(windowWidth,windowHeight);
	
	addPreys(preysAmount);
	resetResources();
}

function draw() {
	background(51);

	drawInfo();
	generationCounter++;
	if (generationCounter == numberOfGenerations) {
		updatePreys();
		drawPreys();
		console.log(preys);
		drawGrasses();
		drawPoisons();
		drawWaters();

		resupplyResources();

		populate();
	}
	
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



function populate() {
	var tickets = [];
	if (countAlive()<=0) {
		
		var oldPreyPopulation = preys.slice(0);
		preys = [];

		for(var i=0; i<oldPreyPopulation.length; i++) {
			var v=oldPreyPopulation[i];
			for (var j=0; j<(v.fitness); j++) { tickets.push(i); }
		}
		console.log(tickets.length);
		
		for(var i=0; i<preysAmount; i++) {
			var v = addPreys();
			console.log(v);
			if (random()>mutationRate) { v.dna.grassMult = randomParent().dna.grassMult; }
			if (random()>mutationRate) { v.dna.grassPerc = randomParent().dna.grassPerc; }
			if (random()>mutationRate) { v.dna.poisonMult = randomParent().dna.poisonMult; }
			if (random()>mutationRate) { v.dna.poisonPerc = randomParent().dna.poisonPerc; }
			if (random()>mutationRate) { v.dna.waterMult = randomParent().dna.waterMult; }
			if (random()>mutationRate) { v.dna.waterPerc = randomParent().dna.waterPerc; }
			v.limit();
		}
		resetResources();
	}
	function randomParent() {
		var j = tickets[floor(random(tickets.length))]
		return oldPreyPopulation[j];
	}
}


function limit(x, limit) {
	if (x>limit) { x=limit;	}
}

function resetResources() {
	theGrass = []; poisons = []; waters = [];
	addGrasses(theGrassAmount);
	addPoisons(poisonsAmount);
	addWaters(watersAmount);
}

function resupplyResources() {
	if (theGrass.length<theGrassAmount) { addGrasses(theGrassAmount-theGrass.length); }
	if (poisons.length<poisonsAmount) { addPoisons(poisonsAmount-poisons.length); }
	if (waters.length<watersAmount) { addWaters(watersAmount-waters.length); }
}

