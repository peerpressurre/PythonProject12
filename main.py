#feature/lab_ex1
def mop():
    try:
        text = input('enter text->')
        old = input('enter a word to replace->')
        new = input('enter replacement word ->')

        print(f'New text: {text.replace(old, new)}')
    except Exception as ex:
        print(f'Error: {ex}')
mop()



