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

def checkPipe(l, r, test):
    if test is l or test is r:
        return test
    else:
        return False

def inOrder(root, test):
    current = root
    s = []
    groups = Stack()
    res = []
    #e1, e2, op = "", "", ""
    done = 0
    i, gap = 0, 0
    while (not done):
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if (len(s) > 0):
                current = s.pop()
                if current.data is "*":
                    print "{", current.data, "}",
                    if groups.size() != 0:
                        left = groups.peek()
                        while starCheck(left, test[i:i + len(left)]):
                            res.append(test[i:i + len(left)])
                            i += len(left)
                    print res, i
                    right = current.right.data
                    if right is test[i]:
                        if groups.size() != 0:
                            e1 = groups.peek()
                            e2 = right
                            groups.push(e1 + e2)
                            i += 1
                            res.append(right)


                elif current.data is "|":
                    print "[", current.data, "]",
                    left = current.left.data
                    right = current.right.data
                    if left is test[i:i + len(left)] or right is test[i]:
                        res.append(test[i])
                        groups.push(res[-1])
                        i += len(left)
                    print res, i

                else:
                    print current.data,
                    if groups.size() == 0:
                        groups.push(current.data)

                current = current.right
            else:
                done = 1
    return "".join(res)



#=============
input = "BBC"
patt = "( ( A | B ) * C )"
t = parseTree(patt)
traverse(t)
ans = inOrder(t, input)
print "here", ans
#print check(input, patt)


