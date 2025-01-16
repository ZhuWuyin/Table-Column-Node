from Database import Database
from Column import Column

c0 = Column([5,4,3,2,1])
c1 = Column(["a", "b", "c", "d", "e"])
c2 = Column([2,2,2,2,2])
c3 = Column([9,9,9,9,9])

d1 = Database(c0)
d1.append_col(c1)
d1.append_col(c2)

d1[1] = c3
del d1[1]

print(d1.print_table(reverse=False, get_content=True))