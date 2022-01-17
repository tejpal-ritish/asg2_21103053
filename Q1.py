#Q1. wap to perform string operations on a string

inp='Python is a case sensitive language'
print('The input is given as :-',inp,'\n')

#Q1. a)

print('The length of the given string is ',len(inp),'\n')

#Q1. b)

print('The following string reversed would be printed as :-',inp[::-1],'\n')

#Q1. c)

inp2=inp[10:26]
print(inp2,'\n')

#Q1. d)

inp3=inp.replace('a case sensitive','object oriented')
print('Edited string will be printed as :-',inp3,'\n')

#Q1. e)

position=inp.find('a')
print('The index of substring "a" in the given string is',position,'\n')

#Q1. f)

inp4=inp.strip()
print('The input string after removing all the whitespaces becomes :-',inp4)
