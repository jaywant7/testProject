score = 200
player_name = "Jaywant"
list = ['apple','banana','green apple']
print("score", score)
print("player name is:", player_name)
print("items", list)

# Value assigment #

a = 10
b = 20
sum = a + b
print(sum)

x,y,z = 10, 10.5, "Hey"
print(x)
print(y)
print(z)

first_name = "Jaywant"
last_name = "Taywade"
print("Full Name is", first_name + " "+ last_name)

# Globle Variable #
x = "global"
def function():
    print("X inside", x)
function()
print("X outside:", x)