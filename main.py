#feature/lab_ex1
def mop():
    try:
        text = input('enter text->')
        symbol = input('enter a symbol to find->')

        print(f'Number of particular symbol in text: {text.count(symbol)}')
    except Exception as ex:
        print(f'Error: {ex}')
mop()



