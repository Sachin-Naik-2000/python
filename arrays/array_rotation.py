here we will rotate the elements in the array

n=int(input("enter the no fo rotation : "))

list=[1,2,3,4,5,6,7]

print("before rotation: {}".format(list))

print("after rotation: {}".format(list[n:]+list[:n]))     #n for clock wise rotation and -n for anticlock wise rotation
