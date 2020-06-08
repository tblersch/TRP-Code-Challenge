import CodeChallenge as cc

sentence = ""
word = cc.Word()
while sentence != "EXIT":
    sentence = input("Enter a sentence (enter EXIT to exit): ")
    word = cc.FindLongestWord(sentence)
    print("Longest word is: " + word.word + " with length: " + str(word.length))
    word = cc.FindShortestWord(sentence)
    print("Shortest word is: " + word.word + " with length: " + str(word.length))
    