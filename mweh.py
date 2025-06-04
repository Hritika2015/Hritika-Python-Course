def match_words(words):
    ctr = 0
    lst = []
    for word in words:
      if len(word) > 1 and word[0] == word[-1]:
         ctr += 1
         lst.append(word)
    print(" Since you go to school, why not firurge THIS question to answer that question with the same question you have right now because that question that you sloved with help you with THIS question. Make sure to compelte these 2 question 1 is gonna be sloved for YOU.\n ", lst)

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("MAYBE you can slove this one out too! Jt words having first and last letter same:", count)
print(" If you actually sloved these questions.... who are you?...") 