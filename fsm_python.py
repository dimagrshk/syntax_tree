"""
def star(sym):
    return sym

def pipe(sym_1, sym_2, key):
    if key is 1:
        return sym_1
    else:
        return sym_2

def group(*args):
    return "".join(args)


def fms(alph):
    ls = []
    for i in range(10):
        for j in range(1,3):
            pattern = group(star("A")*i, group(pipe("B", "DA", j)), "D")
            ls.append(pattern)
    return ls
"""


class Tree(object):
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None
        #self.children = [self.left, self.right]

    def insertLeft(self, data_left = None):
        self.left = Tree()
        self.left.data = data_left

    def insertRight(self, data_right = None):
        self.right = Tree()
        self.right.data = data_right

    def getLeftChild(self):
        return self.left.data

    def getRightChild(self):
        return self.right.data




def buildTree(pattern):
    pattern = pattern.split()
    tree = Tree()
    cur_tree = tree
    parent_list = []
    for i in pattern:
        if i is "(":
            cur_tree.insertLeft("")
            parent_list.append(cur_tree)
            cur_tree = cur_tree.left
        elif i not in ["*", "|", ")"]:
            cur_tree.data = i
            parent = parent_list[-1]
            cur_tree = parent
        elif i in ["*", "|"]:
            cur_tree.data = i
            cur_tree.insertRight("")
            parent_list.append(cur_tree)
            cur_tree = cur_tree.right
        elif i is ")":
            cur_tree = parent_list[-1]
        else:
            raise ValueError
    return tree



def traverse(tr):
    thislevel = [tr]
    while thislevel:
        nextlevel = list()
        for n in thislevel:
            print n.data,
            if n.left: nextlevel.append(n.left)
            if n.right: nextlevel.append(n.right)
        print
        thislevel = nextlevel


def starCheck(leaf, test):
    if leaf is test:
        return True
    else:
        return False

def check(template, pattern):
    tree = buildTree(pattern)
    ls_check = []
    ret = False
    curTree = tree
    index = 0
    while curTree:
       curData = curTree.data
       if curData is "*":
           leaf = curTree.getLeftChild()
           while leaf is template[index:index+len(leaf)]:
               index += len(leaf)
               ls_check.append(1)
           curTree = curTree.right
           curData = curTree.data
       elif curData is template[index:index+len(curData)]:
           ls_check.append(1)
           curTree = curTree.right
       else: break

    if len(ls_check) == len(template):
        return True
    return False




#=============
input = "AAAAAB"
patt = "( A * B )"
t = buildTree(patt)
traverse(t)
print check(input, patt)
