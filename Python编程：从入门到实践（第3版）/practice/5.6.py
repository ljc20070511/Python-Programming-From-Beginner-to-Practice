age = int(input())
if age < 2:
    print("婴儿")
elif age < 4:
    print("幼儿")
elif age < 13:
    print("儿童")
elif age < 18:
    print("少年")
elif age < 65:
    print("中青年")
else:
    print("老年")