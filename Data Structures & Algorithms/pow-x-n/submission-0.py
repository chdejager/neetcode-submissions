class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: 
            return 1.0
        if n < 0:
            return 1 / self.myPow(x, -n)

        result = 1
        power = abs(n)

        while power:
            if power & 1:
                result *= x
            x *= x
            power >>= 1

        return result
