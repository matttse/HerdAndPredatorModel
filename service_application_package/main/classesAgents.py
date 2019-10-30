from builtins import map

import numpy as np
from service_application_package.main.grassAgent import Grass
 
class Prey :
        animalType = -1 #1 if predator, -1 for prey
        age = 0
        epsilon = 0.2
 
        def __init__(self, xPosition, yPosition, ID, lastAte, father, ageOfReproduction,
                     rateOfDeath, rateOfReproduction, weights, rateOfLearning, discountFactor, minimumHunger):
 
            self.xPosition = xPosition
            self.yPosition = yPosition
            self.ID = ID
            self.lastAte = lastAte
            self.father = father
            self.ageOfReproduction = ageOfReproduction
            self.rateOfDeath = rateOfDeath
            self.rateOfReproduction = rateOfReproduction
            self.weights = weights
            self.rateOfLearning = rateOfLearning
            self.discountFactor = discountFactor
            self.minimumHunger = minimumHunger
            self.q = 0
  
        def sensoring(self,matrix):
            """
            Returns the number of the different agents for each neighbor cell
            """
            sensor = np.zeros([3, 9])  # Grass is nr 0, prey 1 and predator 2.
            iMoore = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    xDesired = (self.xPosition + i) % matrix.xDim
                    yDesired = (self.yPosition + j) % matrix.yDim

                    for agents in matrix.grid[xDesired][yDesired]:

                        if type(agents) is Grass:
                            sensor[0][iMoore] += 1
                        if type(agents) is Prey:
                            sensor[1][iMoore] += 1
                        if type(agents) is Predator:
                            sensor[2][iMoore] += 1
                    iMoore += 1
            return sensor

        def perceive(self,x,y,matrix): 
            """
            Returns the features for a position x,y as a matrix 9x3
            """
            #Row 1: grass, Row 2: prey, Row 3: predators
            features=np.zeros(12)
            # Count all predators and prey in the world
            nr_grass=matrix.numGrass
            nr_prey=matrix.numPrey
            nr_pred=matrix.numPred

            # How many agents are at each spot?
            sensor=np.zeros([3,9])  # Grass is nr 0, prey 1 and predator 2.
            iMoore=0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    xDesired = (x+i)%matrix.xDim
                    yDesired = (y+j)%matrix.yDim

                    for agents in matrix.grid[xDesired][yDesired]:

                        if type(agents) is Grass:
                            sensor[0][iMoore]+= 1
                        elif type(agents) is Prey:
                            sensor[1][iMoore]+= 1
                        else:
                            sensor[2][iMoore]+= 1
                    iMoore +=1
 
            # Calculate features. Note: this is for a prey
            if nr_pred != 0:
                features[0]=sum(sensor[2][:])/nr_pred #pred
            else:
                features[0] = 0
            if nr_prey != 0:
                features[1]=sum(sensor[1][:])/nr_prey # prey
            else:
                features[1] = 0
            if nr_grass != 0:
                features[2]=sum(sensor[0][:])/nr_grass # grass
            else:
                features[2] = 0
 
            if sum(sensor[2][:])==0:
                features[3:12]=0
            else:    
                features[3]=sensor[2][0]/sum(sensor[2][:])
                features[4]=sensor[2][1]/sum(sensor[2][:])
                features[5]=sensor[2][2]/sum(sensor[2][:])
                features[6]=sensor[2][3]/sum(sensor[2][:])
                features[7]=sensor[2][4]/sum(sensor[2][:])
                features[8]=sensor[2][5]/sum(sensor[2][:])
                features[9]=sensor[2][6]/sum(sensor[2][:])
                features[10]=sensor[2][7]/sum(sensor[2][:])
                features[11]=sensor[2][8]/sum(sensor[2][:])
 
            return features

        def cellEval(self,matrix):
            """
            Evaluate the neighbooring cells
            """
            x=self.xPosition
            y=self.yPosition
            iMoore=0
            score = np.empty([3, 9])
            for i_x_Moore in [-1,0,1] :
                for i_y_Moore in [-1,0,1] :
                    x_eval = np.mod(x+i_x_Moore,matrix.xDim) # eval case 0 if agent in case 50
                    y_eval = np.mod(y+i_y_Moore,matrix.yDim)
                    f_i = self.perceive(x_eval,y_eval,matrix) 
                    cell_score = np.dot(f_i,self.weights)
                    score[0][iMoore]=x_eval #gives the score and the absolute position
                    score[1][iMoore]=y_eval
                    score[2][iMoore]=cell_score
                    iMoore +=1
            return score

        def updatePosition(self, matrix):
            """
            Perform action (i.e. movement) of the agent depending on its evaluations
            """
            r = np.random.rand()

            if r < 1 - self.epsilon:
                score = self.cellEval(matrix)
                best_score_index = np.argmax(score[2, :])  # select the line with the best score
                x_new = score[0, best_score_index]
                y_new = score[1, best_score_index]
                self.q = score[2, best_score_index]
            else:
                x_new = (self.xPosition + np.random.randint(-1, 2) )%matrix.xDim
                y_new = (self.yPosition + np.random.randint(-1, 2) )%matrix.yDim
                features = self.perceive(x_new, y_new, matrix)
                self.q = np.dot(features, self.weights)
            new_position = np.array([x_new, y_new])
            return new_position
 
        def Aging(self, i):
            self.age += 1
            self.epsilon = 1 / i
            if i <= 501:
                self.rateOfLearning = 0.05 - 0.0001 * (i - 1)
            else:
                self.rateOfLearning = 0
            self.lastAte += 1
            return
 
#---------------------------Learning part-------------------------------#
        def getReward(self,matrix): 
            """
            opponent :number of the other species type within the agent’s Moore
            neighborhood normalized by the number of total
             type is 1 for predator and −1 for prey
            same = {0, 1} for if the opponent is on the same location
            """
            type_animal = self.animalType
            sensor = self.sensoring(matrix)
            x = self.xPosition
            y = self.yPosition
            features = self.perceive(x,y,matrix)
            feature_wanted = features[0]
            opponent = feature_wanted
            same = sensor[2][4]>0
            reward = opponent*type_animal + 2*same*type_animal
 
            return reward
 
        def getQFunction(self,features):
            weights = self.weights
 
            Q = 0
            for i in range(len(weights)):
                Q = Q + weights[i]*features[i]
 
            return Q
 
        def updateWeight(self, reward, matrix, Q_value):
            weights = self.weights
            rateOfLearning = self.rateOfLearning
            discountFactor = self.discountFactor
 
            #Compute the Q'-table:
            Q_prime = []
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    xDesired = (self.xPosition+i)%matrix.xDim
                    yDesired = (self.yPosition+j)%matrix.yDim
                    features = self.perceive(xDesired,yDesired,matrix)
                    Q_prime.append(self.getQFunction(features))
 
            #Update the weights:
            Q_prime_max = max(Q_prime)
            for i in range(0,len(weights)):
                if i <3:
                    c = 9/(matrix.xDim*matrix.yDim)
                else:
                    c = 1/9
                    
                w = weights[i]
                f = features[i]
                f = np.exp(-0.5*(f-c)**2)
 
                weights[i] = w + rateOfLearning*(reward +discountFactor*Q_prime_max - Q_value)*f
 
            self.weights= weights
            return

        def Eat(self, agentListAtMatrixPosition):
            for agent in agentListAtMatrixPosition: #Not selected randomly at the moment, just eats the first prey in the list
                if type(agent) is Grass:
                    killFoodSource = agent.consume()
                    self.lastAte = 0
                    if killFoodSource == 0:
                        return agent.ID
            return -1

        def Starve(self):
            if self.lastAte > self.minimumHunger:
                pdeath = self.lastAte*self.rateOfDeath
                r = np.random.rand()
                if r < pdeath:
                    return self.ID
            return -1

        def Reproduce(self):
            offspring = 0
            if self.age >= self.ageOfReproduction:
                r = np.random.rand()
                if r < self.rateOfReproduction:
                    offspring = Prey(self.xPosition, self.yPosition, -1, 0, self.ID, self.ageOfReproduction,
                                     self.rateOfDeath, self.rateOfReproduction, self.weights, self.rateOfLearning,
                                     self.discountFactor, self.minimumHunger) #ID is changed in Grid.update()
            return offspring
 
class Predator:
 
        animalType = 1 #1 if predator, -1 for prey
        age = 0
        epsilon = 0.2
 
        def __init__(self, xPosition, yPosition, ID, lastAte, father, ageOfReproduction,
                     rateOfDeath, rateOfReproduction, weights, rateOfLearning,discountFactor, minimumHunger):
 
            self.xPosition = xPosition
            self.yPosition = yPosition
            self.ID = ID
            self.lastAte = lastAte
            self.father = father
            self.ageOfReproduction = ageOfReproduction
            self.rateOfDeath = rateOfDeath;
            self.rateOfReproduction = rateOfReproduction
            self.weights = weights
            self.rateOfLearning = rateOfLearning
            self.discountFactor = discountFactor
            self.minimumHunger = minimumHunger
            self.q = 0
 
        def sensoring(self,matrix):
            """
            Returns the number of the different agents for each neighbor cell
            """            
            sensor = np.zeros([3, 9])  # Grass is nr 0, prey 1 and predator 2.
            iMoore = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    xDesired = (self.xPosition + i) % matrix.xDim
                    yDesired = (self.yPosition + j) % matrix.yDim
                    for agents in matrix.grid[xDesired][yDesired]:
                        if type(agents) is Grass:
                            sensor[0][iMoore] += 1
                        if type(agents) is Prey:
                            sensor[1][iMoore] += 1
                        if type(agents) is Predator:
                            sensor[2][iMoore] += 1
                    iMoore += 1
            return sensor    
 
        def perceive(self,x,y,matrix): 
            """
            Returns the features for a position (x,y) as a matrix 9x3
            """
            #Row 1: grass, Row 2: prey, Row 3: predators
            features=np.zeros(12)
            # Count all predators and prey in the world
            nr_grass=matrix.numGrass
            nr_prey=matrix.numPrey
            nr_pred=matrix.numPred

            # How many agents are at each spot?
            sensor=np.zeros([3,9])  # Grass is nr 0, prey 1 and predator 2.
            iMoore=0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    xDesired = (x+i)%matrix.xDim
                    yDesired = (y+j)%matrix.yDim

                    for agents in matrix.grid[xDesired][yDesired]:

                        if type(agents) is Grass:
                            sensor[0][iMoore]+= 1
                        elif type(agents) is Prey:
                            sensor[1][iMoore]+= 1
                        else:
                            sensor[2][iMoore]+= 1
                    iMoore +=1
            # Calculate features. Note: this is for a predator
            if nr_prey != 0:
                features[0]=sum(sensor[1][:])/nr_prey  #prey
            else:
                features[0] = 0
            if nr_pred != 0:
                features[1]=sum(sensor[2][:])/nr_pred  # predators
            else:
                features[1] = 0
            if nr_grass != 0:
                features[2]=sum(sensor[0][:])/nr_grass # grass
            else:
                features[2] = 0
 
            if sum(sensor[1][:])==0:
                features[3:12]=0
            else:    
                features[3]=sensor[1][0]/sum(sensor[1][:])
                features[4]=sensor[1][1]/sum(sensor[1][:])
                features[5]=sensor[1][2]/sum(sensor[1][:])
                features[6]=sensor[1][3]/sum(sensor[1][:])
                features[7]=sensor[1][4]/sum(sensor[1][:])
                features[8]=sensor[1][5]/sum(sensor[1][:])
                features[9]=sensor[1][6]/sum(sensor[1][:])
                features[10]=sensor[1][7]/sum(sensor[1][:])
                features[11]=sensor[1][8]/sum(sensor[1][:])
 
            return features
 
        def cellEval(self,matrix):
            """
            Evaluate the neighbooring cells
            """
            x=self.xPosition
            y=self.yPosition
            iMoore=0
            score = np.empty([3, 9])
            for i_x_Moore in [-1,0,1] :
                for i_y_Moore in [-1,0,1] :
                    x_eval = np.mod(x+i_x_Moore,matrix.xDim) # eval case 0 if agent in case 50
                    y_eval = np.mod(y+i_y_Moore,matrix.yDim)
                    f_i = self.perceive(x_eval,y_eval,matrix) #self.perceive or perceive ?
                    cell_score = np.dot(f_i,self.weights)
                    score[0][iMoore]=x_eval #gives the score and the absolute position
                    score[1][iMoore]=y_eval
                    score[2][iMoore]=cell_score
                    iMoore += 1
            return score
 
        def updatePosition(self,matrix):
            """
            Perform action (i.e. movement) of the agent depending on its evaluations
            """            
            r=np.random.rand()
 
            if r < 1 - self.epsilon:
                score = self.cellEval(matrix)
                best_score_index = np.argmax(score[2,:]) #select the line with the best score
                x_new = score[0, best_score_index]
                y_new = score[1, best_score_index]
                self.q = score[2, best_score_index]
            else :
                x_new = (self.xPosition + np.random.randint(-1, 2) )%matrix.xDim
                y_new = (self.yPosition + np.random.randint(-1, 2) )%matrix.yDim
                features = self.perceive(x_new, y_new, matrix)
                self.q = np.dot(features, self.weights)
            new_position = np.array([x_new, y_new])
            return new_position
 
        def Aging(self, i):
 
            self.age +=1
            self.epsilon = 1/i
            if i <= 501:
                self.rateOfLearning = 0.05 - 0.0001*(i - 1)
            else:
                self.rateOfLearning = 0
            self.lastAte +=1
 
            return
#---------------------------Learning part-------------------------------#
        def getReward(self,matrix):
            """
            opponent :number of the other species type within the agent’s Moore
            neighborhood normalized by the number of total
            type is 1 for predator and −1 for prey
            same = {0, 1} for if the opponent is on the same location
            """
            type_animal = self.animalType
            sensor = self.sensoring(matrix)
            x = self.xPosition
            y = self.yPosition
            features = self.perceive(x,y,matrix)
            feature_wanted = features[0]
            opponent = feature_wanted
            same = sensor[1][4]>0
            reward = opponent*type_animal + 2*same*type_animal
            return reward
 
        def getQFunction(self,features):
            weights = self.weights
 
            Q = 0
            for i in range(len(weights)):
                Q = Q + weights[i]*features[i]
 
            return Q
 
        def updateWeight(self, reward, matrix, Q_value):
            weights = self.weights
            rateOfLearning = self.rateOfLearning
            discountFactor = self.discountFactor
 
            #Compute the Q'-table:
            Q_prime = []
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    xDesired = (self.xPosition+i)%matrix.xDim
                    yDesired = (self.yPosition+j)%matrix.yDim
 
                    features = self.perceive(xDesired,yDesired,matrix)
                    Q_prime.append(self.getQFunction(features))
 
            #Update the weights:
            Q_prime_max = max(Q_prime)
            for i in range(0,len(weights)):
                if i<3:
                    c = 9/(matrix.xDim*matrix.yDim)
                else:
                    c=1/9
                    
                w = weights[i]
                f = features[i]
                f = np.exp(-0.5*(f-c)**2)
                weights[i] = w + rateOfLearning*(reward +discountFactor*Q_prime_max - Q_value)*f
 
            self.weights= weights
            return

        def Eat(self, agentListAtMatrixPosition):
            for agent in agentListAtMatrixPosition:
                if type(agent) is Prey: #Not selected randomly at the moment, just eats the first prey in the list
                    self.lastAte = 0
                    return agent.ID
            return -1

        def Starve(self):
            if self.lastAte > self.minimumHunger:
                pdeath = self.lastAte*self.rateOfDeath
                r = np.random.rand()
                if r < pdeath:
                    return self.ID
            return -1

        def Reproduce(self):
            offspring = 0
            if self.age >= self.ageOfReproduction:
                r = np.random.rand()
                if r < self.rateOfReproduction:
                    offspring = Predator(self.xPosition, self.yPosition, -1, 0, self.ID, self.ageOfReproduction,
                                            self.rateOfDeath, self.rateOfReproduction, self.weights, self.rateOfLearning,
                                            self.discountFactor, self.minimumHunger) #ID is changed in Grid.update()
            return offspring
