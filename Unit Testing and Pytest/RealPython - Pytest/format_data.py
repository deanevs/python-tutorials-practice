

def format_data_for_display(people):
    formated_list = []
    for person in people:
        formated_list.append(person["given_name"] + " " +
                             person["family_name"] + ": " +
                             person["title"]
        )
    return formated_list


def format_data_for_excel(people):
    s = "given, family, title, "
    for person in people:
        s += person["given_name"] + ", "
        s += person["family_name"] + ", "
        s += person["title"] + ", "
    return s