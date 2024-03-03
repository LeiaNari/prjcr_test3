from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return li[i], li[j]


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen = set()
    for num in li:
        complement = target - num
        if complement in seen:
            return complement, num
        seen.add(num)


# Test the functions
assert find_sum(5, [1, 2, 3, 4, 5]) in {(2, 3), (1, 4)}
assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(2, 3), (1, 4)}
