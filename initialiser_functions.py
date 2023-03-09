import random
import numpy as np
from car_class import Car, lying_car

def honest_cars_init(car_list:list, position):
#initialising honest cars with a random position, velocity and range of sight
    velocity = ((np.random.rand(2)*2)-1)
    range_of_sight = 0.1 #np.random.uniform(0, 0.25, size=(1)).astype(int)
    ID = str(len(car_list))
    coerced = None
    car_list.append(Car(position, velocity, range_of_sight, ID, coerced))
    return car_list

def lying_cars_init(car_list:list, position, fake_position):
#initialising lying cars with a random position, velocity and range of sight

    velocity = ((np.random.rand(2)*2)-1)
    range_of_sight = 0.1 #round(random.uniform(0.1,0.2), 100)
    ID = str(len(car_list))
    coerced = None
    car_list.append(lying_car(position, velocity, range_of_sight, ID, coerced, fake_position))

    return car_list


def create_position(environment):
    x_position = np.random.uniform(low=environment.x_coordinates[0], high=environment.x_coordinates[1], size=1)
    y_position = np.random.uniform(low=environment.y_coordinates[0], high=environment.y_coordinates[1], size=1)
    
    position = np.concatenate((x_position, y_position), axis=0)
    
    return position

#TODO: pass position and fake position as an input
def cars_init(number_of_cars, p, q, car_list, environment):

    for i in range(number_of_cars):
        coin_toss = np.random.rand()
        position = create_position(environment)
        
        if coin_toss < 1 - p:
            car_list = honest_cars_init(car_list, position)
        else:
            fake_position = create_position(environment)
            car_list = lying_cars_init(car_list, position, fake_position)


    for car in car_list:
        coin_toss = np.random.rand()
        
        if coin_toss < q:
            car.coerced = True
        else:
            car.coerced = False

        #print(car.ID, car.coerced, car.honest)     
    return car_list
