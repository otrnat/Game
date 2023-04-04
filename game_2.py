matrix = [[" "," "," "],[" "," "," "],[" " ," ", " "]]



symb = "X"



step = 0
while step <= 9 :
    row = int(input("Enter your number of row"))
    column = int(input ("Enter your number of column" ))
    matrix[row][column] = symb
    step += 1   
    if symb == "X":
       symb = "0" 
    if symb == "0":
       symb = "X"   
   

