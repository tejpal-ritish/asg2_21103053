#Q4. wap to find the greatest of three numbers input by user

num_1=int(input('Enter the first number -> '))
num_2=int(input('Enter the second number -> '))
num_3=int(input('Enter the third number -> '))

if num_1>num_2 and num_1>num_3:
    print('The greatest of the three numbers entered by you is',num_1)

elif num_2>num_1 and num_2>num_3:
    print('The greatest of the three numbers entered by you is',num_2)

elif num_3>num_2 and num_3>num_1:
    print('The greatest of the three numbers entered by you is',num_3)
