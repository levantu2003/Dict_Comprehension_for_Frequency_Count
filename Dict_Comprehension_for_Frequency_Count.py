from calendar import c


text = input("Input line of text: ")
print(f"Your text: {text}")
print(f"The characters from the text: {set(text)}")
print("The number of these characters are: ", {c: text.count(c) for c in set(text)})