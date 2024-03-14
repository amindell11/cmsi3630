import sys
import CircularListNode as c
circleSize = int(sys.argv[1])
increment = int(sys.argv[2])
startVal = int(sys.argv[3])
ppl = c.CircularList()
for i in range(0,circleSize):
    ppl.insert(i)
ppl.display()
while(not ppl.current.data==startVal):
    ppl.step()
temp = ppl.current
while(not temp.next == temp):
    temp = ppl.current
    [ppl.step() for _ in range(increment)]
    print(f"kill person {temp.data}")
    ppl.delete(temp.data)
print(f"last survivor was person {temp.data}")

