// var preys = [];
function preyClass(dna) {
	this.pos = createVector(random(spawnBorder, width-spawnBorder), random(spawnBorder, height-spawnBorder));
	this.vel = createVector(random(-2, 2), random(-2, 2));
	this.acc = createVector();
	this.r = 6;

	this.fitness = 0;
	this.dead = false;
	this.health = 1;
	this.thirst = 0;
	//existing DNA
	// if (dna) {
	// 	this.dna = dna;
	// } else {
	// 	// this.dna = {
	// 	// 	grassMult: random(-maxMult,maxMult),
	// 	// 	grassPerc: random(0,maxPerc),
	// 	// 	poisonMult: random(-maxMult,maxMult),
	// 	// 	poisonPerc: random(0,maxPerc),
	// 	// 	waterMult: random(-maxMult,maxMult),
	// 	// 	waterPerc: random(0,maxPerc)
	// 	// }
	// 	this.dna = new DNA();
	// }
	// Did it receive DNA to copy?
	if (dna instanceof Array) {
		this.dna = [];
		// Copy all the DNA
		for (var i = 0; i < dna.length; i++) {
		  // 10% chance of mutation
		  if (random(1) < 0.1) {
		    if (i < 2) {
		      // Adjust steering force weights
		      this.dna[i] = dna[i] + random(-0.2, 0.2);

		    } else {
		      // Adjust perception radius
		      this.dna[i] = dna[i] + random(-10, 10);
		    }
		    // Copy DNA
		  } else {
		    this.dna[i] = dna[i];
		  }
		}
		} else {
		var maxf = 3;
		// DNA
		// 0: Attraction/Repulsion to food
		// 1: Attraction/Repulsion to poison
		// 2: Radius to sense food
		// 3: Radius to sense poison
		this.dna = [random(-maxf, maxf), random(-maxf, maxf), random(5, 100), random(5, 100)];
	}
	
	this.eat = function(list, perception, lifeGain, thirstGain) {
		var record = Infinity;
		var closest = null;
		for(var i=list.length-1; i>=0; i--) {
			var d = this.pos.dist(list[i].pos);
			if (d<this.r*2) {
				list.splice(i, 1);
				this.addHealth(lifeGain);
				this.addThirst(thirstGain);
			} else if (d<record && d<perception) { 
				record=d;
				closest = list[i].pos;
			}
		}
		if (closest!=null) {
			return this.seek(closest);
		}
		return createVector(0, 0);
	}

	this.seek = function(target) {
		var desired = p5.Vector.sub(target, this.pos);
		
		desired.setMag(maxspeed);

		var steer = p5.Vector.sub(desired, this.vel);
		steer.limit(maxTurnForce);
		
		return steer;
	}

	this.behaviour = function(grassList, poisonList) {
		var steer1 = this.eat(grassList, this.dna.grassPerc, 0.05, 0.01);
		var steer2 = this.eat(poisonList, this.dna.poisonPerc, -0.34, -0.05);
		// var steer3 = this.eat(waterList, this.dna.waterPerc, 0, -0.05);

		steer1.mult(this.dna.grassMult);
		steer2.mult(this.dna.poisonMult);
		// steer3.mult(this.dna.waterMult);

		this.acc.add(steer1);
		this.acc.add(steer2);
		// this.acc.add(steer3);
	}

	this.boundaries = function() {
		if (this.pos.x>width-spawnBorder || this.pos.x<spawnBorder) {
			this.acc.add(this.seek(createVector(width/2, this.pos.y)));
		}
		if (this.pos.y>height-spawnBorder || this.pos.y<spawnBorder) {
			this.acc.add(this.seek(createVector(this.pos.x, height/2)));
		}

		
	}

	this.update = function() {
		if (this.dead==true) { return; }

		this.boundaries();
		this.vel.add(this.acc);
		this.vel.limit(maxspeed);
		this.pos.add(this.vel);

		this.acc.mult(0);

		this.addThirst(0.002);
		this.addHealth(-this.thirst/100);
		this.fitness++;
	}

	this.addHealth = function(amount) {
		this.health+=amount;
		if (this.health>1) { this.health=1; }
	}
	this.addThirst = function(amount) {
		this.thirst+=amount;
		if (this.thirst>1) { this.thirst=1; }
		else if (this.thirst<0) { this.thirst=0; }
	}

	this.limit = function() {
		if(this.dna.grassMult>maxMult) { this.dna.grassMult=maxMult; }
		else if(this.dna.grassMult<-maxMult) { this.dna.grassMult=-maxMult; }
		if(this.dna.grassPerc>maxPerc) { this.dna.grassPerc=maxPerc; }

		if(this.dna.poisonMult>maxMult) { this.dna.poisonMult=maxMult; }
		else if(this.dna.poisonMult<-maxMult) { this.dna.poisonMult=-maxMult; }
		if(this.dna.poisonPerc>maxPerc) { this.dna.poisonPerc=maxPerc; }
	}

	this.draw = function() {
		//if (this.dead==true) { return; }
		if (this.pos.x>width || this.pos.x<0 || this.pos.y>height || this.pos.y<0) { return; }

		var gr = color(0, 255, 0);
		var rd = color(255, 0, 0);
		var col = lerpColor(rd, gr, this.health);

	    push();
		    translate(this.pos.x,this.pos.y);

		    if(drawPerception==true && this.dead==false) {
		    	noFill(); 
		    	stroke(0, 255, 0, 80);
			    ellipse(0, 0, this.dna.grassPerc*2, this.dna.grassPerc*2);
			    stroke(255, 0, 0, 80);
			    ellipse(0, 0, this.dna.poisonPerc*2, this.dna.poisonPerc*2);
			    stroke(0, 0, 255, 80);
			    ellipse(0, 0, this.dna.waterPerc*2, this.dna.waterPerc*2);
		    }

		    rotate(this.vel.heading()+PI/2);

			fill(col); stroke(col);
		    beginShape();
			    vertex(0, -this.r*2);
			    vertex(-this.r, this.r*2);
			    vertex(this.r, this.r*2);
		    endShape(CLOSE);
	    pop();
	}

	//fitness scoring
	this.getFitness = function() {
		//closer to target == better fitness
		var distance = dist(this.position.x, this.position.y, target.x, target.y);
		//1 == best fitness score possible i.e. we hit the target
		// this.fitness = (1 / distance);
		this.fitness = map(distance, 0, width, width, 0);//mapping the distance, inverted distance val
		//just rewarding the fit rockets
		if (this.touching) {
			this.fitness *= 10;//boost fitness scores
			if (this.elapsedTime < 2000) {
				this.fitness *= (10^3);//boost fitness scores
			} else if (this.elapsedTime < 1000) {
				this.fitness *= (10^4);//boost fitness scores
			} else if (this.elapsedTime < 500) {
				this.fitness *= (10^5);//boost fitness scores
			} else if (this.elapsedTime < 100) {
				this.fitness *= (10^6);//boost fitness scores
			}
		}
		if (this.collision) {
			if (this.border) {
				this.fitness /= 100;
			} else if (this.obstacle) {
				this.fitness /= 5;
			}
			
		}
		
	}
}



function addPreys(n) { 
	for(var i=0; i<n; i++) {
		addPrey();
	}
}
function addPrey(){
	var prey = new preyClass();

	preys.push(prey);
	return prey;
}
function drawPreys() {
	stroke(200);
	strokeWeight(2);
	for(var i=0; i<preys.length; i++) {
		preys[i].draw();
	}
}
function updatePreys() {
	var factors = [grasses, poisons];

	for(var i=0; i<preys.length; i++) {
		preys[i].behaviour(grasses, poisons);
		preys[i].update();
	}

	killPreys();
}
function killPreys() {
	for(var i=preys.length-1; i>=0; i--) {
		var v = preys[i];
		if (v.health<=0) {
			v.dead = true;
			//preys.splice(i, 1);
		}

	}
}
function countAlive() {
	var count = 0;
	for(var i=0; i<preys.length; i++) {
		if (preys[i].dead==false) { count++; }
	}
	return count;
}