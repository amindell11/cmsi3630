from PriorityQueue import PriorityQueue
from BinaryTreeNode import BinaryTreeNode
class HuffmanCode:
    def __init__(self, string) :
        self.coded_tree = create_huffman_tree(string)
        self.code_table = generate_code_table(self.coded_tree)
    def encodeMessage(self,msg):
        coded_msg = ''
        for char in msg:
            try:
                coded_msg += self.code_table[char]
            except KeyError:
                print(f'invalid msg: no code for char {char}')
                return None
        return coded_msg

    def decodeMessage(self, msg):
        decoded_msg = ''
        current_node = self.coded_tree

        for char in msg:
            if char == '1':
                current_node = current_node.right
            elif char == '0':
                current_node = current_node.left

            if not current_node.data[0] == '-':
                decoded_msg += current_node.data[0]
                current_node = self.coded_tree

        return decoded_msg
def create_huffman_tree(string):
    chars = []
    freqs = []
    for char in string:
        if(char in chars):
            freqs[chars.index(char)] +=1
        else:
            chars.append(char)
            freqs.append(1)
    print(chars,freqs)
    prioq = PriorityQueue()
    for i in range(len(chars)):
        prioq.enqueue(BinaryTreeNode([chars[i],freqs[i]]),freqs[i])
    while(len(prioq)>1):
        l_node = prioq.dequeue()
        r_node = prioq.dequeue()
        
        #print("l node ", l_node._draw_tree())
        sum_freq = l_node.get_data()[1]+r_node.get_data()[1]
        #print(sum_freq)
        
        new_node = BinaryTreeNode(["-",sum_freq])
        new_node.add_child(l_node, "L", True)
        new_node.add_child(r_node, "R", True)
        #print(new_node)
        
        #print("making new node: \n", new_node._draw_tree())
        prioq.enqueue(new_node,sum_freq)
    return prioq.dequeue()
def generate_code_table( root, code='', code_table={}):
    if root:
        # If the current node is a leaf node, add its value and code to the code table
        if not root.left and not root.right:
            code_table[root.data[0]]=code
        # Traverse left subtree, append '0' to the code
        generate_code_table(root.left, code + '0', code_table)
        # Traverse right subtree, append '1' to the code
        generate_code_table(root.right, code + '1', code_table)
    return code_table

def main():
    code = HuffmanCode("pee pee poo poo and a lot of big snoottttt")
    print(code.coded_tree._draw_tree())
    print (code.code_table)
    coded = code.encodeMessage('pee pee poo poo and a lot of big snoottttt')
    print(coded)
    print(code.decodeMessage(coded))
main()

    