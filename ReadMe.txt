
Introduction:
	FastKnock is an efficient algorithm to identify all possible knockout strategies for growth-coupled overproduction of biochemical(s) of interest.


Prerequisites:
	- python 2.7 or 3.0
	- Cobrapy 0.15.2 and above
		pip install cobra
	- Gurobi 7.5.2 and above
		python -m pip install -i https://pypi.gurobi.com gurobipy

Running the project:
	1 - copy a desired genome scale model (.mat or .xml file) to the main directory of project
	2 - specify the name of the model in the main method of FastKnock.py
	3 - define the medium culture in the model_preparation function in FastKnock.py
	4 - define the desired chemicals and biomass reactions and their threshold in identifyMaximizedSolution.py
	5 - in the main function of FastKnock.py demonstrate the the workspace of each process
	6 - run the fastKnock.py file

		


Details of each file:

- Fastknock.py: FastKnock.py is the main method of the algorithm.
		Processes are defined in this method for traversing the tree branches.
    		Each Process writes its solutions into the separate files.

- PreProcessing.py : PreProcessing.py aims to  determine eliminate list of the model.

- Gene_Rule.py : This file demonstrates the essential and involved sets of each reaction.
    		 These sets are being used in Clustering_Reactions.py and findingCoKnockOut.py

- Clustering_Reactions.py: In this file, based on the obtained essential and involved sets of each reaction in Gene_Rule.py,
			   the way of each reaction knockout by the genes is determined.
			   Other reactions that are forcibly eliminated with the reaction are also identified.

- Node.py: This class is definition of the node object and its properties.


- findingCoKnockOut.py: In this function, based on the analysis of the Clustering_Reactions.py and Gene_Rule.py,
		        all of coKnockout reactions are identified.

- traverseTree_nonrec.py: This file contains two function, procTraverseTree which call traverseTree function for each processes of the parallel algorithm.
   			  The traverseTree sub-procedure recursively navigates the tree based on a depth-first traversal. 

- constructSubTree.py: This method is construct corresponding subtree of the node X
    		       It returns children nodes of X at level (X.level+1)

- identifyTargetSpace.py: In this method the target_space of each node X is obtained.
    			  It determines the flux distribution and target space of node X.

- identifyMaximizedSolution.py: This method specifies whether a flux distribution of a node X can be the maximized solution to the problem.
    				In this function all of the desired chemicals and their threshold are defined.