#Rene Esquivel
#80219337
#CS2302
import difflib as dl

#AVLTree
class AVLTree:
    def __init__(self):
        self.root = None

    def rotateLeft(self, node):

        right_left_child = node.right.left

        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:
            self.root = node.right
            self.root.parent = None

        node.right.set_child('left', node)
        node.set_child('right', node)

        return node.parent

    def rotateRight(self,node):

        left_right_child = node.left.right

        if node.parent is not None:
            node.parent.replace_child(node, node.left)

        else:
            self.root = node.left
            self.root.parent = None

            node.left.set_child('right', node)

            node.set_child('left', left_right_child)

            return node.parent

    def rebalance(self, node):

        node.update_height()

        if node.get_balance == -2:

            if node.right.get_balance() == 1:
                self.rotate_right(node.right)
                return self.rotate_left(node)

            elif node.get_balance() == 2:

                if node.left.get_balance() == -1:
                    self.rotate_left(node.left)

            return self.rotate_right(node)

        return node


    def words_In_Tree_Ascending(Node):
        Node.sort()
        if Node is None:
            return

            words_In_Tree_Ascending(Node)
            return Node

        words_In_Tree_Ascending(Node)
        print(Node)

    def tree_Height(Node):
        if Node is None:
            return -1

            leftHeight = tree_Height(Node)
            rightHeight = tree_Height(Node)

            return 1 + max(leftHeight, rightHeight)


#Red/BlackTree
class RBTNode:

    def __init__(self, key, parent, isRed = False, left = None, right = None):
        self.key = key
        self.left = left
        self.right - right
        self.parent = parent

        if isRed:
            self.color = "red"
        else:
            self.color = "black"

    def are_Both_Children_Black(self):
        if self.left != None and self.left.isRed():
            return False

        if self.right != None and self.right.isRed():
            return False

        return True

    def count(self):
        count = 1
        if self.left != None:
            count = count + self.left.count()
        if self.right != None:
            count = count + self.right.count()

        return count

    def get_Grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent


    def get_Predecessor(self):
        node = self.left
        while node.right is not None:
            node=node.right
        return node

    def get_Sibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
        return self.parent.left

        return None

    def get_Uncle(self):
        grandparent = self.get_Grandparent()

        if grandparent is None:
            return None

        if grandparent.left is self.parent:
            return grandparent.right
        return grandparent.left

    def is_Black(self):
        return self.color == "black"

    def is_Red(self):
        return self.color == "red"

    def replace_Child(self, current_Child, new_Child):
        if self.left is current_Child:
            return self.set_child("left", new_Child)
        elif self.right is current_Child:
            return self.set_child("right", new_Child)
        return False

    def set_Child(self, which_child, child):
        if which_child != "left" and which_child != "right":
            return False

        if which_child == "left":
            self.left = child
        else:
            self.right = child

        if child != None:
            child.parent = self
        return True

    def num_Of_Nodes_Tree(self):
        count = 0

        if self is None:
            return 0
            count += 1 + num_Of_Nodes_Tree(self.get_left()) + num_Of_Nodes_Tree(self.get_right())

        return count

    def get_Height(self):
        if self.root:
            return self.root.get_Height()
        else:
            return 0

    def get_Height(self):
        if self.left_Child and self.right_Child:
            return 1 + max(self.left_Child.get_Height(), self.right_Child.get_Height())
        elif self.left_Child:
            return 1 + self.left_Child.get_Height()
        elif self.right_Child:
            return 1 + self.right_Child.get_Height()
        else:
            return 1

    def words_In_Tree_Ascending(Node):
        Node.sort()
        if Node is None:
            return

            words_In_Tree_Ascending(Node)
        return Node

        words_In_Tree_Ascending(Node)
        print(Node)

    def tree_Height(Node):
        if Node is None:
            return -1

            leftHeight = tree_Height(Node)
            rightHeight = tree_Height(Node)

            return 1 + max(leftHeight, rightHeight)


class cos_sim():

    fileB = open('glove.6B.50d.txt', 'r')
    fileC = open('glove.6B.100d.txt', 'r')

    sim = dl.get_close_matches

    s = 0

    newFileB = fileB.split()
    newFileC = fileC.split()

    for i in newFileB:
        if sim(i, newFileC[0]):
            s += 1
            n = float(s) / float(len(newFileB[0]))
            print('%d%% similarity',  int (n*100))


##main
fileA = open('glove.6B.50d.txt', 'r')

out = open("output.txt", 'w')

# move to a tree then call to the AVLTree or RBTNode class
# creating file for exercise 1 and 3
array_One = []

for line in fileA:
    for file in fileA:
        array_One.append(str(line))

out.write("length after adding txt file")
out.write(str(len(array_One)) + "\n")
out.close()


loop = 1
choice = 0

while loop == 0:
    print("Pick a tree method, your options are")
    print("2) Avl_Tree")
    print("3) Red/Black Tree")

choice = input("AVL Tree press 2, Black/Red Tree 1")
print("your choice was ", choice)


# operator chooses input and goes to that specified class
if choice == 2:
    array_One = AVLTree()
    print(array_One)

elif choice == 3:
    array_One = RBTNode()
    print(array_One)
    print("finished")

""""# create file for comparing two files exercise 2
fileB = open('glove.6B.50d.txt', 'r')
fileC = open('glove.6B.100d.txt', 'r')

output = open("outputB", 'w')

similar_Words = []

for line in fileB:
    for file in fileB:
        similar_Words.append(str(line))

output.write("Length after adding glove.6B.50d: ")
output.write(str(len(similar_Words)) + "\n")
output.close()

for line in fileC:
    for file in fileC:
        similar_Words.append(str(line))

output.write("Length after adding glove 6B.100d:")
output.write(str(len(similar_Words)) + "\n")
similar_Words = sim_Words()
print(similar_Words)"""