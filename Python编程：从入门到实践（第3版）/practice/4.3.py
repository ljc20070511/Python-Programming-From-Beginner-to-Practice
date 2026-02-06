numbered = []

for number in range(1,21):
    print(number)
for number in range(1,21,2):
    print(number)
for number in range(3,30,3):
    print(number)
numbers = [1**3,2**3,3**3,4**3,5**3,6**3,7**3,8**3,9**3,10**3]
for number in numbers:
    print(number)
    numbered.append(number)

print(numbered)