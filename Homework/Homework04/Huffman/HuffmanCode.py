from PriorityQueue import PriorityQueue
from BinaryTreeNode import BinaryTreeNode
class HuffmanTree:

    def __init__(self, string) :
        self.create_tree(string)
    def create_tree(self, string):
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
            sum_freq = l_node.get_data()[1]+r_node.get_data()[1]
            print(sum_freq)
            new_node = BinaryTreeNode(["-",sum_freq])
            new_node.add_child(l_node, "L")
            new_node.add_child(r_node, "R")
            print(new_node)
            print("making new node: \n", new_node._draw_tree())
            prioq.enqueue(new_node,sum_freq)
        print(prioq.peek()._draw_tree())
def main():
    tree = HuffmanTree("hello")
main()

    