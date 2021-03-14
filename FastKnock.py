"""
    *** FastKnock.py is the main method of the algorithm
    *** Processes are defined in this method for traversing the tree branches.
    *** Each Process writes its solutions into the separate files.
"""

from Node import Node
import PreProcessing as PreProc
import cobra.test
from identifyTargetSpace import identifyTargetSpace
from constructSubTree import constructSubTree
from traverseTree_nonrec import procTraverseTree
import sys
import multiprocessing
from findingCoKnockOut import findingCoKnockoutRxns



def construct_data_structure (number):
    data_struct = [[] for i in range(number+1)]
    return data_struct

"""
    * medium culture is determined and 
    * by preprocessing the model Removable and
    * coKnockoutRxns sets are obtained in this method
"""
def model_preparation (model_name):
    model = cobra.io.load_matlab_model(model_name)
    model.solver = "gurobi"
    
    model.reactions[model.reactions.index("EX_o2(e)")].lower_bound = 0
    model.reactions[model.reactions.index("EX_o2(e)")].upper_bound = 0

    model.reactions[model.reactions.index("EX_glc(e)")].lower_bound = -10
    model.reactions[model.reactions.index("EX_glc(e)")].upper_bound = 0

    coKnockoutRxns = findingCoKnockoutRxns(model)
    PreProc.identifying_eliminate_list(model)

    eliminate_list = []
    with open("eliminate_list.txt" , 'r') as f:
        for line in f:
            if line not in ['\n', '\r\n', '\t']:
                line = line.replace('\n', '')
                eliminate_list.append(line)
    model = PreProc.remove_blocked_rxn(model)

    Removable = []
    for i in model.reactions:
        if i.id not in eliminate_list:
            Removable.append(i.id)

    return model, Removable, coKnockoutRxns


def print_node(X):
    print X.level
    print X.deleted_rxns
    print X.target_space
    print X.flux_dist


""" The solutions are written in the file by this method"""
def writeInFile (level, solution):

    file_name = str(level)+".txt"
    with open(file_name , 'w') as f:
        for X in solution:
            sol = [X.deleted_rxns, X.biomass, X.chemical]
            f.write(str(sol))
            f.write('\n')
    f.close()
    
    

def main():
    
    target_level = input("Enter your desired level: ")

    queue = construct_data_structure (target_level)
    checked = construct_data_structure (target_level)
    solution = construct_data_structure (target_level)

    
    model, Removable, coKnockoutRxns = model_preparation ("iJR904.mat")

    root = Node (0,[] , [] , [],0,0)
    root = identifyTargetSpace(root, model, Removable,coKnockoutRxns)

    all_fba_call = [[] for i in range(target_level+1)]
    for i in range (target_level+1):
        all_fba_call[i] = 0
    
    level_one, queue, checked, solution, all_fba_call = constructSubTree(root, target_level, checked, queue, solution, model, Removable, all_fba_call, coKnockoutRxns)

    #--------- Process 1-----------------
    queue_p1 = construct_data_structure (target_level)
    checked_p1 = construct_data_structure (target_level)
    solution_p1 = construct_data_structure (target_level)
    
    all_fba_call_p1 = construct_data_structure (target_level)
    for i in range (target_level+1):
        all_fba_call_p1[i] = 0
        
    queue_p1[level_one] = queue[level_one][0:1]

    p1 = multiprocessing.Process(target = procTraverseTree, args=('p1', level_one, queue_p1, checked_p1, solution_p1, target_level, model, Removable, all_fba_call_p1, coKnockoutRxns))

    #--------- Process 2-----------------
    queue_p2 = construct_data_structure (target_level)
    checked_p2 = construct_data_structure (target_level)
    solution_p2 = construct_data_structure (target_level)
    
    all_fba_call_p2 = construct_data_structure (target_level)
    for i in range (target_level+1):
        all_fba_call_p2[i] = 0
        
    queue_p2[level_one] = queue[level_one][1:3]
    checked_p2[level_one] = queue[level_one][0:1]

    p2 = multiprocessing.Process(target = procTraverseTree, args=('p2', level_one, queue_p2, checked_p2, solution_p2, target_level, model, Removable, all_fba_call_p2, coKnockoutRxns))


    #--------- Process 3-----------------
    queue_p3 = construct_data_structure (target_level)
    checked_p3 = construct_data_structure (target_level)
    solution_p3 = construct_data_structure (target_level)
    
    all_fba_call_p3 = construct_data_structure (target_level)
    for i in range (target_level+1):
        all_fba_call_p3[i] = 0
        
    queue_p3[level_one] = queue[level_one][3:7]
    checked_p3[level_one] = queue[level_one][0:3]

    p3 = multiprocessing.Process(target = procTraverseTree, args=('p3', level_one, queue_p3, checked_p3, solution_p3, target_level, model, Removable, all_fba_call_p3, coKnockoutRxns))
    

    #--------- Process 4-----------------
    queue_p4 = construct_data_structure (target_level)
    checked_p4 = construct_data_structure (target_level)
    solution_p4 = construct_data_structure (target_level)
    
    all_fba_call_p4 = construct_data_structure (target_level)
    for i in range (target_level+1):
        all_fba_call_p4[i] = 0
        
    queue_p4[level_one] = queue[level_one][7:20]
    checked_p4[level_one] = queue[level_one][0:7]

    p4 = multiprocessing.Process(target = procTraverseTree, args=('p4', level_one, queue_p4, checked_p4, solution_p4, target_level, model, Removable, all_fba_call_p4, coKnockoutRxns))

    #--------- Process 5-----------------
    queue_p5 = construct_data_structure (target_level)
    checked_p5 = construct_data_structure (target_level)
    solution_p5 = construct_data_structure (target_level)
    
    all_fba_call_p5 = construct_data_structure (target_level)
    for i in range (target_level+1):
        all_fba_call_p5[i] = 0
        
    queue_p5[level_one] = queue[level_one][20:]
    checked_p5[level_one] = queue[level_one][0:20]

    p5 = multiprocessing.Process(target = procTraverseTree, args=('p5', level_one, queue_p5, checked_p5, solution_p5, target_level, model, Removable, all_fba_call_p5, coKnockoutRxns))

   
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
  

if __name__ =='__main__':
    main()
