import numpy as np 
  
# Get the size m and n  
m , n = 4, 4        
  
# Function to calculate sum of each row  
def row_sum(arr) : 
  
    sum = 0
  
    print("\nFinding Sum of each row:\n") 
  
    # finding the row sum  
    for i in range(4) : 
        for j in range(4) : 
  
            # Add the element  
            sum += arr[i][j] 
  
        # Print the row sum  
        print("Sum of the row",i,"=",sum) 
  
        # Reset the sum  
        sum = 0
  
  
# Function to calculate sum of each column  
def column_sum(arr) : 
  
    sum = 0
  
    print("\nFinding Sum of each column:\n") 
  
    # finding the column sum  
    for i in range(4) : 
        for j in range(4) : 
  
            # Add the element  
            sum += arr[j][i] 
  
        # Print the column sum 
        print("Sum of the column",i,"=",sum) 
  
        # Reset the sum  
        sum = 0
  
          
  
# Driver code      
if __name__ == "__main__" : 
  
    arr = np.zeros((4, 4)) 
  
    # Get the matrix elements  
    x = 1
      
    for i in range(m) : 
        for j in range(n) : 
            arr[i][j] = x 
  
            x += 1
                  
    # Get each row sum  
    row_sum(arr) 
  
    # Get each column sum  
    column_sum(arr) 
  
# This code is contributed by  
# ANKITRAI1 