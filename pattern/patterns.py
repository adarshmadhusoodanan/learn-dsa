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
        pattern1:
                    *****
                    *****
                    *****
                    *****
                    *****
        ''' 
      


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    pattern1(n)

