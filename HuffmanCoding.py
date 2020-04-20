import heapq
import bitstring


# Reading input file in an array
value = input("Please enter a string:\n")
value1 = value+'Binary.txt'
value2 = value+'Answer.txt'
value = value+'.txt'

print('you will find the encrypted file as :'+value1)
print('you will find the file after decryption as :'+value2)

f = open(value, 'r')
read_data = f.read()
chars = list(read_data)

chars.append('$')
# printing the array
# print(chars)

# Calculating the frequency of each element in the array
Freq = {}
for char in chars:
    if char in Freq:
        Freq[char] += 1
    else:
        Freq[char] = 1

# testing the frequency
# for i in Freq:
# print(i , Freq[i])


# constructing the tree
class node:
    def __init__(self, lChild, rChild, Value, Frequency):
        self.lChild = lChild
        self.rChild = rChild
        self.Value = Value
        self.Frequency = Frequency

# Local Comparison to know on which value insert in the heap
    def __lt__(self, other):
        return self.Frequency<other.Frequency


Hp = [None] * len(Freq)
count = 0

# Creating List Of Nodes
for i in Freq:
    
    Hp[count] = node(None, None, i, Freq[i])
    count += 1

heapq.heapify(Hp)       # Constructing the heap

# Checking if the heap has been sorted correctly
# for i in range(count):
#    print(Hp[i].Value) 
 
# Combine The least two nodes together till we have one node
while len(Hp) > 1:
    x = heapq.heappop(Hp)
    y = heapq.heappop(Hp)
    if x.Frequency > y.Frequency:
        z = node(x, y, None, x.Frequency+y.Frequency)
    else: 
        z = node(y, x, None, x.Frequency+y.Frequency)
    heapq.heappush(Hp, z)

# Checking that all node are combined
# for i in range(len(Hp)):
    # print(Hp[i].Frequency)

# Getting the code for every Char
EnD = {}


def Recurse (node, Code = ""):
   
    if node.Value == None:
        # print(node.lChild)
        # print('left')
        Recurse(node.lChild, Code=Code+'1')
        # print('right')
        Recurse(node.rChild, Code=Code+'0')
    else:
        EnD [node.Value] = Code
        # print('d5alt')
        return


Recurse(node= Hp[0])

# print (EnD)

# for i in EnD:
# print(i , EnD[i])


# Produce a binary encrypted file

binary = ''
for char in chars:
    binary = binary+EnD[char]
# print(binary)


def String_To_Byte(text):
    i = 0
    solly = bytearray()
    while i+8 <= len(text):
        b = text[i:i+8]
        b = int(b, 2)
        solly.append(b & 0xff)
        i += 8

    remain = len(text) - i
    if remain == 0:
        return solly
    b = text[i:]
    b += '0'*(8-remain)
    b = int(b, 2)
    solly.append(b & 0xff)
    return solly


toWrite = String_To_Byte(binary)

a = open(value1, 'wb')
a.write(toWrite)
a.close()

# creating the inverse dictionary
DecD = {}

for key, value in EnD.items():
    DecD[value] = key

# print(DecD)

# Decrypting the binary file

a2 = open(value1, 'r')
toRead = bitstring.Bits(a2)
# print(toRead)
kelma = ''

# print(binary)

f2 = open(value2, 'a')
for i in toRead:
    kelma = kelma+str(str(int(i)))
    # print(i)
    # print(kelma)
    if kelma in DecD.keys():
        # print(DecD[kelma])
        if DecD[kelma] == '$':
            break
        f2.write(DecD[kelma])
        kelma = ""







