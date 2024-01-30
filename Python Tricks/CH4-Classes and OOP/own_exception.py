

class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


if __name__ == '__main__':
    validate('dean')

