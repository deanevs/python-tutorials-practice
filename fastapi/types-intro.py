def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name(first: str, last: str):
    full = first.title() + " " + last.title()
    return full


def get_age(name: str, age: int):
    nameage = name + " " + str(age)
    return nameage
