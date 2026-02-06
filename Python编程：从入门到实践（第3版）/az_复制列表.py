if True:
    my_foods = ['pizza', 'falafel', 'carrot cake']
    # 这是行不通的：
    friend_foods = my_foods
    my_foods.append('cannoli')
    friend_foods.append('ice cream')
    print("My favorite foods are:")
    print(my_foods)
    print("\nMy friend's favorite foods are:")
    print(friend_foods)