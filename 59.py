def max_2(*args):
    # print(args) tuple
    max_1 = max(args)
    args = list(args)
    args.remove(max_1)
    return max(args)

print(max_2(2, -3, 5, 7))
# Algorithm 
# 1. max_1 topish
# 2. tupledan max_1 ni o'chirish
# 3. max_2 topish