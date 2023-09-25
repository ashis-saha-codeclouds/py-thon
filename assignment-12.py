para = input("Please enter the paragraph: ")
if len(para) > 1:
    searchingWord = input("Please enter the word that you want to search: ")
    replaceWord = input("Please enter the word that you want to replace with the searching word: ")
    countTheChar = str(para.count(searchingWord))
    print(searchingWord + " is exist in " + countTheChar + " places in the entered para")
    print("Updated Paragraph \n", para.replace(searchingWord, replaceWord))
else:
    print("Paragraph should not be blank!")


