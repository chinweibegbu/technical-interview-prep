def isHappy_solution(n: int) -> bool:
    tracker = {}
    num = n
    tracker[num] = 1
    while True:
        nums_squared = [int(x)*int(x) for x in str(num)]
        num = sum(nums_squared)
        if (num == 1):
            return True
        else:
            if num in tracker:
                return False
            else:
                tracker[num] = 1