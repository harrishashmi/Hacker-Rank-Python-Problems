"""i=0
def countdown(i):
    print (i)
    if i <= 0: #BASE CASE
        return
    else: 
        countdown(i-1) # Recursive case


countdown(5);"""

"STACK"
"""""
def greet(name):
 print ('hello,' + name + '!')
 greet2(name)
 print ('getting ready to say bye...')
 bye()


def greet2(name):
    print ('how are you ');

def bye():
    print('ok honn bye')

greet('Harris'  )

"""""
"""""
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
    
x=sum([1,2,3,4])
print(x)
"""""
'''''
def xyz(arr):
    total = 0
    if arr == []:
        return 0
    return arr[0] + xyz(arr[1:])

x=xyz([1,2,3,4])
print(x);

'

''''''
#WRITE A FUNCTION TO COUNT NUMBERS IN A LIST
def count(arr):
    if arr == []:
        return 0
    else:
        return 1+count(arr[1:])

x=count([1,4,5,0,9])
print (x)
'''''
'''''''''
def max(list):
     if len(list) == 3:
        return list[0] if list[0] > list[1] else list[1]
        sub_max = max(list[1:])
        
        return list[0] if list[0] > sub_max else sub_max

x = max([91,23,1-])
print(x)

''''''''''''''
'''''''
# Quick Sort
def quicksort(array):
     if len(array) < 2:
         return array #Base case: arrays with 0 or 1 element are already “sorted.”
     else:
      pivot = array[0] #Recursive case
      less = [i for i in array[1:] if i <= pivot] #Sub-array of all the elements 
      #less than the pivot
      greater = [i for i in array[1:] if i > pivot] #Sub-array of all the elements greater than the pivot
      return quicksort(less) + [pivot] + quicksort(greater)
    
print (quicksort([10, 5, 2, 3,9]))
'''''''''

#Binary search recursive

'''''''''''''''''''''''
def binarySearch (arr, x):
        l = 0
        r = len(arr)-1
        mid = (l+r) // 2
        
        if (arr[mid] == x):
            return mid
          
        # If element is smaller than mid, then it 
        # can only be present in left subarray
        if  x > arr[mid]:
           
            return binarySearch(arr[mid+1:],x) + mid+1
  
        # Else the element can only be present 
        # in right subarray
        else:
          return binarySearch(arr[:mid],x) + mid+1
  
        
        # Element is not present in the array
        return -1

''''''''

      
 
        
  
# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 3
# Function call


result = binarySearch(arr,x)



  
print (result)
'''''
# Queues and Graphs 
''''''''''''''''
graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = [] 


from collections import deque
search_queue = deque()
search_queue += graph['you']



def person_is_mango_seller(name):
    return name[-1] == 'j' 


def search(name):
    search_queue = deque()
    search_queue += graph['you']
    searched = []
    while search_queue:
        
        person = search_queue.popleft()
        if not person in searched:
            if person_is_mango_seller(person):  
                print(person + '  is a mango seller')
                return True
        
            else:
                search_queue += graph[person]
                searched.append(person)

    return False
    

result = search('you')
print(result)
'''''''''''''''''''''


# Dijkstras Algorithm:
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}
infinity = float('inf')
costs  = {}
costs['a'] = 6
costs['b'] = 2 
costs['fin'] = infinity

#hash table for parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = 'None'

processed = []



def find_lowest_cost_node(costs):
 lowest_cost = float('inf')
 lowest_cost_node = None
 for node in costs: 
    cost = costs[node]
 if cost < lowest_cost:
    lowest_cost = cost
   
 return lowest_cost_node 

node = find_lowest_cost_node(costs) 
while node is not None: 
 cost = costs[node]
 neighbors = graph[node] 
 for n in neighbors.keys(): 
    new_cost = cost + neighbors[n] 
 if costs[n] > new_cost:
    costs[n] = new_cost
 parents[n] = node 
 processed.append(node) 
 node = find_lowest_cost_node(costs)



