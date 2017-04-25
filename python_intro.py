# print
print('Hello, Django girls!')


# if only
if 3 > 2:
    print('It works!')


# if else
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')


# if elif else
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')


# if many-elif else
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")


# def-basic
#def hi():
#   print('Hi there!')
#   print('How are you?')
#
#hi()


# def-param
#def hi(name):
#    if name == 'Ola':
#        print('Hi Ola!')
#    elif name == 'Sonja':
#        print('Hi Sonja!')
#    else:
#        print('Hi anonymous!')
#
#hi("Ola")


# def-final
def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")


# loop
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
