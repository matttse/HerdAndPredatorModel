class Elk:
	def __init__(self, x0):
		self.position_i=[]
		self.velocity_i=[]
		self.pos_best_i=[]
		self.err_best_i=-1
		self.err_i=-1
		# pip freeze | xargs pip uninstall -y