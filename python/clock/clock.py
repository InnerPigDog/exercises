class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = self.time_rollover(hour, minute)

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

    def time_rollover(self, hour, minute):
        # rolls over minutes > 59 to hours; 24 hours format
        hour = (hour + minute // 60) % 24   
        minute = minute % 60
        return (hour, minute)