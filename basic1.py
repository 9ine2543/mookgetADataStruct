h,m = input('enter : ').split()
h,m = int(h) + int(int(m) / 60), int(m) % 60
price = 0
if(h >= 0 and m >= 0):
    if(m > 0):
        price = h * 30
    else:
        price = (h-1) * 30
    print(price)
else:
    print('hour, minute can\'t be negative')