def match_word(words):
    char=0
    lst=[]
    for word in words:
        if len(word) > 1 and word[0]==word[-1]:
            char=char+1
            lst.append(word)
    print("The first and the last characters are the same",*lst)
    return char
c=match_word(["abc","12","SOS","40","aba","ada","asa"])
print("The last character and the last characters are the same",c)
