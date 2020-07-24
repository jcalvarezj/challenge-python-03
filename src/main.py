# Resolve the problem!!
import re

FILE_NAME = 'encoded.txt'


def run():
    with open(FILE_NAME, encoding = 'utf-8') as input_file:
        contents = input_file.read()
        message = ''.join(re.findall(r'[a-z]', contents))
        print(message)


if __name__ == '__main__':
    run()
