'''
Time Complexity : O(m + n*logm)
                  m ---> length of source
                  n ---> lenght of target
Space Complexity: 0(1)
Run On LeetCode: Yes
'''
import bisect

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        # add the words into dictionary
        sourceDict = {}
        
        for i in range(0,len(source)):
            if source[i] not in sourceDict:
                sourceDict[source[i]] = [i]
            else:
                sourceDict[source[i]].append(i)
        
        # print('Source Dict is:\t',sourceDict)
        
        # source ptr
        sp = 0
        
        # target ptr
        tp = 0
        
        # return the result
        count = 0
        
        while tp != len(target):
            
            if target[tp] not in sourceDict:
                return -1
            
            # binary search to find the char in source
            charList = sourceDict[target[tp]]
            index = bisect.bisect_left(charList,sp)
            
            if index == len(charList):
                # out of bounds, set index to min value i.e. 0th index of charList
                index = 0
                # update the count
                count += 1
            
            sp = charList[index]+1
            tp += 1
            
        '''end of while loop'''
        
        if tp == len(target):
            count += 1
        
        return count
        