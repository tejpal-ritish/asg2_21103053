#Q6. wap to find whether a triangle with sides of measure input by user can be formed or not

side_1=int(input('Enter the measure of the first side -> '))
side_2=int(input('Enter the measure of the second side -> '))
side_3=int(input('Enter the measure of the third side -> '))

if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2 :
   print('Yes')

else:
    print('No')
