new_str = "Count = " + str(42)
print (new_str)

str1 = "Hello"
str2 = "Hello"
if str1 == str2:
    print ("strings are equal")
else:
    print ("strings are not equal")

str3 = 'the cat sat on the mat'
result = ('cat' in str3)
if result == True:
    print ('its there')

print ('Position = ' + str(str3.find('mat')))

print ()
#problem 1-4 slice notation
print ( str3[4:7]) # cat
print (str3[8:])
print (str3[7:])

#problem 1-5 replace
str4 = "Here are a string"
corrected_str = str4[:5] + 'is' + str4[8:]
print (corrected_str)
corrected_str1 = str4.replace('are','is',1)
print ('cor2 = ' + corrected_str1)
print ()

#problem 1-6 reversing string
str5 = "Hello World!"
str6 = str5[::-1]
print (str6)

#problem 1-7 Trimming
print ()
str8 = "Hello World!   "
print (str8,end='')
print (str8)
str9 = str8.strip()
print (str9,end='')
print (str9)

#problem 1-8 Changing Case
print ()
str10 = str8.lower()
print (str10)
str11 = str8.upper()
print (str11)

#problem 1-9 Converting to Numbers
print ()
hex1 = int('ff',16)
print (hex1)

#problem 1-10 Iterating over a string
print ()
str12 = '012345'
cnt  = len(str12)
for i in range(cnt):
    print (str12[i],end='')
    if  i != (cnt - 1) :
        print (' and ',end='')
    else:
        print()

#problem 1-11 Stats
print ()
str21 = "Hello world"
print ('len = ', len(str21))
print ('min = ', min(str21))
print ('max = ', max(str21))
print ('count = ',str21.count('l'))

#problem 1-13 Translation
print()
translate_table = str21.maketrans("Helo","Lory")
print (str21.translate(translate_table))

# Count = 42
# strings are equal
# its there
# Position = 19
#
# cat
# sat on the mat
#  sat on the mat
# Here is a string
# cor2 = Here is a string
#
# !dlroW olleH
#
# Hello World!   Hello World!
# Hello World!Hello World!
#
# hello world!
# HELLO WORLD!
#
# 255
#
# 0 and 1 and 2 and 3 and 4 and 5
#
# len =  11
# min =
# max =  w
# count =  3
#
# Lorry wyrrd
