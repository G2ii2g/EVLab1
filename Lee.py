import time
from collections import deque

# Класс для хранения координат ячеек
class Cell:
	def __init__(self,x: int, y: int):
		self.x = x
		self.y = y

# Обявление класса элемента очереди для использования в поиске в ширину
class queueNode:
	def __init__(self,pt: Cell, dist: int):
		self.pt = pt # Координата ячейки
		self.dist = dist # Расстояние до ячейки от исходной

# Проверка, является ли данная ячейка (row,col) допустимой
def checkValid(mat, row: int, col: int):
        ROW = len(mat) # Количество строк
        COL = len(mat[0]) # Количество столбцов
        return ((row >= 0) and (row < ROW) and (col >= 0) and (col < COL))

# Массивы для 4 возможных перемещений из ячейки
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

# Функция для нахождения кратчашего пути между исходной (src) и конечной ячейками (dest) поиском в ширину
def dictbfsLee(mat, src: Cell, dest: Cell):
	# Проверка, что исходная и конечная ячейки имеют значение 1 (допустимая ячейка в пути) 
	if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1:
		return -1
	
	visited = {}
	
	# Пометить исходную ячейку как посещённую 
	visited[(src.x,src.y)] = True
	
	# Создать очередь для поиска в ширину 
	q = deque()
	
	# Расстояние исходной ячейки равно 0
	s = queueNode(src,0)
	q.append(s) # Поместить в очередь исходную ячейку
	
	# Выыполнить поиск в ширину, начиная с иходной ячейки
	while q:
		curr = q.popleft() # Извлечь первую ячейку в очереди
		
		# Если достигнута конечная ячейка, возвращается расстояние до нее 
		pt = curr.pt
		if pt.x == dest.x and pt.y == dest.y:
			return curr.dist
		
		# Иначе поместить в очередь её смежные непосещённые ячейки со значением 1 (допустимая ячейка в пути) 
		for i in range(4):
			row = pt.x + rowNum[i]
			col = pt.y + colNum[i]
			
			# Поместить в очередь допустимые смежные непосещённые ячейки
			if (checkValid(mat, row,col) and mat[row][col] == 1 and (row,col) not in visited):
				visited[(row,col)] = True
				Adjcell = queueNode(Cell(row,col),curr.dist+1)
				q.append(Adjcell)
	
	# Взвратить -1 если конечная ячейка не может быть достигнута
	return -1

def bfsLee(mat, src: Cell, dest: Cell):
	# Проверка, что исходная и конечная ячейки имеют значение 1 (допустимая ячейка в пути) 
	if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1:
		return -1
	
	visited = [[False for i in range(len(mat[0]))] 
					for j in range(len(mat))]
	
	# Пометить исходную ячейку как посещённую 
	visited[src.x][src.y] = True
	
	# Создать очередь для поиска в ширину 
	q = deque()
	
	# Расстояние исходной ячейки равно 0
	s = queueNode(src,0)
	q.append(s) # Поместить в очередь исходную ячейку
	
	# Выыполнить поиск в ширину, начиная с иходной ячейки
	while q:
		curr = q.popleft() # Извлечь первую ячейку в очереди
		
		# Если достигнута конечная ячейка, возвращается расстояние до нее 
		pt = curr.pt
		if pt.x == dest.x and pt.y == dest.y:
			return curr.dist
		
		# Иначе поместить в очередь её смежные непосещённые ячейки со значением 1 (допустимая ячейка в пути) 
		for i in range(4):
			row = pt.x + rowNum[i]
			col = pt.y + colNum[i]
			
			# Поместить в очередь допустимые смежные непосещённые ячейки
			if (checkValid(mat, row,col) and mat[row][col] == 1 and not visited[row][col]):
				visited[row][col] = True
				Adjcell = queueNode(Cell(row,col),curr.dist+1)
				q.append(Adjcell)
	
	# Взвратить -1 если конечная ячейка не может быть достигнута
	return -1

# Код тестирующей программы
def testdict(mat):
    source = Cell(0,0)
    dest = Cell(len(mat)-1,len(mat[0])-1)
    start = time.time() ## точка отсчета времени
    dist = dictbfsLee(mat,source,dest)
    end = time.time() - start ## собственно время работы программы

    print("Матрица", len(mat), "на", len(mat[0]))       
    if dist!=-1:
            print("Длина кратчайшего пути равна",dist)
    else:
            print("Кратчайший путь не существует")
    print("Время работы с использованием словаря", end) ## вывод времени        

def test(mat):
    source = Cell(0,0)
    dest = Cell(len(mat)-1,len(mat[0])-1)
    start = time.time() ## точка отсчета времени
    dist = bfsLee(mat,source,dest)
    end = time.time() - start ## собственно время работы программы

    print("Матрица", len(mat), "на", len(mat[0]))       
    if dist!=-1:
            print("Длина кратчайшего пути равна",dist)
    else:
            print("Кратчайший путь не существует")
    print("Время работы с использованием списка", end) ## вывод времени        

mat0 = [ [ 1, 0, 1, 1, 1 ],
	[ 1, 0, 1, 0, 1 ], 
	[ 1, 1, 1, 0, 1 ], 
	[ 0, 0, 0, 0, 1 ], 
	[ 1, 1, 1, 0, 1 ]]
mat1= [[1 for i in range(500)] for j in range(500)]
mat2= [[1 for i in range(1000)] for j in range(1000)]
testdict(mat0)
test(mat0)
testdict(mat1)
test(mat1)
testdict(mat2)
test(mat2)

