import time
timestamp = int(time.strftime('%H'))
print(timestamp)
if(timestamp <= 12):
    print("Good Morning")
elif(timestamp <= 15):
    print("Good Afternoon")
elif(timestamp <= 18):
    print("Good Evening")
else:
    print("Good Night")

    # elif(timestamp < 3)
    #     print("ge")
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)