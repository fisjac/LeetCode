class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(net) < 0: return -1

        l,r = 0,0
        gas = 0
        while r < len(net):
            gas += net[r]
            # print(gas, l, r)
            if gas < 0:
                l = r + 1
                gas = 0
            r += 1
        return l
