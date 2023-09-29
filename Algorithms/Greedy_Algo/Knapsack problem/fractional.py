class Item:
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight
    
    def __str__(self):
        return f"{self.profit},{self.weight}"
    
    def __repr__(self):
        return self.__str__()

def knapsack(arr,W):
    ppw = []
    for item in arr:
        ppw.append(round(float(item.profit/item.weight),2))

    # sorting based on profit-per-weight(ppw)
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if ppw[j] < ppw[j+1]:
                ppw[j],ppw[j+1] = ppw[j+1],ppw[j]
                arr[j],arr[j+1] = arr[j+1],arr[j]

    tot_profit = 0
    for item in arr:
        if W == 0:
            break
        if item.weight <= W:
            tot_profit += item.profit
            W -= item.weight
        else:
            fraction = W / item.weight
            tot_profit += item.profit * fraction
            W = 0
    print(tot_profit)
    

arr = [Item(10,2),Item(5,3),Item(15,5),Item(7,7),Item(6,1),Item(18,4),Item(3,1)]
W = 15

knapsack(arr,W)