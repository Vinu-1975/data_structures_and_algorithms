const bestSum = (targetSum,numbers)=>{
    if (targetSum === 0) return []
    if (targetSum < 0) return null

    let shortestCombination = null

    for(let num of numbers){
        const remainder = targetSum - num
        const remainderResult = bestSum(remainder,numbers)
        if (remainderResult !== null){
            combination =  [ ...remainderResult,num]
            if (shortestCombination != null || combination.length < shortestCombination.length){
                shortestCombination = combination
            }
        }
    }
    
    return shortestCombination
}