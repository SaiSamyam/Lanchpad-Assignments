import heapq

numbers=list(eval(input('Enter the list of numbers: ')))
n=int(input('how many nth lowest terms do u want: '))
print('The lowest nth term is: ',heapq.nsmallest(n,numbers))