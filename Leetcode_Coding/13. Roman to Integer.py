class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        if('IV' in s):
            sum+=4
            s = s.replace('IV', '')
        if('IX' in s):
            sum+=9
            s = s.replace('IX', '')
        if 'XL' in s:
            sum+=40
            s = s.replace('XL','')
        if 'XC' in s :
            sum+=90
            s = s.replace('XC','')
        if 'CD' in s:
            sum+=400
            s = s.replace('CD', '')
        if 'CM' in s:
            sum+=900
            s = s.replace('CM', '')
        for i in s:
            if(i == 'I'):
                sum+=1
            elif(i == 'V'):
                sum+=5
            elif(i == 'X'):
                sum+=10
            elif(i == 'L'):
                sum+=50
            elif(i == 'C'):
                sum+=100
            elif(i == 'D'):
                sum+=500
            elif(i == 'M'):
                sum+=1000
        return(sum)
                
        
