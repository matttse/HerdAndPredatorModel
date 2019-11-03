
function grassClass() {
	this.pos = createVector(random(spawnBorder, width-spawnBorder), random(spawnBorder, height-spawnBorder));

	this.draw = function() {
		ellipse(this.pos.x, this.pos.y, 6, 6);
	}
}

function addGrasses(n) { 
	for(var i=0; i<n; i++) {
		addGrass();
	}
}
function addGrass() {
	var grass = new grassClass();
	grasss.push(grass);
	return grass;
}

function drawGrasses() {
	fill(50, 255, 50);
	noStroke();
	for(var i=0; i<grasss.length; i++) {
		grasss[i].draw();
	}
}