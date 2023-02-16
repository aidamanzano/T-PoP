# T-PoP
We present Tree Proof of Position protocol (T-PoP). It is a decentralised, collaborative protocol that allows agents to prove their position. 
The protocol uses a tree architecture and does not rely on a central verifier to approve or reject each agent's claimed position.

The T-PoP algorithm script is `proof_of_location.py`. The agent class is `car_class.py` and the environment is defined in the `environment_class.py` script.

The simulations showing the results of T-PoP's accuracy and the Naive Proof of Location algorithm can be found in the notebook: `final_simulation_generator.ipynb`. 
Feel free to change the threshold parameters in the Naive-PoL algorithm to experiment with different results. 

The simulations in `new_simulations.ipynb` show the accuracy of T-PoP as we vary through every single possible combination of coerced, honest and dishonest agent distributions when the total number of agents is 1000.
You can change these variables and experiment with different results. 

NOTE: the simulation script is set up to save all the results in text files in your cwd. If you don't want all this data saved, you will have to change this in the appropriate simulation generator function for each algorithm in the `simulation_functions.py` script.

The `initialiser_functions.py` script is to generate the different types of agents, and the `simulation_functions.py` script contains useful functions to generate the simulation results calling the different types of algorithms.

I will link the detailed explanation of T-PoP here as soon as the work is up on Arxiv, but you can check the comments of the `proof_of_location.py` file to follow how the algorithm works.
Same with the Naive Proof of Location algorithm, the details can be found in the `refactoredNaivePoL.py` script.

The simulation generator notebooks will likely be updated, and details on the collaborative lying attack simulations will be up shortly too. Currently, these can be found in `collaborative-lying simulations.ipynb`.
This is a simulation on how robust is T-PoP to an attack where a cluster of lying and coerced cars agree to lie together. 

## TLDR: 
Quick start guide: for in depth accuracy results of T-PoP go to: `new_simulations.ipynb`

For comparison between T-PoP and the naive proof of position algorithm go to: `final_simulation_generator.ipynb`

For collaborative lying cluster attacks go to: `collaborative-lying simulations.ipynb`

## TODO: 
I need to upload a requirements file still.
