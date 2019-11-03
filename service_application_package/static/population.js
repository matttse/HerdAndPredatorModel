

function populate() {
	var tickets = [];
	if (countAlive()<=0) {
		
		var oldPopulation = vehicles.slice(0);
		vehicles = [];

		for(var i=0; i<oldPopulation.length; i++) {
			var v=oldPopulation[i];
			for (var j=0; j<(v.fitness); j++) { tickets.push(i); }
		}
		console.log(tickets.length);
		
		for(var i=0; i<vehiclesAmount; i++) {
			var v = addVehicle();
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
		return oldPopulation[j];
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

