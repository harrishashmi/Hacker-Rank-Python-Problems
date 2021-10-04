from collections import Counter
no_shoes = int(input())
shoe_sizes = map(int,input().split())
no_of_customers = int(input())
size_price = map(list,(map(int,input().split()) for _ in range(no_of_customers)))
n = Counter(shoe_sizes)
price = 0
for i in size_price:
    if i[0] in n.keys() and n[i[0]] > 0:
        n[i[0]] = n[i[0]]-1
        price = price + i[1]

print(price)
print(n)
print(size_price)