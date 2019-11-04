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

	// this.mating
}