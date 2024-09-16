#O(N^2)

def max_profit(prices):
    n = len(prices)
    res = 0
    
    for i in range(n - 1):
        for j in range(i + 1, n): 
            res = max(res, prices[j] - prices[i])
    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(max_profit(prices))
    

# O(N)
    
def maxProfit(prices):
    minSoFar = prices[0]
    res = 0

    
    for i in range(1, len(prices)):
        minSoFar = min(minSoFar, prices[i])
                       
        res = max(res, prices[i] - minSoFar)
    
    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices))