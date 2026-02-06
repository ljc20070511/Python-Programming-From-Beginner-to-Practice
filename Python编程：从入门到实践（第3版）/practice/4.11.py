I = ['pizza', 'falafel', 'carrot cake']
friend = I[:]
friend.append('chicken')
print(f'I like food are : "{I}"')
print(f'My friend like food are : "{friend}"')
for food in friend:
    print(food,"\n")
print("\n")
for food in I:
    print(food,"\n")