"""
    *** This file contains two function, procTraverseTree which call traverseTree function for each processes of the parallel algorithm
    *** The traverseTree subprocedure recursively navigates the tree based on a depth-first traversal. 
"""


from constructSubTree import constructSubTree

def writeInFile (process_name, level, solution):

    file_name = process_name+'_'+str(level)+".txt"
    with open(file_name , 'w') as f:
        for X in solution:
            sol = [X.deleted_rxns, X.biomass, X.chemical]
            f.write(str(sol))
            f.write('\n')
    f.close()
    

def traverseTree(process_name,level, queue, checked, solution, target_level, model, Removable, all_fba_call, coKnockoutRxns):

    while True:

        if level == 0:
            return solution

        elif len(queue[level]) == 0:
            checked[level] = []
            level = level - 1

        else:
            X = queue[level].pop(0)
            next_level, queue, checked, solution, all_fba_call = constructSubTree (X, target_level, checked, queue, solution, model, Removable, all_fba_call, coKnockoutRxns)
            level = next_level
            print process_name,level,len(queue[level]), len (checked[level])


def procTraverseTree(process_name, level, queue, checked, solution, target_level, model, Removable, all_fba_call, coKnockoutRxns):

    print "process ", process_name, " is started."
    solution = traverseTree(process_name,level, queue, checked, solution, target_level, model, Removable, all_fba_call, coKnockoutRxns)
    for i in range(len(solution)):
        writeInFile (process_name,i, solution[i])

    print "process ", process_name, " is fininshed."


        
