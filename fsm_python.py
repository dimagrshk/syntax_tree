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

from pythonds import Stack
from collections import deque

operators = { "*":1, "|":1}

##==========================================================
class Tree(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left

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

    def ExprNode(self, data):
        self.data = data
        self.right = None
        self.left = None



##==========================================================

def parseTree(pattern):
    pattern = pattern.split()
    tree = Tree()
    operatorStack = Stack()
    exprStack = Stack()
    for i in pattern:
        #print i
        if i is "(":
            operatorStack.push(i)

        elif i in ["A", "B", "D", "C"]:
            exprStack.push(Tree(i))

        elif i in ["*", "|"]:
            if operatorStack.size() == 0:
                operator = operatorStack.pop()
                e2 = exprStack.pop()
                e1 = exprStack.pop()
                exprStack.push(Tree(operator, e1, e2))

            operatorStack.push(i)

        elif i is ")":
            while operatorStack.peek() is not "(":
                operator = operatorStack.pop()

                e2 = exprStack.pop()
                e1 = exprStack.pop()
                exprStack.push(Tree(operator, e1, e2))
            operatorStack.pop()

        else:
            raise ValueError

    return exprStack.pop()

##==========================================================
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

##==========================================================
def starCheck(leaf, test):
    if leaf is test:
        return True
    else:
        return False

def check(template, pattern):
    tree = parseTree(pattern)
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
       elif curData is "|":
           var_1 = curTree.getLeftChild()
           var_2 = curTree.getRightChild()
           if template[index] is var_1 or template[index] is var_2:
               ls_check.append(1)
               print template[index]
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
input = "AAAAAC"
patt = "( ( ( C | B ) * C ) * A )"
t = parseTree(patt)
traverse(t)
#print check(input, patt)


