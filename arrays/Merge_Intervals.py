
# Not correct, needs sort upfront

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        for interval in intervals:
            print('-----',interval, '-----')
            [current_start, current_end] = interval
            if len(stack) == 0:
                print('adding', interval)
                stack.append(interval)
                print(stack)
            else:
                merged = False
                for i in range(len(stack)):
                    [previous_start, previous_end] = stack[i]
                    if current_start <= previous_end and current_end >= previous_start:  # if overlap
                        stack[i] = [min(current_start, previous_start), max(current_end, previous_end)]
                        print('merging', interval)
                        print(stack)
                        merged = True
                        break
                if merged == False:
                    print('adding', interval)
                    stack.append(interval)
                    print(stack)
        return stack
