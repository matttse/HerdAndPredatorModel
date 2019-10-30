from __future__ import division
from flask import render_template, request, Blueprint
from service_application_package.main.forms import GenerationNumberAndStartForm
import argparse
from matplotlib import pyplot as plt
import pyp5js as p5
import pickle
import json
import math
import numpy as np

ga = Blueprint('ga', __name__)

genes = []
def DNA():
	for i in range(500):
		genes[i] = p5.Vector.random2d()
	print (genes)
	# else:
	# 	self.genes = 
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

def decode(x):
    y=0+int(x,2)/(2**17-1)*9
    return y



def fitness(population,aimFunction):
    value=[]
    for i in range(len(population)):
        # value.append(aimFunction(decode(population[i])))
        #weed out negative value
        if value[i]<0:
            value[i]=0
    return value

@ga.route("/runGA/<int:numberOfGenerations>")
def start(numberOfGenerations):

	# create start def
	form = GenerationNumberAndStartForm()


	# x=[i/100 for i in range(900)]
	# y=[0 for i in range(900)]
	# for i in range(900):

	#     y[i]=aimFunction(x[i])

	# #plt.plot(x,y)


	# #initiate population
	# population=[]
	# for i  in range(10):
	#     entity=''
	#     for j in range(17):  
	#         entity=entity+str(np.random.randint(0,2))
	#     population.append(entity)

	    
	# t=[]
	# for i in range(1000):
	#     #selection
	#     value=fitness(population,aimFunction)
	#     population_new=selection(population,value)
	#     #crossover
	#     offspring =crossover(population_new,0.7)
	#     #mutation
	#     population=mutation(offspring,0.02)
	#     result=[]
	#     # for j in range(len(population)):
	#         # result.append(aimFunction(decode(population[j])))
	#     t.append(max(result))
	    
	# # plt.plot(t)
	# plt.axhline(max(y), linewidth=1, color='r') 

	return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations, universe=DNA())



# def stop():
	# create stop def