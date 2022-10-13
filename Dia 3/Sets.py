mi_set = set([1,2,(4,5),3,4])
print((4,5) in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)


s4 = {1,2,3,4,5,6,7,8}
s4.add(5)
s4.discard(9)
print(s4)
pop1 = s4.pop()
print(pop1)
print(s4)




