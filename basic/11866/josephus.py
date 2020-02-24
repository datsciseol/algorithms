class Node:
    def __init__(self, objValue = "", nodeNext = ""):
        self.objValue = objValue
        self.nodeNext = nodeNext
    
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    
    def setValue(self, objValue):
        self.objValue = objValue
    
    def getNext(self):
        return self.nodeNext
    
    def getValue(self):
        return self.objValue

def nodeMove(nodeCurr, idx):
    for _ in range(idx):
        nodeCurr = nodeCurr.getNext()
    return nodeCurr

num, kth = map(int, input().split())
nodeStart = Node(1)
nodeCurr = nodeStart
basis = 2
size = 1
while basis < num + 1:
    nodeNew = Node(basis)
    nodeCurr.setNext(nodeNew)
    nodeCurr = nodeCurr.getNext()
    basis += 1
    size += 1
nodeCurr.setNext(nodeStart)
# 여기까지 이제 원형 연결 리스트 완성
print("<", end = "")
while size:
    nodePrev = nodeMove(nodeCurr, kth - 1)
    nodeCurr = nodePrev.getNext()
    nodeNext = nodeCurr.getNext()
    nodePrev.setNext(nodeNext)
    
    print(nodeCurr.getValue(), end = "")
    size -= 1
    if size != 0:
        print(end = ", ")
print(">")
