from sys import argv
from src.service.metro_service import MetroService

ms = MetroService()


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

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        command, *args = line.split()
        if command == "BALANCE":
            ms.init_metro_card(*args)
        elif command == "CHECK_IN":
            ms.check_in(*args)
        elif command == "PRINT_SUMMARY":
            ms.print_summary()
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
