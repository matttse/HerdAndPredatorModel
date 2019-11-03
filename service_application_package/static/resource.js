var poisons = [];

function poisonClass() {
	this.pos = createVector(random(spawnBorder, width-spawnBorder), random(spawnBorder, height-spawnBorder));

	this.draw = function() {
		ellipse(this.pos.x, this.pos.y, 6, 6);
	}
}
function addPoisons(n) { 
	for(var i=0; i<n; i++) {
		poisons.push(new poisonClass());
	}
}
function drawPoisons() {
	fill(255, 50, 50);
	noStroke();
	for(var i=0; i<poisons.length; i++) {
		poisons[i].draw();
	}
}
var waters = [];

function waterClass() {
	this.pos = createVector(random(spawnBorder, width-spawnBorder), random(spawnBorder, height-spawnBorder));

	this.draw = function() {
		ellipse(this.pos.x, this.pos.y, 6, 6);
	}
}
function addWaters(n) { 
	for(var i=0; i<n; i++) {
		addWater();
	}
}
function addWater() {
	var water = new waterClass();
	waters.push(water);
	return water;
}

function drawWaters() {
	fill(50, 50, 255);
	noStroke();
	for(var i=0; i<waters.length; i++) {
		waters[i].draw();
	}
}