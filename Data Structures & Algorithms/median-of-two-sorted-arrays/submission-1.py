class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #identify the smaller list
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        #compute the median position
        n, m = len(nums1), len(nums2)
        half = (n + m) // 2

        #figure out how many spots are "allocated" from the smaller array through binary search (i.e starting from the middle of the smaller array)
        left, right = 0, n

        while left <= right:
            smaller_array_partition_count = (left + right) // 2
            remaining_partition_count = half - smaller_array_partition_count
            
            #check if right bound of smaller array's left partition is <= left bound of bigger array's right partition
            smaller_array_left_partition_right_bound_value = nums1[smaller_array_partition_count - 1] if smaller_array_partition_count > 0 else float("-inf")
            bigger_array_right_partition_left_bound_value = nums2[remaining_partition_count] if remaining_partition_count < m else float("inf")

            #check if right bound of bigger array's left partition is <= left bound of smaller array's right partition
            bigger_array_left_partition_right_bound_value = nums2[remaining_partition_count - 1] if remaining_partition_count > 0 else float("-inf")
            smaller_array_right_partition_left_bound_value = nums1[smaller_array_partition_count] if smaller_array_partition_count < n else float("inf")

            if smaller_array_left_partition_right_bound_value > bigger_array_right_partition_left_bound_value:
                #we have too many values from smaller array
                right = smaller_array_partition_count - 1

            elif bigger_array_left_partition_right_bound_value > smaller_array_right_partition_left_bound_value:
                #we have too few values from smaller array
                left = smaller_array_partition_count + 1
            
            else: #we have the correct partition
                if ((n + m) % 2):
                    #if odd
                    return min(
                        smaller_array_right_partition_left_bound_value,
                        bigger_array_right_partition_left_bound_value
                    )
                else:
                    #if even
                    return (
                        max(
                            smaller_array_left_partition_right_bound_value,
                            bigger_array_left_partition_right_bound_value
                        )
                        +
                        min(
                            smaller_array_right_partition_left_bound_value,
                            bigger_array_right_partition_left_bound_value
                        )
                    ) / 2