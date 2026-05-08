class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        left, right = 0, n
        half = (n + m) // 2

        while left <= right:
            nums1_partition_count = (left + right) // 2
            nums2_partition_count = half - nums1_partition_count

            #computer 4 values (2 comparisons) - nums1_left_partition_right_bound, nums1_right_side, nums2_left_partition_right_bound, nums2_right_side

            # 1 - make sure nums1_left_partition_right_bound <= nums2_right_side
            nums1_left_partition_right_bound = nums1[nums1_partition_count - 1] if nums1_partition_count > 0 else float("-inf")
            nums2_right_side = nums2[nums2_partition_count] if nums2_partition_count < m else float("inf")
            
            #2 - make sure nums2_left_partition_right_bound <= nums1_right_side
            nums2_left_partition_right_bound = nums2[nums2_partition_count - 1] if nums2_partition_count > 0 else float("-inf")
            nums1_right_side = nums1[nums1_partition_count] if nums1_partition_count < n else float("inf")
            
            if nums1_left_partition_right_bound > nums2_right_side: # we have too many value from nums1, decrease
                right = nums1_partition_count - 1

            elif nums2_left_partition_right_bound > nums1_right_side: # we have too few value from nums1, increase
                left = nums1_partition_count + 1
            
            else:
                if ((n + m) % 2): #odd 
                    return min(nums1_right_side, nums2_right_side)
                else: #even
                    return (max(nums1_left_partition_right_bound, nums2_left_partition_right_bound) + min(nums1_right_side, nums2_right_side)) / 2 