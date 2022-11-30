mod = 1000000009
nums = {}


def ans(n):
    if n < 50000000:
        if n in nums:
            return nums[n]
        if n == 0:
            nums[n] = 1
            return nums[n]
        if n == 1:
            nums[n] = 10
            return nums[n]

        x = ans(n // 2)
        y = ans(n // 2 - 1)

        if n % 2 == 0:
            nums[n] = ((x * x) - (y * y)) % mod
        else:
            z = ans(n // 2 + 1)
            nums[n] = (x * (z - y)) % mod

        return nums[n]
    else:
        if n in nums1:
            return nums1[n]

        x1 = ans(n // 2)
        y1 = ans(n // 2 - 1)

        if n % 2 == 0:
            nums1[n] = ((x1 * x1) - (y1 * y1)) % mod
        else:
            z1 = ans(n // 2 + 1)
            nums1[n] = (x1 * (z1 - y1)) % mod

        return nums1[n]


for _ in range(int(input())):
    n = int(input())
    nums1 = {}
    print(ans(n))
