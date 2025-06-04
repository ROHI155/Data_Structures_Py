class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas) # Assigning the n as length of gas.
        current_tank = 0 # Assigning the current and total and final as 0.
        total_tank = 0
        final = 0
        for i in range (n): # Loop to iterate through each element in the gas and cost.
            current_tank += gas[i]-cost[i] # Sum the difference of gas and cost for both the current and total.
            total_tank += gas[i]-cost[i]

            if current_tank < 0: # Check if the current is lesser than 0 means,
                final = i + 1 # Aassign the final as i + 1.
                current_tank = 0 # Then empty the current tank
        return final if total_tank >= 0 else -1 # Return if final if the total is greater then or equal to 0.