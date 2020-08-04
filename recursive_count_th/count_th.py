'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # counter variable
    count = 0
    # base case --> have reached end of word or input has length of 0
    if len(word) <= 1:
        return 0
    # check first two indexes and increment count if 'th' found
    if word[0] == 't' and word[1] == 'h':
        count += 1
    
    return count_th(word[1:]) + count
