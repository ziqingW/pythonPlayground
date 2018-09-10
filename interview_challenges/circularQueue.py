class MyCircularQueue(object):

  def __init__(self, k):
    self.queue = [None] * k
    self.size = k
    self.tail = 0
    self.head = 0

  def enQueue(self, value):
    if not self.isFull():
      if self.tail == self.size:
        self.tail = 0
      self.queue[self.tail] = value
      self.tail += 1
      return True
    return False
  
  def deQueue(self):
    if not self.isEmpty():
      self.queue[self.head] = None
      self.head += 1
      if self.head == self.size:
        self.head = 0
      return True
    return False
  
  def Front(self):
    if self.head == self.size:
      self.head = 0
    return self.queue[self.head]

  def Rear(self):
    return self.queue[self.tail-1]

  def isEmpty(self):
    for value in self.queue:
      if value != None:
        return False
    return True

  def isFull(self):
    if not None in self.queue:
      return True
    return False
    
obj = MyCircularQueue(4)
obj.enQueue(3)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(4)
obj.enQueue(5)
print(obj.Front(), obj.Rear())
print(obj.queue)
obj.deQueue()
print(obj.queue)
obj.deQueue()
print(obj.queue)
obj.enQueue(6)
print(obj.queue)
obj.enQueue(7)
print(obj.queue)
obj.enQueue(8)
print(obj.queue)
print(obj.Front())
print(obj.Rear())