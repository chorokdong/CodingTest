import queue


################# Queue() #################
# 일반적인 큐 자료구조
data = queue.Queue()
data.put(1) # 1
data.put(2) # 1 -> 2
data.put(3) # 1 -> 2 -> 3
data.get() # 1 출력
data.get() # 2 출력
###########################################



################# LifoQueue() #################
# Stack과 동일하게 나중에 입력된 데이터가 먼저 출력되는 구조 (후입선출)
data = queue.LifoQueue()
data.put(1) # 1
data.put(2) # 2 -> 1
data.put(3) # 3 -> 2 -> 1
data.get() # 3 출력
data.get() # 2 출력
###############################################

################# PriorityQueue() #################
# 데이터마다 우선순위를 지정하여 정렬된 큐
# 우선순위 높은 순으로 출력하는 자료구조
data = queue.PriorityQueue()
data.put(4) # 4
data.put(1) # 1 -> 4
data.put(7) # 1 -> 4 -> 7
data.put(3) # 1 -> 3 -> 4 -> 7
data.get() # 1 출력
data.get() # 3 출력 

data.put((3,'Apple')) # (3, 'Apple')
data.put((2,'Banana')) # (2, 'Banana') -> (3, 'Apple')
data.put((1,'Orange')) # (1,'Orange') -> (2, 'Banana') -> (3, 'Apple')
data.get() # (1,'Orange') 출력
data.get() # (2, 'Banana') 출력
###################################################


################ Stack ################
stack = list()
stack.append(1) # 1
stack.append(3) # 1 -> 3
stack.append(2) # 1 -> 3 -> 2
stack.pop() # 2 출력
stack.pop() # 3 출력
#######################################