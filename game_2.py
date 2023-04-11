#           0    1   2
matrix = [[" ", " "," "], #0
          [" "," "," "],#  1
          [" " ," ", " "]]#2


symb = "X"



while True:
   row = int(input("Enter your number of row: "))
   column = int(input ("Enter your number of column: " ))
   matrix[row][column] = symb

   for i in range(len(matrix)):
      print(f"{matrix[i][0]} | {matrix[i][1]} | {matrix[i][2]}")

   if matrix[0][0] == symb and matrix[0][1] == symb and matrix[0][2] == symb:
      print(f"You are Winner {symb}")
      break
   if matrix[0][0] ==symb and matrix[1][0] == symb and matrix[2][0] == symb:
      print(f"You are Winner {symb}")
      break
   if matrix[2][0] == symb and matrix[1][1] == symb and matrix[0][2] == symb:
      print(f"You are Winner {symb}")
      break
   
   if matrix[0][0] ==symb and matrix[1][1] == symb and matrix[2][2] == symb:
      print(f"You are Winner {symb}")
      break     
   if matrix[2][0] ==symb and matrix[1][1] == symb and matrix[0][2] == symb:
      print(f"You are Winner {symb}")
      break          
       
      
   if matrix[0][0] ==symb and matrix[1][0] == symb and matrix[2][0] ==symb:
      print(f"You are Winner {symb}")
      break    
   if matrix[0][1] ==symb and matrix[1][1] == symb and matrix[2][1] == symb:
      print(f"You are Winner {symb}")
      break    
   if matrix[0][2] ==symb and matrix[1][2] == symb and matrix[2][2] == symb:
      print(f"You are Winner {symb}")
      break 



   print(matrix)  
   if symb == "X":
       symb = "0" 
   else: symb = "X" 

   # logic of winner
   



       
