from sys import argv
from src.facade import PortfolioOverlapFacade
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
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    for line in Lines:
        command, *args = line.split()
        if command == "CURRENT_PORTFOLIO":
            facade.current_portfolio(args)
        elif command == "CALCULATE_OVERLAP":
            facade.calculate_overlap(*args)
        else:
            facade.add_stock(args[0], " ".join(args[1:]))


if __name__ == "__main__":
    main()
