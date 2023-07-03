# if you make it to "None", you've traversed the entire list
def is_bst_rec(root, min_value, max_value):

  # that means it's a Binary Search Tree not just a binary tree
  if root == None:
    return True

  # if the current node is less than the minimum value or it's greater than the max val
  # obviously this is not sorted correctly, it's not a BST return false
  if root.data < min_value or root.data > max_value:
    return False

  # otherwise, we need to recurse again
  # for left side we pass the left node and the current parent numerical value
  # the min value will be some very large negative number
  # for the right side we pass the right node and the current parent numerical value as the "max"
  # eventually we either find the tree is not balanced OR we hit "None" which means it is balanced
  return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)

def is_bst(root):
  return is_bst_rec(root, -sys.maxsize - 1, sys.maxsize)
