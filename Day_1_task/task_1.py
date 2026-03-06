with open("task_1.txt","r") as f:
    data = f.read()

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
clean_text = ''
for word in data:
    if word not in punctuation:
        clean_text += word.lower()

words = clean_text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sentance = 0
for word in data:
    if word in ".!?":
        sentance += 1

print(f"Total Words:{len(word_count)}")
print(f"Total Sentences:{sentance}")
print(f"Total characters:{len(data)}")
print("Top Frequent Words:")

i=0
for key, values in word_count.items():
    if i<=4:
        print(f"{key} -> {values}")
        i = i + 1
