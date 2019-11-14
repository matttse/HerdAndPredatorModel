var preysAmount = 15;
var numberOfGenerations = $("#numberOfGenerations").val();

var grassAmount = 3;
var watersAmount = 3;
var poisonsAmount = 1;

var spawnBorder = 40;

var drawPerception=true;
var count = 0;
var mutationRate = 0.5;

var generationCounter = 0;
function setup() {
	createCanvas(windowWidth,windowHeight);
	population = new populate();	
	addPreys(preysAmount);
	resetResources();
}

function draw() {
	background(51);
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

	// for (var i = numberOfGenerations - 1; i >= 0; i--) {

		// addPreys(preysAmount);
		// resetResources();
		updatePreys();//controls movement
		drawPreys();	
		drawGrasses();
		drawPoisons();
		// resupplyResources();
		population.run();
		// population.eval();
		// population.natSelection();
	// }

	
}

function mousePressed() { drawPerception = !drawPerception; }
function keyPressed() { if (keyCode===32) { noLoop(); } }


function populate() {
	this.matingPool = [];
	var tickets = [];
	this.eval = function() {
		var maximumFitness = 0;

		for (var r = 0; r < preysAmount; r++) {
			tickets[r].getFitness()
			if (tickets[r].fitness > 0) {
				maximumFitness = tickets[i].fitness
			}
		}

		for (var r = 0; r < preysAmount; r++) {
			if (maximumFitness != 0) {
				this.pres[r].fitness /= maximumFitness;
			}
		}

		for (var r = 0; r < preysAmount; r++) {
			if (tickets[r].fitness > 0) {
				var n = tickets[r].fitness = 100//normalization
				for (var s = 0; s < n; s++) {
					this.matingPool.push(tickets[r]);//add favorable genes to matingPool
				}
			}
		}
	}
	this.run = function() {
		
		if (countAlive()<=0) {
			
			var oldPopulation = preys.slice(0);
			preys = [];

			for(var i=0; i<oldPopulation.length; i++) {
				var v=oldPopulation[i];
				for (var j=0; j<(v.fitness); j++) { tickets.push(i); }
			}
			console.log(tickets.length);
			
			for(var i=0; i<preysAmount; i++) {
				var v = addPrey();
				if (random()>mutationRate) { v.dna.foodMult = randomParent().dna.foodMult; }
				if (random()>mutationRate) { v.dna.foodPerc = randomParent().dna.foodPerc; }
				if (random()>mutationRate) { v.dna.poisonMult = randomParent().dna.poisonMult; }
				if (random()>mutationRate) { v.dna.poisonPerc = randomParent().dna.poisonPerc; }
				v.limit();
			}
			resetResources();
		}
		function randomParent() {
			var j = tickets[floor(random(tickets.length))]
			return oldPopulation[j];
		}
	}
	this.natSelection = function() {
		
		var babyPrey = [];
		for (var i = 0; i < tickets.length; i++) {
			var parentOne = random(matingPool).dna;//allowed via p5 library, picks random index for us given array
			var parentTwo = random(matingPool).dna;//does not account for the parents being the same**
			var child = parentOne.mating(parentTwo);//lets make a baby/child
			child.mutation();//adds in variability
			babyPrey[i] = new Prey(child);//new prey is born
		}
		tickets = babyPrey;//we have a new generation set
	}
}


function limit(x, limit) {
	if (x>limit) { x=limit;	}
}

function resetResources() {
	grass = []; poisons = []; waters = [];
	addGrasses(grassAmount);
	addPoisons(poisonsAmount);
	addWaters(watersAmount);
}

function resupplyResources() {
	if (grass.length<grassAmount) { addGrasses(grassAmount-grass.length); }
	if (poisons.length<poisonsAmount) { addPoisons(poisonsAmount-poisons.length); }
	if (waters.length<watersAmount) { addWaters(watersAmount-waters.length); }
}

