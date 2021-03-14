"""
    *** isMaximizedSolution specifies whether a flux distribution of a node X can be the maximized solution to the problem
    *** In this function all of the desired chemicals and their threshold are defined and set.
"""

def isMaximizedSolution(X):

    chemical = "EX_succ(e)"
    biomass = "BiomassEcoli"
    Th_chemical = 0.64
    Th_biomass = 0.01

    if (X.flux_dist.x_dict[biomass] >Th_biomass) and (X.flux_dist.x_dict[chemical] >Th_chemical):
        return True
    else:
        return False

def setSolution(X):
    chemical = "EX_succ(e)"
    biomass = "BiomassEcoli"

    X.biomass = X.flux_dist.x_dict[biomass]
    X.chemical = X.flux_dist.x_dict[chemical]

    return X

    
    
