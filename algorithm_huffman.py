
import string
with open("csci3104_spring2014_PS5_data.txt") as s:
	text = s.read().strip()
	frequencies = {}
	for x in text:
		frequencies[x] = text.count(x)




class PriorityQueue:
	"""docstring for PriorityQueue"""
	def __init__(self):
		self.heap = [0]
		self.size = 0
	def push(self, huf_node):
		self.heap.append(huf_node)
		self.size = self.size + 1
		self.moveUp(self.size)
	def moveUp(self, index):
		if index // 2 > 0:
			#print self.heap[index].freq < self.heap[index // 2].freq
			#the bug is probably near here
			if self.heap[index].freq < self.heap[index // 2].freq:
				self.swap(index, index // 2)
			self.moveUp(index // 2)
	def pop(self):
		retval = self.heap[1]

		self.heap[1] = self.heap[self.size]
		self.size = self.size - 1
		self.heap.pop()
		self.moveDown(1)
		return retval
	def moveDown(self, index):
		if index * 2 <= self.size:
			small_child = self.smallChild(index)
			if self.heap[index].freq > self.heap[small_child].freq:
				self.swap(index, small_child)
			self.moveDown(small_child)
	def smallChild(self, index):
		if 2 * index + 1 > self.size:
			return 2 * index
		else:
			if self.heap[2*index].freq > self.heap[2*index+1].freq:
				return 2 * index + 1
			else:
				return 2*index
	def swap(self, a, b):
		temp = self.heap[a]
		self.heap[a] = self.heap[b]
		self.heap[b] = temp
class HuffmanNode(object):
	def __init__(self, left = None, right = None, root = None):
		self.left = left
		self.right = right
		self.root = root
		self.isLeaf = False
		symbol = None
		freq = 0
	def children(self):
		return(self.left, self.right)



pq = PriorityQueue()
for key in frequencies:
	node = HuffmanNode()
	node.symbol = key
	node.freq = frequencies[key]
	node.isLeaf = True
	pq.push(node)
while pq.size > 1:
	node = HuffmanNode()
	left = pq.pop()
	right = pq.pop()
		