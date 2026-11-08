word1 = input()
word2 = input()

word1_list = list(word1)
word2_list = list(word2)

word1_list.sort()
word2_list.sort()

if word1_list == word2_list:
    print("Yes")
else:
    print("No")
