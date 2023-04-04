matrix = [[" ", " "," "],[" "," "," "],[" " ," ", " "]]



symb = "X"



step = 0
while step <= 9 :
    row = int(input("Enter your number of row: "))
    column = int(input ("Enter your number of column: " ))
    matrix[row][column] = symb
    step += 1
    for i in range(len(matrix)):
       print(f"{matrix[i][0]} | {matrix[i][1]} | {matrix[i][2]}")

    print(matrix)  
    if symb == "X":
       symb = "0" 
    else: symb = "X" 

       
   

