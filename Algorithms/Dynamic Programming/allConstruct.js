const allConstruct = (target,wordBank) => {
    if (target == '') return [[]]
    
    const result = [];

    for (let word of wordBank){
        if (target.indexOf(word) == 0){
            const suffix = target.slice(word.length);
            const suffixWays = allConstruct(suffix,wordBank)
            const targetWays = suffixWays.map( way => [word,...way]);
            result.push(...targetWays)
        }

    }
    return result
}

console.log(allConstruct('purple',['purp','p','ur','le','purpl']))
console.log(allConstruct("abcdef",["ab","abc","cd","def","abcd"]))
console.log(allConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
console.log(allConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
console.log(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee","eeeeeee"]))