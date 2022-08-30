# Chef rented a car for a day.

#Usually, the cost of the car is Rs 1010 per km. However, since Chef has booked the car for the whole day, he needs to pay for at least 300300 kms even if the car runs less than 300300 kms.

#If the car ran XX kms, determine the cost Chef needs to pay.

t = int(input())
for i in range(t):
    s = int(input())
    if(s>=300):
        print(s*10)
    else:
        print(300*10)
