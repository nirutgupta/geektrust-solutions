class StationSummary:
    @staticmethod
    def print_summary(station, collection, discount, passenger_to_visit):
        print(f"TOTAL_COLLECTION {station.upper()} {collection} {discount}")
        print("PASSENGER_TYPE_SUMMARY")

        res = [(passenger, passenger_to_visit[passenger]) for passenger in passenger_to_visit]
        res.sort(key=lambda x: (-x[1], x[0]))
        for each in res:
            print(f"{each[0]}\t{each[1]}")
