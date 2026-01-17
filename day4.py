# # day 4 challenge
# Palindrome Check. Write a function that takes a string and returns `True` if it’s a palindrome (reads same forwards/backwards), ignoring case/spaces/punctuation. Use two pointers (start/end moving inward).



def is_palendrome(text):
    text = text.replace(' ', '').lower()
    forward = text
    backward = text[::-1]
    return forward == backward


print(is_palendrome(input('Enter a phrase: ')))

# AI Feedback
# Strengths
# 	•	Proper preprocessing: Removing spaces and converting to lowercase handles the key edge cases effectively.
# 	•	Clear logic: Direct forward/backward comparison is simple and readable.
# 	•	Interactive input makes it practical for testing.
# Areas to Improve
# 	•	Spelling: “palendrome” should be “palindrome” (minor but good for portfolio).
# 	•	Built-in slice: Using `text::-1` skips the two-pointer practice goal. Try manual reversal or pointers:


