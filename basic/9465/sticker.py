test_case = int(input())
for _ in range(test_case):
   length = int(input())
   matrix = []
   matrix.append(list(map(int, input().split())))
   matrix.append(list(map(int, input().split())))
   if length == 1:
      result = max(matrix[0][0], matrix[1][0])
      print(result)
   elif length == 2:
      result = max(matrix[0][0] + matrix[1][1], matrix[0][1] + matrix[1][0])
      print(result)
   else:
      matrix[0][1] += matrix[1][0]
      matrix[1][1] += matrix[0][0]
      for iter in range(2, length):
         matrix[0][iter] += max(matrix[1][iter - 1], matrix[1][iter - 2])
         matrix[1][iter] += max(matrix[0][iter - 1], matrix[0][iter - 2])
      result = max(matrix[0][length - 1], matrix[1][length - 1])
      print(result)