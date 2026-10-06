my_info = {'name': 'faith', 'age': 20}
print(my_info['name'])
print(my_info['age'])
my_point = my_info.get('suject')
print(my_point)

my_info['postion'] = 0
my_info['1-position'] = 25
print(my_info)

my_info = {}
my_info['name'] = 'faith'
my_info['age'] = 20
print(my_info)
my_info['name'] = 'joy'
print(my_info)
del my_info['name'] 
print(my_info)

my_friends_favorite_food = {
             'faith:' 'beans',
            'grace:' 'yam',
            'mary:' 'egg',
            'helen:' 'moimoi',
                           }
print(my_friends_favorite_food)

my_friends_favorite_food = {
             'faith': 'beans',
            'grace': 'yam',
            'mary': 'egg',
            'helen': 'moimoi',
                           }
for key,  value in my_friends_favorite_food.items():
    print(f"\nkey:{key}")
    print(f"value:{value}")                          

