from service_application_package.ga.animal import Animal
import numpy as np
class DNA(Animal):
	def __init__(self, Animal):
		if not Animal.genes:
			self.genes = np.random2d()
		else:
			self.genes = Animal.genes
	def crossover(population_new, pc):
    
	    half=int(len(population_new)/2)
	    father=population_new[:half]
	    mother=population_new[half:]
	    np.random.shuffle(father)
	    np.random.shuffle(mother)
	    offspring=[]
	    for i in range(half):      
	        if np.random.uniform(0,1)<=pc:
	            copint = np.random.randint(0,int(len(father[i])/2))
	            son=father[i][:copint]+(mother[i][copint:])
	            daughter=mother[i][:copint]+(father[i][copint:])
	        else:
	            son=father[i]
	            daughter=mother[i]
	        offspring.append(son)
	        offspring.append(daughter)
	    return offspring
	def mutation(offspring,pm):
	    for i in range(len(offspring)):
	        if np.random.uniform(0,1)<=pm:
	            position=np.random.randint(0,len(offspring[i]))
	            #'str' object does not support item assignment,cannot use = to change value
	            if position!=0:
	                if offspring[i][position]=='1':
	                    offspring[i]=offspring[i][:position-1]+'0'+offspring[i][position:]
	                else:
	                    offspring[i]=offspring[i][:position-1]+'1'+offspring[i][position:]
	            else:
	                if offspring[i][position]=='1':
	                    offspring[i]='0'+offspring[i][1:]
	                else:
	                    offspring[i]='1'+offspring[i][1:]
	    return offspring
	def selection(population,value):
	    
	    fitness_sum=[]
	    for i in range(len(value)):
	        if i ==0:
	            fitness_sum.append(value[i])
	        else:
	            fitness_sum.append(fitness_sum[i-1]+value[i])
	    
	    for i in range(len(fitness_sum)):
	        fitness_sum[i]/=sum(value)
	    
	    #select new population
	    population_new=[]
	    for i in range(len(value)):
	        rand=np.random.uniform(0,1)
	        for j in range(len(value)):
	            if j==0:
	                if 0<rand and rand<=fitness_sum[j]:
	                    population_new.append(population[j])
	                    
	                
	            else:
	                if fitness_sum[j-1]<rand and rand<=fitness_sum[j]:
	                    population_new.append(population[j])             
	    return population_new