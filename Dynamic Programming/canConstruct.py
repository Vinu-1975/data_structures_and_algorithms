def canConstruct(target,wordBank):
    if target == '':
        return True
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(suffix,wordBank) is True:
                return True
            
    return False
    
print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee","eeeeeee"]))