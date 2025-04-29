text = input("Text: ").lower()

letters = 0
words = 1
sentences = 0

for i in text:
    if i != ' ':
        if i >= 'a' and i <= 'z':
            letters += 1
    if i == ' ':
        words += 1
    if i == '.' or i == '!' or i == '?':
        sentences += 1

L = float(letters / words) * 100
S = float(sentences / words * 100)

index = 0.0588 * L - 0.296 * S - 15.8
rIndex = int(round(index))

print(rIndex)
if rIndex < 1:
    print("Before Grade 1")
elif rIndex > 16:
    print("Grade 16+")
else:
    print(f"Grade {rIndex}")
