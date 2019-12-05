import time
longestTime = 0
timeList = []
while True:
    wrongWords = []
    text = "This is a line of text that you can type out if you want to lol lol"
    print(text)
    start = time.time()
    userInput = input()

    for word in text.split(' '):
        if word in userInput:
            continue
        else:
            wrongWords.append(word)

    end = time.time()
    if len(wrongWords) > 0:
        print(f"You got these words wrong")
        print(wrongWords)
    textLength = len(text.split(' '))
    average = round((len(userInput) / 5) / (end - start) * 60, 2)
    timeList.append(average)
    for times in timeList:
        if longestTime < times:
            longestTime = times
    print(
        f"it took you {round(end - start, 2)}s to complete. So {average}words per minute")
    print(f"fastest time {longestTime}")
# life = 3
# text = "This is some text for you to copy"
# for word in text.split(' '):
#     if life > 0:

#         print(word)
#         userInput = input()
#         if userInput == word:
#             continue
#         else:
#             life -= 1
#     else:
#         break
