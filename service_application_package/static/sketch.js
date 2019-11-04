var preysAmount = $("#numberOfGenerations").val();
var numberOfGenerations = $("#numberOfGenerations").val();

var theGrassAmount = 70;
var watersAmount = 70;
var poisonsAmount = 50;

var spawnBorder = 40;

var drawPerception=true;


var predators = [];

var generationCounter = 0;
function setup() {
	createCanvas(windowWidth,windowHeight);
	population = new populate();
	addPreys(preysAmount);
	resetResources();
}

function draw() {
	background(51);

	drawInfo();
	population.run();

	generationCounter++;
	if (generationCounter == numberOfGenerations) {
		population.eval();
		population.natSelection();
		// updatePreys();
		// drawPreys();
		// console.log(preys);
		// drawGrasses();
		// drawPoisons();
		// drawWaters();

		// resupplyResources();
		// populate();
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
	
	this.matingPool = [];

	if (countAlive()<=0) {
		
		var oldPreyPopulation = preys.slice(0);
		
		//populate prey
		for(var i=0; i<oldPreyPopulation.length; i++) {
			var v=oldPreyPopulation[i];
			for (var j=0; j<(v.fitness); j++) { tickets.push(i); }
		}
		console.log(tickets.length);
		this.eval = function() {
			var maximumFitness = 0;

			for (var r = 0; r < this.preysAmount; r++) {
				this.preys[r].getFitness()
				if (this.preys[r].fitness > 0) {
					maximumFitness = this.preys[i].fitness
				}
			}

			for (var r = 0; r < this.preysAmount; r++) {
				if (maximumFitness != 0) {
					this.pres[r].fitness /= maximumFitness;
				}
			}

			for (var r = 0; r < this.preysAmount; r++) {
				if (this.preys[r].fitness > 0) {
					var n = this.preys[r].fitness = 100//normalization
					for (var s = 0; s < n; s++) {
						this.matingPool.push(this.preys[r]);//add favorable genes to matingPool
					}
				}
			}
		}
		// for(var i=0; i<preysAmount; i++) {
		// 	var v = addPreys();
		// 	console.log(v);
		// 	if (random()>mutationRate) { v.dna.grassMult = randomParent().dna.grassMult; }
		// 	if (random()>mutationRate) { v.dna.grassPerc = randomParent().dna.grassPerc; }
		// 	if (random()>mutationRate) { v.dna.poisonMult = randomParent().dna.poisonMult; }
		// 	if (random()>mutationRate) { v.dna.poisonPerc = randomParent().dna.poisonPerc; }
		// 	if (random()>mutationRate) { v.dna.waterMult = randomParent().dna.waterMult; }
		// 	if (random()>mutationRate) { v.dna.waterPerc = randomParent().dna.waterPerc; }
		// 	v.limit();
		// }
		resetResources();
		generationCounter++;
	}

	this.run = function() {
		updatePreys();
		drawPreys();
		console.log(generationCounter);
		drawGrasses();
		drawPoisons();
		drawWaters();

		resupplyResources();
	}
	this.natSelection = function() {
		var babyPrey = [];
		for (var i = 0; i < this.preys.length; i++) {
			var parentOne = random(this.matingPool).dna;//allowed via p5 library, picks random index for us given array
			var parentTwo = random(this.matingPool).dna;//does not account for the parents being the same**
			var child = parentOne.mating(parentTwo);//lets make a baby/child
			child.mutation();//adds in variability
			babyPrey[i] = new Prey(child);//new prey is born
		}
		this.preys = babyPrey;//we have a new generation set
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

