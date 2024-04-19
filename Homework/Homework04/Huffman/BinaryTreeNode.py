###
# filename: BinaryTreeNode.py
# purpose: binary tree demonstrator
# author:   Dr. Johnson
# date:     2023-02-23
###

class BinaryTreeNode:

   # the constructor
   def __init__( self, value ):
      self.data  = value
      self.left  = None
      self.right = None

   # add a child to the node
   def add_child( self, value, child, isNode = False):
      if(not isNode):
         self.add_child(BinaryTreeNode(value),child,True)
      else:
         child = child.upper()
         if( child == "L"  ):
            print ("adding to L tree",value)
            self.left = value
         elif( child == "R" ):
            print ("adding to R tree",value)
            self.right = value
         else:
            raise( "   Illegal Argument Exception..." )

   # get one child from this parent node
   def get_child( self, child ):
      child = child.upper()
      if( child == "L" ):
         return self.left
      elif( child == "R" ):
         return self.right
      else:
         raise( "   Illegal Argument Exception..." )

   # get this node's data value
   def get_data( self ):
       return self.data

   def __str__(self):
      return str(self.get_data())
   
   def _draw_tree(self, prefix="", is_left=True):
      result = ""
      if self.right is not None:
         result += self.right._draw_tree(prefix + ("│   " if is_left else "    "), False)
      result += prefix + ("└── " if is_left else "┌── ") + str(self) + "\n"
      if self.left is not None:
         result += self.left._draw_tree(prefix + ("    " if is_left else "│   "), True)
      return result
   def __hash__(self):
      # Calculate hash based on value, left child, and right child
      return hash((self.val, self.left, self.right))

   def __eq__(self, other):
      # Check if two nodes are equal by comparing their attributes
      if isinstance(other, BinaryTreeNode):
         return self.val == other.val and self.left == other.left and self.right == other.right
      return False
   
root = BinaryTreeNode("[1,0]")
root.add_child("[1,0]", "L")
root.add_child("[5,0]", "R")
root.left.add_child("[4,0]", "L")
root.left.add_child("[2,0]", "R")

print(root)