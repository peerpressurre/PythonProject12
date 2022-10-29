#feature/lab_ex1 rstring = str[::-1]
def rev():
    try:
        str = input('enter string->')

        print(str[::-1])
    except Exception as ex:
        print(f'Error: {ex}')
print(rev())
