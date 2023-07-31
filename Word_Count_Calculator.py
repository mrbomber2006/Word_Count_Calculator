text = input("Send the text and I will tell you how many words it contains: ").strip()

word_list = text.split()
word_count = len(word_list)

print(f"This text has {word_count} words.")

# word = 1
# while True:
#     for x in word:
#         if x == " ":
#             word += 1
#     break


# print(f"this texts has {word} words")
÷