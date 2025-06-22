low = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))

while (low <= upper):
    if (low % 2 != 0):
        print(low)

    low += 1
