import heapq
from bitarray import bitarray

# Reading input file in an array
path = input("Please enter file path : ")

file = open(path, encoding="utf8")
data = file.read()
file.close()

# Calculating the frequency of each element in the array
Freq = {}
for char in data:
    if char in Freq:
        Freq[char] += 1
    else:
        Freq[char] = 1


# constructing the tree
class Node:
    def __init__(self, left, right, character, frequency):
        self.left = left
        self.right = right
        self.value = character
        self.frequency = frequency

# Local Comparison to know on which value insert in the heap
    def __lt__(self, other):
        return self.frequency < other.frequency


Hp = [None] * len(Freq)
count = 0

# Creating List Of Nodes
for i in Freq:
    Hp[count] = Node(None, None, i, Freq[i])
    count += 1

heapq.heapify(Hp)


# Combine The least two nodes together till we have one node
while len(Hp) > 1:
    x = heapq.heappop(Hp)
    y = heapq.heappop(Hp)
    if x.frequency > y.frequency:
        z = Node(x, y, None, x.frequency+y.frequency)
    else: 
        z = Node(y, x, None, x.frequency+y.frequency)
    heapq.heappush(Hp, z)

# Getting the code for every Char
EnD = {}


def recurse(node, code):
    if node.value is not None:
        c = bitarray(code)
        EnD[node.value] = c
        return
    else:
        recurse(node.left, code + '1')
        recurse(node.right, code + '0')


recurse(Hp[0], '')

# Produce a binary encrypted file
binary = bitarray()

for char in data:
    binary += EnD[char]

path = path.split('.txt')
path = path[0]
a = open(path+'Binary.txt', 'wb')
a.write(binary)
a.close()


# creating the inverse dictionary
DecD = {}
for key, value in EnD.items():
    DecD[value.to01()] = key

# Decrypting the binary file
a2 = open(path+'Binary.txt', 'rb')
toRead = bitarray()
toRead.fromfile(a2)
a2.close()

word = ''
string = ''
f2 = open(path+'Decrypted.txt', 'wb')
for i in toRead:
    word = word + str(int(i))
    if word in DecD.keys():
        if DecD[word] == '$':
            break
        string += DecD[word]
        word = ""

f2.write(string.encode('utf-8', 'ignore'))







