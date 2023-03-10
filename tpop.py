import random
import numpy as np
from matplotlib import pyplot as plt
import initialiser_functions as i
import environment_class as e
#import networkx as nx
#IMPORTANT: scipy must be at least version 1.8 otherwise networkx will throw an attribute error: 
# https://github.com/pyg-team/pytorch_geometric/issues/4378 

def checks(car, car_position, witnesses, number_of_witnesses_needed:int, named_cars:set, threshold):

    #or has less than the required number of witnesses, or has named duplicate witnesses
    #NOTE: this should technically be: if len(named_witnesses)*threshold < witness_number then False, 
    #but then would have to pass a different value into car.name_witness(witness_number)

    if len(witnesses) < int(number_of_witnesses_needed *threshold) or (len(witnesses) != len(set(witnesses))):
        car.algorithm_honesty_output = False
        print('car has less than 2 witnesses or cross referenced witnesses')
            
    else:
        
        #TODO: add the red car to the graph only if the witnesses tests pass
        #DAG.add_node(car, color = 'red')
        counter = 0
        for witness in witnesses:

            #The witness cannot have been named before (ie: cannot be Car 1)
            if witness.ID in named_cars:
                car.algorithm_honesty_output = False
                #print('witness has already been named')

            #Car 1 must be a neighbour of the witness
            elif witness.is_car_a_neighbour(car) is False:
                car.algorithm_honesty_output = False
                #print('car is not neighbour of the witness')
                
            # Car 1 must be within the range of sight of the witness
            elif witness.is_in_range_of_sight(car_position) is False:
                car.algorithm_honesty_output = False
                #print('car is not in ROS of witness')
                
            else:
                car.algorithm_honesty_output = True
                counter += 1
                #print('entered True output')
                #we add each witness ID to named_cars set to keep track of the named cars so far
                named_cars.add(witness.ID)

        if counter < int(number_of_witnesses_needed *threshold):
            car.algorithm_honesty_output = False
        

    return witnesses, named_cars


#---------------------START OF AIDA POL protocol----------------------:
    
""" if len(witness_number_per_depth) != depth:
    raise Exception('Make sure there is number of witnesses defined for each round') """
#call this function for car in cars
def tpop(car, depth, witness_number_per_depth, threshold):
    
    for i in range(depth):
        
        number_of_witnesses_needed = witness_number_per_depth[i]
        car_position = car.claim_position()
        witnesses = car.name_witness(number_of_witnesses_needed)
        
        named_cars = set()
        named_cars.add(car.ID)

        if witnesses is None:
            car.algorithm_honesty_output = False
            
        else:    
            witnesses, named_cars = checks(car, car_position, witnesses, number_of_witnesses_needed, named_cars, threshold)

            for witness in witnesses:
                tpop(witness, depth -1, witness_number_per_depth, threshold)
                




def results(cars):
    True_Positive = 0
    True_Negative = 0
    False_Positive = 0
    False_Negative = 0


    for car in cars:

        if car.honest is True and car.algorithm_honesty_output is True:
            True_Positive += 1
        if car.honest is True and car.algorithm_honesty_output is False:
            False_Negative += 1
        if car.honest is False and car.algorithm_honesty_output is True:
            False_Positive += 1
        if car.honest is False and car.algorithm_honesty_output is False:
            True_Negative += 1

    Accuracy = ((True_Positive + True_Negative) / (True_Positive + True_Negative + False_Positive + False_Negative)) * 100
    
    return True_Positive, True_Negative, False_Positive, False_Negative, Accuracy


#print(True_Positive, True_Negative, False_Positive, False_Negative)
#print(False_Negative_cars)
