import os


def driver():
    test_path = 'C:\\Users\\212628255\\Documents\\Knowledge'
    disk_usage(test_path)
    # print(os.listdir(test_path))


def disk_usage(path):
    """Return the number of bytes used by file/folder and any descendants."""
    total = os.path.getsize(path)
    # only recurse if a directory
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<12}'.format(total), path)
    return total


if __name__ == '__main__':
    driver()
