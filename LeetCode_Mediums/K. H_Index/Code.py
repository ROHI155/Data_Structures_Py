class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) # Sort the list in the descending order.

        for index,citation in enumerate(citations): # Iterate through each element in the sorted list.
            if index>= citation: # Check if the index is lesser then the citation value.
                return index # Then return the H-Index.
        return len(citations) # Else return the length of the citation.