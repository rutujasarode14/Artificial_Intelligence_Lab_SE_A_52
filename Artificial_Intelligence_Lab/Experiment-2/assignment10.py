def alpha_beta(depth, nodeIndex, isMax, values, alpha, beta, maxDepth):

    if depth == maxDepth:
        return values[nodeIndex]
    
    if isMax:
        best = float('-inf')
        for i in range(2): 
            val = alpha_beta(depth+1, nodeIndex*2+i, False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break 
        return best
    else:
        best = float('inf')
        for i in range(2):  
            val = alpha_beta(depth+1, nodeIndex*2+i, True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break   
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]  

maxDepth = 3
optimal_value = alpha_beta(0, 0, True, values, float('-inf'), float('inf'), maxDepth)
print("Optimal value (with Alpha-Beta Pruning):", optimal_value)
