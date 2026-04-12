##1186. Maximum Subarray Sum with One Deletion
class Solution:
    def maximumSum(self, arr):
        no_del = arr[0]
        one_del = 0
        ans = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]

            one_del = max(no_del, one_del + x)
            no_del = max(x, no_del + x)

            ans = max(ans, no_del, one_del)

        return ans
    
#test 
#     
