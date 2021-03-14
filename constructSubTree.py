"""
    *** This method is construct corresponding subtree of the node X
    *** it returns children nodes of X at level (X.level+1)
"""

from Node import Node
from identifyTargetSpace import identifyTargetSpace
from identifyMaximizedSolution import isMaximizedSolution
from identifyMaximizedSolution import setSolution

def constructSubTree (X, target_level, checked, queue, solution, model, Removable,all_fba_call, coKnockoutRxns):

    current_level = X.level
    next_level = current_level + 1

    if current_level == target_level:
        return target_level, queue, checked, solution, all_fba_call

    else:
        for rxn in X.target_space:
            
            if (rxn not in checked[next_level]) and (rxn in coKnockoutRxns):
                
                r = Node (next_level, X.deleted_rxns+[rxn], [], [],0,0)

                r = identifyTargetSpace(r, model, Removable, coKnockoutRxns)
                all_fba_call[next_level] += 1
                
                if  (r.flux_dist != 0):
                    if (isMaximizedSolution(r)):
                        r = setSolution(r)
                        solution[next_level].append(r)

                queue[next_level].append(r)
                checked[next_level].append(rxn)

        return next_level, queue, checked, solution, all_fba_call

                
                
    
