
vowel = {"a", "e", "i", "o", "u", "y"}

punctuation = {",", ".", "!", "?", ";", ":", "'", " "}
vowels_and_punctuation = vowel.union(punctuation)
#print(vowel)

user_Text = set(input("Please enter your text into the vowel destructionator: ").lower())
#print(user_Text)

destructed_Set = set(user_Text.difference(vowels_and_punctuation))
print(sorted(destructed_Set))

