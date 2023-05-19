class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0: return res
        s, e = nums[0], nums[0]

        for num in nums:
            # options are:
            # it's the end of nums -> check if in part of sequence
            # it's in sequence -> update end
            # it's not in sequence -> add previous sequence and update s and e to new
            if num > e + 1: # append case
                if s != e: res.append(f'{s}->{e}')
                else: res.append(f'{e}')
                s, e = num, num
                if e == nums[-1]: res.append(f'{e}')
            else: # skip case
                e = num
                if e == nums[-1]:
                    if s != e:
                        res.append(f'{s}->{e}')
                    else:
                        res.append(f'{e}')
        return res
