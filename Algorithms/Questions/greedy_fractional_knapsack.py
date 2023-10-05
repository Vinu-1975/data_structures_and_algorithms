class Item:
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight
    def __str__(self):
        return f"({self.profit},{self.weight})"
    
    def __repr__(self):
        return self.__str__()
    
def fractional_knapsack(arr,W):
    n = len(arr)
    ppw = [round(x.profit/x.weight,2) for x in arr]
    print(ppw)

    for i in range(n):
        for j in range(n-1-i):
            if ppw[j] < ppw[j+1]:
                ppw[j],ppw[j+1] = ppw[j+1],ppw[j]
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
    total_profit = 0
    for item in arr:
        if W == 0:
            break
        if item.weight <= W:
            total_profit += item.profit
            W -= item.weight
        else:
            frac = W / item.weight
            total_profit += item.profit * frac
            W = 0
    return round(total_profit,2)

arr = [Item(10,2),Item(5,3),Item(15,5),Item(7,7),Item(6,1),Item(18,4),Item(3,1)]
W = 15
print(arr)
print(fractional_knapsack(arr,W))