class Viewer:
    @staticmethod
    def print_renewal_details(renewal_reminders, renewal_amount):
        for renewal_reminder in renewal_reminders:
            print(f"RENEWAL_REMINDER\t{renewal_reminder[0].name}\t{renewal_reminder[1]}")
        print(f"RENEWAL_AMOUNT\t{renewal_amount}")

    @staticmethod
    def print_string(input_string):
        print(input_string)
