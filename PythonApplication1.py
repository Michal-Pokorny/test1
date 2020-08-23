i = 100
num1 = 5
num2 = 3
word1 = 'Agile'
word2= 'Software'
word12 = 'Testing'
while i > 0:
    if i%num1 == 0 and i%num2 == 0:
        print(word12)
    elif i%num1 == 0:
        print(word1)
    elif i%num2 == 0:
        print(word2)
    else:
        print(i)
    i+=-1






