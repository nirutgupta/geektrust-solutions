from sys import argv
from src.services.subscriptions import SubscriptionsService


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
    subscription_service = SubscriptionsService()
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    for line in Lines:
        command, *args = line.split()
        if command == "START_SUBSCRIPTION":
            subscription_service.start_subscription(*args)
        elif command == "ADD_SUBSCRIPTION":
            subscription_service.add_subscription(*args)
        elif command == "ADD_TOPUP":
            subscription_service.add_topup(*args)
        else:
            subscription_service.print_renewal_details()

    
if __name__ == "__main__":
    main()