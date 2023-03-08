import random
import numpy as np
from matplotlib import pyplot as plt
#import networkx as nx
#IMPORTANT: scipy must be at least version 1.8 otherwise networkx will throw an attribute error: 
# https://github.com/pyg-team/pytorch_geometric/issues/4378 

#---------------------START OF AIDA POL protocol----------------------:
def PoL(cars, depth, witness_number_per_depth:list):
    #DAG = nx.Graph()

    True_Positive = 0
    True_Negative = 0
    False_Positive = 0
    False_Negative = 0


    for car in cars:

        #A Car claims their position, starting the protocol round
        car_position = car.claim_position()

        #Car 1 names its witnesses
        named_witnesses = car.name_witness()
        named_cars = set()
        named_cars.add(car.ID)

        #A car with no witnesses is deemed a liar
        if named_witnesses is None:
            car.algorithm_honesty_output = False
            print('car has 0 witnesses', car.honest)
            
        #or has less than the required number of witnesses, or has named duplicate witnesses
        elif len(named_witnesses) < 2 or (len(named_witnesses) != len(set(named_witnesses))):
            car.algorithm_honesty_output = False
            print('car has less than 2 witnesses or cross referenced witnesses')
                
        else:
            
            #TODO: add the red car to the graph only if the witnesses tests pass
            #DAG.add_node(car, color = 'red')

            for witness in named_witnesses:

                witness_position = witness.claim_position()

                #The witness cannot have been named before (ie: cannot be Car 1)
                if witness.ID in named_cars:
                    car.algorithm_honesty_output = False
                    print('witness has already been named')

                #Car 1 must be a neighbour of the witness
                elif witness.is_car_a_neighbour(car) is False:
                    car.algorithm_honesty_output = False
                    print('caris not neighbour of the witness')
                    
                # Car 1 must be within the range of sight of the witness
                elif witness.is_in_range_of_sight(car_position) is False:
                    car.algorithm_honesty_output = False
                    print('car is not in ROS of witness')
                    
                else:
                    car.algorithm_honesty_output = True

                    #we add each witness ID to named_cars set to keep track of the named cars so far
                    named_cars.add(witness.ID)

                    #DAG.add_node(witness, color = 'blue')
                    #DAG.add_edge(car, witness)
                

                #Each witness must name its own witnesses (which we call attestors to avoid confusion)
                witness_attestors = witness.name_witness()

                #if witness has no attestors car 1 is deemed a liar
                if witness_attestors is None:
                    car.algorithm_honesty_output = False
                    print('car witness has no attestors')
                    
                #witness must have at least 2 attestors, and check that witness doesn't select same attestor twice
                elif len(witness_attestors) < 2 or (len(witness_attestors) != len(set(witness_attestors))):
                    car.algorithm_honesty_output = False
                    print('witnesses of car has less than 2 attestors, or named same attestor twice')

                    
                else:

                    # Attestors must be a neighbour AND be in range of sight of witness
                    for attestor in witness_attestors:

                        # Attestors must be a neighbour of the witness
                        if attestor.is_car_a_neighbour(witness) is False:
                            car.algorithm_honesty_output = False
                            print('witnesses is not a neighobour of the attestor')
                            
                        # Witness must be in range of sight of its attestor
                        elif attestor.is_in_range_of_sight(witness_position) is False:
                            car.algorithm_honesty_output = False
                            print('witness is not in ROS of attestor')

                        #check that none of the attestors have already been named before as a witness or car 1.
                        elif attestor.ID in named_cars:
                            car.algorithm_honesty_output = False           
                            print('attestor has already been named', car.ID)                 

                        else:
                            car.algorithm_honesty_output = True
                            #DAG.add_node(attestor, color = 'green')
                            #DAG.add_edge(witness, attestor)

        if car.honest is True and car.algorithm_honesty_output is True:
            True_Positive += 1
        if car.honest is True and car.algorithm_honesty_output is False:
            False_Negative += 1
        if car.honest is False and car.algorithm_honesty_output is True:
            False_Positive += 1
        if car.honest is False and car.algorithm_honesty_output is False:
            True_Negative += 1
        
        Accuracy = ((True_Positive + True_Negative) / (True_Positive + True_Negative + False_Positive + False_Negative)) * 100
        #color_map = nx.get_node_attributes(DAG, 'color')

        #some code i copied from stack overflow to change the color of each node, 
        # probably will do this better later    
        """ for key in color_map:
            if color_map[key] == 'green':
                color_map[key] = 'green'
            if color_map[key] == 'blue':
                color_map[key] = 'blue'
            if color_map[key] == 'red':
                color_map[key] = 'red'
            
        car_colors = [color_map.get(node) for node in DAG.nodes()] """
    
    #nx.draw(DAG, node_color=car_colors)
    #plt.show()
    return Accuracy, True_Positive, True_Negative, False_Positive, False_Negative #,DAG