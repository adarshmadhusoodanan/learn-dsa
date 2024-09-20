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

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    pattern6(n)

