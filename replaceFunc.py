placesMas = []
n = int(input('amount of files:\n'))
for k in range(n):
    placesMas.append(input('file {}\n'.format(k + 1)))


a = input('string (type in format: old line-new line)\n').split('-')
wordInput = a[0]
newWordInput = a[1]


def replace(places, word, newWord):
    try:
        for i in places:
            with open(i, 'r') as file:
                oldData = file.read()

            new_data = oldData.replace(word, newWord)

            with open(i, 'w') as file1:
                file1.write(new_data)
    except BaseException:
        print('Failed')
    else:
        print('Success')


replace(placesMas, wordInput, newWordInput)
