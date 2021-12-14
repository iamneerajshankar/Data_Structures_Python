class ArrayRotate:
    
    def using_temp_variable(self, arr, lengthArray, rotateFactor):
        for i in range(rotateFactor):
            ArrayRotate().roatate_by_one(arr, lengthArray)
            
            
    def roatate_by_one(self, arr, lengthArray):
        temp = arr[0]
        for i in range(lengthArray-1):
            arr[i] = arr[i+1]
            
        arr[lengthArray-1] = temp
        
        #print array after rotating by roatate_by_one
        print("The array after rotation by one")
        for i in range(lengthArray):
            print(arr[i])
    

# driver code 

# creating list with integers
myArr = [1,2,3,4,5,6,7]


#creating object of the class ArrayRotate
instRotate = ArrayRotate()
n = len(myArr)
d = 2

#print array before operation 
print("\n The array before rotation")
for i in range(n):
    print(myArr[i])
instRotate.using_temp_variable(myArr, n, d)