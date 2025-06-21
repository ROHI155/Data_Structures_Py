class Solution(object):
    def isHappy(self, n):
        res = set()

        while n != 1:
            n = sum([int(i)**2 for i in str(n)])

            if n in res:
                return False
            else:
                res.add(n)
        return True
