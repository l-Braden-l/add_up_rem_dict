#
#
#


#---Updating---#
fav_alien = {
        'first_name':'Zoltrac',
        'age': 763,
        'Home_Planet': 'Neptune',
        'Color': 'green'
}
print(f"first_name : {fav_alien['first_name']}")
print(f"age : {fav_alien['age']}")
print(f"Home_Planet : {fav_alien['Home_Planet']}")
print(f"Color : {fav_alien['Color']}\n")



#---adding---#

    #--update()--#
fav_alien.update({'Number_of_eyes': 5})

    #--square--#
fav_alien['age'] = 9543



#---Removing---#

    #--del--#
del fav_alien['age']
print(fav_alien)

    #--pop--#
remove_color = fav_alien.pop('Home_Planet')
print(fav_alien)
