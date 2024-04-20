#import this
seconds_past_midnight = 63252
hours = seconds_past_midnight // 3600
minutes = (seconds_past_midnight % 3600) // 60
seconds = seconds_past_midnight % 12
time_str = str(hours) + ':' + str(minutes) + ':' + str(seconds)
print(time_str)

