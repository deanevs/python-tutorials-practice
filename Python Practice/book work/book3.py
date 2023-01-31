import itertools

#problem 3-1 Iterator
my_list = [1,2,3,4]
new_iter = iter(my_list)
print (next(new_iter))
print (next(new_iter))
print (next(new_iter))
print (next(new_iter))

#problem 3-2
pets = ['dog','cat','mouse','rabbit']
pet_enum = enumerate(pets)
print (next(pet_enum))
pet_list = list(enumerate(pets))
print (pet_list)

#problem 3-3 Filtering an iterator
odd_nums = filter(lambda x:x%2,range(10))
odd_list = list(odd_nums)
print (odd_list)

#problem 3-4 Iterating over a file
file1 = open('test.csv')
for line in file1:
    print (line,end='')

#problem Iterating with no it
def squares(value=0):
    while True:
        value = value + 1
        print ('Value inside = ',value)
        yield (value-1)*(value-1)

generator = squares()
while True:
    result = next(generator)
    if (result > 100):
        break
    print (result)

#problem 3-6 Creating Std Class Iter
accumumlator = itertools.accumulate(range(10))
result = 0
while result < 10:
    result = next(accumumlator)
    print (result)

# Combinations
comb_list = list(itertools.combinations(range(5),3))
for x in comb_list:
    print (x)

a_list = list(itertools.permutations("ABCD",3))
for x in a_list:
    print (x)