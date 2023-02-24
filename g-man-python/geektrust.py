from sys import argv

from src.facade import GManFacade

facade = GManFacade()


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    for line in lines:
        command, *args = line.split()
        func = getattr(facade, command.lower())
        func(*args)


if __name__ == "__main__":
    main()
