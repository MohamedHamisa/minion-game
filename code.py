def minion_game(string):
    s=len(string)
    vowel = 0
    consonant = 0
     
    for i in range(s):
        if string[i] in 'AEIOU':
           vowel+=(s-i)
        else:
           consonant+=(s-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')

'''
When i = 0, character at string[i] is a consonant (as ‘BANANA’[0] = ‘B’) and we increment consonant by (s-i) which equals to 6 as here s = 6 and i = 0, We do this because starting from ‘B’ there are six possible words (or substrings) that can be formed. 
[‘B’, ‘BA’, ‘BAN’, ‘BANA’, ‘BANAN’, ‘BANANA’]. On subsequent iterations when string[i] is a consonant at indices 2 and 4, we add additional substrings or the same substrings with additional instances.
Subsequently after the execution of the above for loop, if vowel is less than consonant we print Stuart along with value of consonant and else if vowel is greater than consonant we print Kevin along with the value of vowel, and if both are equal we print ‘Draw’.
'''


