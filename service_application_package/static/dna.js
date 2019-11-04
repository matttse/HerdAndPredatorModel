function DNA(genes) {
	if (genes) {
		this.genes = genes;
	} else {
		this.genes = []//new random DNA
		for (var i = 0; i < genes.length; i++) {
			this.genes[i] = p5.Vector.random2D();//random vector
			this.genes[i].setMag(0.2)//inherent speed

		}
	}

	this.mating = function(mate) {
		var childDNA = [];
		//randomly select via p5 library
		//a point that is somewhere in the middle
		var midPoint = floor(random(this.genes.length));
		//create new / overwrite DNA with parents
		for (var i = 0; i < this.genes.length; i++) {
			if (i > midPoint) {
				childDNA[i] = this.genes[i];
			} else {
				childDNA[i] = mate.genes[i];
			}

		}
		return new DNA(childDNA);
	}
	//allows for some variability rather than just the first generation genes
	this.mutation = function() {
		for (var i = 0; i < this.genes.length; i++) {
			if (random(1) < 0.01) {//random number with mutation rate of 1%
				this.genes[i] = p5.Vector.random2D();//becomes new Random vector
				this.genes[i].setMag(0.1); //length of vector
			}
			
		}
	}
}