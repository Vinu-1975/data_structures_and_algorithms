def climb_stair(n,memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = 1
        return memo[n]
    memo[n] = climb_stair(n-1,memo) + climb_stair(n-2,memo)
    return memo[n]

print(climb_stair(3))
print(climb_stair(4))
print(climb_stair(10))
