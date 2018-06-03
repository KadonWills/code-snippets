#S = {x² : x in {0 ... 9}}
#V = (1, 2, 4, 8, ..., 2¹²)
#M = {x | x in S and x even}

noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes   = [x for x in range(2, 50) if x not in noprimes]
words    = 'The quick brown fox jumps over the lazy dog'.split()

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)

stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)
for i in stuff:
    print(i)

# http://www.secnetix.de/olli/Python/lambda_functions.hawk
# Used in python: filter,map,reduce functions
# lambda <param>[,<param>]: <expression>

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print (filter(lambda x: x % 3 == 0, foo))
#[18, 9, 24, 12, 27]

print (map(lambda x: x * 2 + 10, foo))
#[14, 46, 28, 54, 44, 58, 26, 34, 64]

# reduce is removed in python 3
# print (reduce(lambda x, y: x + y, foo))
#139