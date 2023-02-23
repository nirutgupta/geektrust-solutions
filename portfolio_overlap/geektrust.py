from sys import argv
from src.facade import PortfolioOverlapFacade

EXPECTED_ARGS = 2
facade = PortfolioOverlapFacade()


def main():
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    if len(argv) != EXPECTED_ARGS:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    for line in Lines:
        command, *args = line.split()
        getattr(facade, command.lower())(*args)


if __name__ == "__main__":
    main()
