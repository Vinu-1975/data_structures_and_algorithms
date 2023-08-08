def countConstruct(target,wordBank,memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    
    totalCount = 0

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            numOfWays = countConstruct(suffix,wordBank,memo)
            totalCount += numOfWays
    
    memo[target] = totalCount
    return memo[target]

print(countConstruct("purple",['purp','p','ur','le','purpl']))
print(countConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee","eeeeeee"]))