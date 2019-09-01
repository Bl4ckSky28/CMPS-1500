
def isClique(G, X, k):
    if k != len(X):
        return False
    else:
        for x in G:
            if x in X:
                if 
            
        

G = {1: [2, 3, 4], 2: [3, 4], 3: [1, 2, 4], 4: [2, 3]}
X = {2, 3, 4}

print(isClique(G, X, 3))


