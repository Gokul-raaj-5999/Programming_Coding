def minion_game(string):
    # your code goes here
    vowels='AEIOU'
    ke=0
    st=0
    for i in range(len(string)):
        if string[i] in vowels:
            ke+= (len(string)-i)
        else:
            st += (len(string)-i)
    if ke>st:
        print ("Kevin",ke)
    elif ke<st:
        print ("Stuart",st)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

##########################################################################
"""
INPUT:
    BANANA
OUTPUT:
    Stuart 12
"""
