def bubble(words):
    n = len(words)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]

words = ["banana", "apple", "cherry", "date"]
bubble(words)
print(words)
