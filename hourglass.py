


def HourGlass(arr):
    level = 1
    totalSum = 0
    finalsum = 0 
    while(level <= len(arr) - 2 ):
        for j in range(len(arr[0]) - 2):
                
            totalSum =( arr[level][j] +  
                        arr[level-1][j-1] + arr[level-1][j] + arr[level-1][j+1]+
                        arr[level+1][j-1] + arr[level+1][j] + arr[level+1][j+1])
            if(totalSum > finalsum):
                finalsum = totalSum
            print(totalSum)    
        level += 1
        
    print(finalsum)
            
arr = [
    
[-1 ,-1 , 0 ,-9 ,-2 ,-2],
[-2 ,-1 ,-6 ,-8 ,-2 ,-5],
[-1 ,-1 ,-1 ,-2 ,-3 ,-4],
[-1 ,-9 ,-2 ,-4 ,-4 ,-5],
[-7 ,-3 ,-3 ,-2 ,-9 ,-9],
[-1 ,-3 ,-1 ,-2 ,-4 ,-5]

]            
HourGlass(arr)            