#feature/lab_ex1
def mop():
    try:
        text = input('enter text->')
        word = input('enter a word to find->')

        print(f'Number of particular symbol in text: {text.count(word)}')
    except Exception as ex:
        print(f'Error: {ex}')
mop(



