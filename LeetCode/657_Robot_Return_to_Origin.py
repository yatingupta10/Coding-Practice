class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U=moves.count('U')
        L=moves.count('L')
        D=moves.count('D')
        R=moves.count('R')
        
        axis1=U-D
        axis2=R-L
        
        output=True
        
        if axis1 != 0:
            output=False
        if axis2 != 0:
            output=False
        
        return(output)