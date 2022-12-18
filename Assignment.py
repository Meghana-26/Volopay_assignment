import math 

#Need to fill other than window and centre seats first
def aisle_seats(mat, ind, input, passengers_in_a_queue): 
  for p1 in range(0, row):      #for every row need to iterate
    k = 0
    for i in range(0, len(input)):
      temp = k
      if(p1 < input[i][1]):     #Check for limit of that row
        mid = math.floor(input[i][0]/2) 
        if(input[i][0]%2 == 1): #Odd no.of columns
          mid += temp
          for j in range(temp, temp+input[i][0]):
            k += 1
            if(j != mid and j != 0 and j != col-1):
              mat[p1][j] = ind
              if(ind < passengers_in_a_queue):  
                ind += 1
              else:
               return ind      # if passengers_in_a_queue is completed we need to stop arranging 
        else:                  # Even no.of columns
          mid += temp
          for j in range(temp, temp+input[i][0]):
            k += 1
            if(input[i][0] <= 2 or j != mid and j != mid-1):
              if(j != 0 and j != col-1):
                mat[p1][j] = ind
                if(ind < passengers_in_a_queue):
                  ind += 1
                else:
                  return ind
      else:
        for j  in range(temp, temp + input[i][0]):
          k += 1
  return ind 

#Need to fill window seats next
def window_seats(mat, ans, array, passengers_in_a_queue, h):
  for i in range(0, row):
    for j in range(0, col):
      if(j == 0 and array[0][1] > i):        #Fill the first column from left to right
        mat[i][j] = ans
        if(ans < passengers_in_a_queue):
          ans += 1
        else:
          return ans+1
      if(j == col-1 and array[h-1][1] > i):  #Fill the last column from left to right
        mat[i][j] = ans
        if(ans < passengers_in_a_queue):
          ans += 1
        else:
          return ans
  return ans

#Need to fill middle seats at last
def middle_seats(mat, ans, input, passengers_in_a_queue):
  for p1 in range(0, row):
    k = 0
    for i in range(0, len(input)):
      temp = k
      if(p1 < input[i][1]): 
        mid = math.floor(input[i][0]/2)
        if(input[i][0]%2 == 1):        # for odd no.of columns
          mid += temp
          for j in range(temp, temp+input[i][0]):
            k += 1
            if(mat[p1][j] == 0 ):
              mat[p1][j] = ans
              if(ans < passengers_in_a_queue):
                ans += 1
              else:
                return ans
        else:                          # for even no.of columns
          mid += temp
          for j in range(temp, temp+input[i][0]):
            k += 1
            if(mat[p1][j] == 0 ):
              mat[p1][j] = ans
              if(ans < passengers_in_a_queue):
                ans += 1
              else:
                return ans
      else:
        for j  in range(temp, temp + input[i][0]):
          k += 1
    

"""
Read input from file 
Input format :
  No.of passengers in a queue  No.of rows
  Input format as a list
"""
# Can use file1.dt or file.dat
with open('file1.dat') as f:
    passengers, h = [int(x) for x in next(f).split()] # read first line
    array = []
    for line in f: # read rest of lines
        array.append([int(x) for x in line.split()])

col = 0
row = 0
for j in range(0, len(array)):
  col += array[j][0] #No.of columns
  row = max(row, array[j][1]) #No.of rows

#Empty matrix
mat = [[0 for _ in range(col)] for _ in range(row)]


ans = aisle_seats(mat, 1, array, passengers)

ans = window_seats(mat, ans, array, passengers, h)

ans = middle_seats(mat, ans, array, passengers)

"""
For better representation we can import numpy and use matrix
arr = np.matrix(mat)
print(arr)
"""

#Resultant arrangement
for i in range(0, row): 
  print(mat[i], end = "\n")
