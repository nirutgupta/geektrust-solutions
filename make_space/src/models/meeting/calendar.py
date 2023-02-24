class MeetingCalendar:
    def __init__(self):
        self._events = []

    def add_event(self, time_range):
        self._events.append(time_range)

    def get_events(self):
        return self._events

    def add_events(self, time_ranges):
        self._events.extend(time_ranges)
