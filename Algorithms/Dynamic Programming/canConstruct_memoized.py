def canConstruct(target,wordBank,memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return True
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(suffix,wordBank,memo) is True:
                memo[target] = True
                return memo[target]
            
    memo[target] = False
    return memo[target]

print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))