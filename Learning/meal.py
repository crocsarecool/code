
def main():
    time = convert(input("What's the time in 24h format?"))
    if 7<= time <=8 : print("breakfast time")
    elif 12 <= time <= 13 : print("lunch time")
    elif 18<= time <= 19 : print ("dinner time")
    else: pass

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes)/60

if __name__ == "__main__":
    main()




