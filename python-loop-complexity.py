import time

#Time counter
start_time = time.time();

#Math Matrixs.
column = ["A", "B", "C", "D"];
rowValues = [1, 2, 3, 4];

#Setting the colums name

for col in column:
    print (col, end = " ");
print ("")

#The first on iterate is the outer loop (col) and the second one is the inner loop (row)

for idx, col in enumerate(column):
    for jdx, row in enumerate(rowValues):
        print(str(row+idx+jdx), end = " "); 
    print ("")

#See how much time take to loop the matrix
print((time.time()-start_time))
image.png
#With the timer, we can know how much time take the matrix to loops,
#this help us to optimize our code.

