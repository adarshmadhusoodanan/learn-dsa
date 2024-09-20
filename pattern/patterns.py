# solving 22 patterns problems

# tips
# 1. for the outer loop, count the no. of lines
# 2. for the inner loop, focus on the columns and connect with them somehow to the rows
# 3. print them " * " inside the inner for loop
# 4. observe symmetry { optional }

def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()  # Moves to the next line after each row

        '''
        pattern:
                    *****
                    *****
                    *****
                    *****
                    *****
        ''' 
      
def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
        '''
        pattern:
                    *
                    **
                    ***
                    ****
                    *****
        ''' 

def pattern3(n):
    for i in range(n):
        for j in range(1,i+2):
            print(f"{j}", end="")   
        print()
        '''
        pattern:
                1
                12
                123
                1234
                12345
        ''' 

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f"{i}",end="")
        print()
        '''
        pattern:
                1
                22
                333
                4444
                55555
        ''' 

def pattern5(n):
    for i in range(n):
        for j in range(n,i,-1):
            print("*", end="")
        print()
        '''
        pattern:
                *****
                ****
                ***
                **
                *
        '''

def pattern6(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(f"{j}",end="")
        print()
        '''
        pattern:
                12345
                1234
                123
                12
                1
        '''

def pattern7(n):
    for i in range(n):
        #space
        for j in range(n-i-1):
            print(" ", end="")     
        #star
        for j in range(2*i+1):
            print("*",end="")
        #space
        for j in range(n-i-1):
            print(" ", end="")
        print()
        '''
        pattern:
                        *
                       ***
                      *****
                     *******
                    *********
        '''

def pattern8(n):
    for i in range(n):
        #space
        for j in range(i):
            print(" ", end="")     
        #star
        for j in range(2*n-(2*i+1)):
            print("*",end="")
        #space
        for j in range(i):
            print(" ", end="")
        print()
        '''
        pattern:
                    *********
                     *******
                      *****
                       ***
                        *
        '''

def pattern9(n):   
    for i in range(2*n): #0 to 9
        star=i
        if (i>n):      # after the 5 th row
            star=2*n-i    #reduce the star
        for j in range(star):
            print("*",end="")
        print()

        '''
        pattern:
                    *
                    **
                    ***
                    ****
                    *****
                    ****
                    ***
                    **
                    *
        '''

def pattern10(n):
    star=1
    for i in range(n+1):
        
        if (i%2==0):
            star=0
        else:
            star=1
        for j in range(i):
            print(f"{star}",end="")
            star=1-star
        print()
        '''
        pattern:
                1
                01
                101
                0101
                10101
        '''

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    pattern10(n)

