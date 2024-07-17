calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string


def is_contains(string, list_to_search):
    count_calls()
    list_ = [words.lower() for words in list_to_search]
    if string.lower() in list_:
        return True
    else:
        return False


print(string_info('Soundmaker'))
print(string_info('Equalization'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('Motorcycle', ['moto', 'cycle', 'moTOR']))
print(calls)
