
def read_file():
  filename = './input.txt'
  datos = []

  try:
    with open(filename, 'r') as file:
      firstLine = file.readline().strip()
      n, m = map(int, firstLine.split())
      datos.append((n, m))
      
      for linea in file:
        x1, y1, x2, y2 = list(map(int, linea.strip().split()))
        datos.append((x1, y1, x2, y2))
        
  except FileNotFoundError:
    print(f"Error: El archivo '{filename}' no fue encontrado.")
  except ValueError:
    print("Error: Asegúrate de que el archivo contenga solo números.")

  return datos

input = read_file()

# create square with pairs
n, m = input[0]
square = [0]*n
for i in range(n):
  square[i] = [0]*n

# sort rectangles by area
input.pop(0)
input.sort(key=lambda x: (x[2]-x[0]+1)*(x[3]-x[1]+1))
  
# fill square with rectangles
for k in range(m):
  x1, y1, x2, y2 = input[k]
  for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
      square[i][j] = square[i][j] + 1

# print square
for i in range(n):
  for j in range(n):
    print(square[i][j], end=" ")
  print()


ans = 0
for k, rect in enumerate(input):
  x1, y1, x2, y2 = rect
  has_one = False
  is_completly_painted = True
  
  for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
      if square[i][j] == 1:
        has_one = True
      if square[i][j] != 0:
        is_complitly_painted = False
          
  if has_one: 
    # it's needed to paint this rectangle
    ans += min(x2 - x1 + 1, y2 - y1 + 1)
    for i in range(x1, x2 + 1):
      for j in range(y1, y2 + 1):
        square[i][j] = 0
    
  elif is_completly_painted:
    # this rectangle is painted previously 
    pass
  else:
    # reduce the number of rectangles by squares by one
    for i in range(x1, x2 + 1):
      for j in range(y1, y2 + 1):
        square[i][j] = square[i][j] - 1 
     


print(ans)