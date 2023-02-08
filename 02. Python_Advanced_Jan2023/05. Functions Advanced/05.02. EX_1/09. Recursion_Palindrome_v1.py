def palindrome(word, left_index, right_index=-1):
    if abs(left_index) == len(word)//2:
        return f"{word} is a palindrome"
    if word[left_index] != word[right_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, left_index+1, right_index-1)

#############################
# Test_Code_1:
print(palindrome("abcba", 0))
# -----------------------------
# Output_1:
# abcba is a palindrome
# #############################
# Test_Code_2:
print(palindrome("peter", 0))
# -----------------------------
# Output_2:
# peter is not a palindrome
#############################
