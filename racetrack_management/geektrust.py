from sys import argv

from src.factories.racetrack_management_command_factory import RaceTrackManagementCommandFactory


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
        RaceTrackManagementCommandFactory.get_instance(command).execute(*args)


if __name__ == "__main__":
    main()
