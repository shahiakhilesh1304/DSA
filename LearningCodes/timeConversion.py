def timeConversion(s):
    if "PM" in s:
        time = s.split("PM")
        day = "PM"
    elif "AM" in s:
        time = s.split("AM")
        day = "AM"
    t = time[0].split(":")
    if day=="PM":
        t[0] = int(t[0])+12 if int(t[0])!=12 else 12
    else:
        t[0] = "00" if int(t[0])==12 else t[0].zfill(2)
    return ":".join(t)

if __name__ == "__main__":
    s = input("Enter the time in 12 hour format")
    print(timeConversion(s))
    