class MyArray():
  def __init__(self):
    self.length = 0
    self.data = []
  def get(self, index): 
    return self.data[index]
  
  def push(self, item): 
    self.data.append(item)
    self.length +=1
    return self.length
  def pop(self):
    lastitem = self.data[self.length -1]
    del self.data[self.length-1]
    self.length -= 1
    return lastitem
  
  def delete(self, index): 
    item = self.data[index]
    self.shiftitem(index)
    self.length -= 1

  def shiftitem(self, index):
    for i in range(index, self.length-1):
      self.data[i] = self.data[i+1]
    del self.data[self.length-1]


if __name__ == '__main__':
  MA = MyArray()
  MA.push('hi')
  MA.push('you')
  MA.push('!')
  MA.push('are')
  MA.push('nice')
  print(MA.length, MA.data)
  MA.delete(0)
  MA.delete(1)
  print(MA.length, MA.data)
  
