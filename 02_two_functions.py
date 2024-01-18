def get_greetings():
    greetings = 'Hello'
    greetings = update_greetings(greetings)
    return greetings + '!'


def update_greetings(local_greetings):
    return local_greetings + 'world'


if __name__ == '__main__':
    result = get_greetings()
    print(result)
