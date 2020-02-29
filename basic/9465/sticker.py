test_case = int(input())
for _ in range(test_case):
   length = int(input())
   matrix = []
   for _ in range(2):
      matrix.append(list(map(int, input().split())))
   if length == 1:
      print(max(matrix[0][0], matrix[1][0]))
      break
   matrix[0][1] += matrix[1][0]
   matrix[1][1] += matrix[0][0]
   for iter in range(2, length):
      matrix[0][iter] += max(matrix[1][iter - 1], matrix[1][iter - 2])
      matrix[1][iter] += max(matrix[0][iter - 1], matrix[0][iter - 2])
   print(max(matrix[0][length - 1], matrix[1][length - 1]))

   
    
