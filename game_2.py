#           0    1   2
matrix = [[" ", " "," "], #0
          [" "," "," "],#  1
          [" " ," ", " "]]#2


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

   # logic of winner
   if matrix[0][0] =="X" and matrix[0][1] == "X" and matrix[0][2] == "X":
      print("You are Winner")
      break
   if matrix[0][0] =="X" and matrix[1][0] == "X" and matrix[2][0] == "X":
      print("You are Winner")
      break
   if matrix[2][0] =="X" and matrix[1][1] == "X" and matrix[0][2] == "X":
      print("You are Winner")
      break
   
   if matrix[0][0] =="X" and matrix[1][1] == "X" and matrix[2][2] == "X":
      print("You are Winner")
      break     
   if matrix[2][0] =="X" and matrix[1][1] == "X" and matrix[0][2] == "X":
      print("You are Winner")
      break          
       
      
   if matrix[0][0] =="X" and matrix[1][0] == "X" and matrix[2][0] == "X":
      print("You are Winner")
      break    
   if matrix[0][1] =="X" and matrix[1][1] == "X" and matrix[2][1] == "X":
      print("You are Winner")
      break    
   if matrix[0][2] =="X" and matrix[1][2] == "X" and matrix[2][2] == "X":
      print("You are Winner")
      break 



       
