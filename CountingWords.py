intro=input("enter your intro :")
#print(intro)
charactercount=0
wordcount=1
for i in intro :
    charactercount += 1
    if(i==' '):
        wordcount += 1

print('wordcount :' + str(wordcount))
print('charactercount :' + str(charactercount))