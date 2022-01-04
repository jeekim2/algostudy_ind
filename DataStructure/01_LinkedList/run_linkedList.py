from linkedList import LinkedList

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

data = l.first()  # 1
l.next()  # 2
l.next()  # 3
l.next()  # 4
l.insert(10)

# all list print
l.first()
while True:
    if data:
        print(data)
        data = l.next()
    else:
        break
