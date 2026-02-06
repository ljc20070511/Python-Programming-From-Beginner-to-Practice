嘉宾名单 = ["Li li" , "Xi xi" , "Bei bei" , "An na"]
嘉宾名单.pop()
嘉宾名单.append("Bi ly")
嘉宾名单.append("An na")
嘉宾名单.append("Hua hua")
嘉宾名单.append("Ji ba")
print(嘉宾名单)
嘉宾名单.pop()
for i in range(4):
    name = 嘉宾名单.pop()
    print(f"Sorry,{name}.")
for i in 嘉宾名单:
    print(f"{i},you are in.")
print(f"I have {len(嘉宾名单)} friends.")
for i in range(2):
    del 嘉宾名单[0]
print(嘉宾名单)

