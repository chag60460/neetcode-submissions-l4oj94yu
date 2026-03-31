class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen_set = defaultdict(int)

        for i in range(len(numbers)):
            complement = target - numbers[i]

            if complement in seen_set.keys():
                return [min(i+1, seen_set[complement]), max(i+1, seen_set[complement])]
            else:
                seen_set[numbers[i]] = i + 1