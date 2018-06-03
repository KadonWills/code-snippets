#from termcolor import colored
#print(colored('hello', 'red'), colored('world', 'green'))
class colors:
    RED       = '\033[91m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    BLUE      = '\033[94m'
    PURPLE    = '\033[95m'
    CYAN      = '\033[96m'
    PINK      = '\033[31m'
    BROWN     = '\033[33m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    INVERT    = '\033[7m'
    ENDCOLOR  = '\033[0m'

print(colors.BLUE,'BLUE')
print(colors.GREEN,'GREEN')
print(colors.ENDCOLOR,'NORMAL')
print ()

#for i in range(0, 10):
#    print('\033[9' + str(i) + 'm', i, "test", '\033[0m')
#
for i in range(0,10):
    for j in range(0,10):
        print('\033['+str(j)+str(i)+'m',"j=",j,"i=",i, "test", '\033[0m')

print('\033[31m','test')
print('\033[41m','test')
print('\033[32m','test')
print('\033[42m','test')
print('\033[33m','test')
print('\033[43m','test')

print('\033[34m','test')
print('\033[44m','test')

print('\033[35m','test')
print('\033[45m','test')

print('\033[36m','test')
print('\033[46m','test')

print('\033[0m','test')
print('\033[07m','test')

print('\033[37m','test')
print('\033[47m','test')


