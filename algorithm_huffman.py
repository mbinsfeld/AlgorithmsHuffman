
import string


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


def getFrequencies(File):
	with open(File) as s:
		text = s.read().strip()
		frequencies = {}
		for x in text:
			frequencies[x] = text.count(x)
	return frequencies


def buildHuffmanTree(frequencies):
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
		node.left = left
		node.right = right
		node.freq = left.freq + right.freq
		pq.push(node)
	return pq.heap[1]

def buildCodeBook(tree):
	path = ""
	dic = dict()
	dic = buildCodeBookHelp(tree, path)
	return dic
def buildCodeBookHelp(tree, path):
	dic = dict()
	if(tree.isLeaf == True):
		dic[tree.symbol] = path
		return dic
	else:
		path_left = path + "0"
		path_right = path + "1"
		dic = buildCodeBookHelp(tree.left, path_left)
		right = buildCodeBookHelp(tree.right, path_right)
		dic = dict(dic.items() + right.items())
		return dic
def encodeString(original, codeBook):
	result = ""
	string = original.read().strip()
	for c in string:
		result = result + codeBook[c]
	return result
		
File = "csci3104_spring2014_PS5_data.txt"
string = ""
string = open(File)
frequencies = getFrequencies(File)
tree = buildHuffmanTree(frequencies)
codeBook = buildCodeBook(tree)
#print codeBook
encoded = encodeString(string, codeBook)
print encoded
