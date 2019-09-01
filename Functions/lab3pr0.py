
def heartbeats(age):
    beats_per_minute = 72
    beats_per_hour = beats_per_minute * 60
    beats_per_day = beats_per_hour * 24
    beats_per_year = beats_per_day * 365
    beats_per_life = beats_per_year * age
    return beats_per_life

def yawns(age):
    yawns_per_day = 5
    yawns_per_year = yawns_per_day * 365
    yawns_per_life = yawns_per_year * age
    return yawns_per_life

age = int(input("Enter your age in years: "))
print(heartbeats(age), "heartbeats and", yawns(age), "yawns so far")
