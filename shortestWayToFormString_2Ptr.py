'''
Time Complexity : O(mn)
                  m ---> length of source
                  n ---> lenght of target
Space Complexity: 0(1)
Run On LeetCode: Yes
'''
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        # source ptr
        sp = 0
        
        # target ptr
        tp = 0
        
        # previous position 
        pp = 0
        
        # return the result
        count = 0
        while tp != len(target):
            if sp < len(source) and source[sp] == target[tp]:
                sp += 1
                tp += 1
            elif sp < len(source) and source[sp] != target[tp]:
                sp += 1
            elif sp == len(source) and pp != tp:
                count += 1
                sp = 0
                pp = tp
            else:
                return -1
        
        if tp == len(target):
            count += 1
        
        return count