const howSum = (targetSum,numbers)=>{
    if (targetSum === 0) return []
    if (targetSum < 0) return null

    for(let num of numbers){
        const remainder = targetSum - num
        const remainderResult = howSum(remainder,numbers)
        if (remainderResult !== null){
            return [ ...remainderResult,num]
        }
    }
    return null
}