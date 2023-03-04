class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.hours < 10:
            hh = f"0{self.hours}"
        else:
            hh = self.hours
        if self.minutes < 10:
            mm = f"0{self.minutes}"
        else:
            mm = self.minutes
        if self.seconds < 10:
            ss = f"0{self.seconds}"
        else:
            ss = self.seconds
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        if self.seconds + 1 <= Time.max_seconds:
            self.seconds += 1
        else:
            self.seconds = 00
            if self.minutes + 1 <= Time.max_minutes:
                self.minutes += 1
            else:
                self.minutes = 00
                if self.hours + 1 <= Time.max_hours:
                    self.hours += 1
                else:
                    self.hours = 00
        return self.get_time()


# #############################################
# Test_Code_1:
time = Time(9, 30, 59)
print(time.next_second())
# --------------------------------------------
# Output_1:
# 09:31:00
# #############################################
# Test_Code_2:
time = Time(10, 59, 59)
print(time.next_second())
# --------------------------------------------
# Output_2:
# 11:00:00
# #############################################
# Test_Code_3:
time = Time(23, 59, 59)
print(time.next_second())
# --------------------------------------------
# Output_3:
# 00:00:00
# #############################################
