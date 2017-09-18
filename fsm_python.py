
from pythonds import Stack

operators = ["*", "|"]

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
                if exprStack.size() == 0:
                    exprStack.push(Tree(operator, e2, Tree("")))
                else:
                    e1 = exprStack.pop()
                    exprStack.push(Tree(operator, e1, e2))

            operatorStack.push(i)

        elif i is ")":
            while operatorStack.peek() is not "(":
                operator = operatorStack.pop()

                e2 = exprStack.pop()
                if exprStack.size() == 0:
                    exprStack.push(Tree(operator, e2, Tree("")))
                else:
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

def inOrder(root, test):
    current = root
    s = []
    groups = Stack()
    res = []
    done = 0
    i= 0
    while (not done):

        if current is not None:
            s.append(current)
            current = current.left
        else:
            if (len(s) > 0):
                current = s.pop()
                if current.data == "*":
                    left_res, right_res = "", ""
                    if groups.size() == 0:
                        left = current.left.data
                        left_res = left
                        right = current.right.data
                        while left == test[i:i+len(left)]:
                            res.append(test[i:i+len(left)])
                            left_res += left
                            i += len(left)
                        else:
                            left = ""

                        if right == test[i:i+len(right)]:
                            res.append(test[i:i+len(right)])
                            right = test[i:i+len(right)]
                            i+=len(right)
                        elif test[i:i+len(right)] == "":
                            return False
                        elif right == "|":
                            current = current.right
                            continue

                        groups.push(left_res+right)

                    else:
                        left = groups.peek()
                        left_res = left
                        right = current.right.data
                        while left == test[i:i+len(left)]:
                            res.append(test[i:i+len(left)])
                            i += len(left)
                            left_res += left
                        print test[i:i+len(right)]
                        if right == test[i:i+len(right)]:
                            res.append(test[i:i+len(right)])
                            i+=len(right)
                        elif test[i:i+len(right)] == "":
                            return False
                        elif right == "|":
                            groups.push(left_res+right_res)
                            current = current.right
                            continue


                        groups.push(left_res+right)

                elif current.data == "|":
                    left = None
                    right = None
                    if groups.size() == 0 or current.left.left == None:
                        left = current.left.data
                        right = current.right.data
                    else:
                        left = groups.peek()
                        right = current.right.data

                    if right == test[i:i+len(right)]:
                        groups.push(test[i:i+len(right)])
                        res.append(test[i:i+len(right)])
                        i += len(test[i:i+len(right)])
                    elif left == test[i:i+len(left)]:
                        groups.push(test[i:i+len(left)])
                        res.append(test[i:i+len(left)])
                        i += len(test[i:i+len(left)])

                current = current.right
            else:
                done = 1
    return "".join(res)



#=============
input = "BC"
patt = "( ( ( B | D ) * C ) * A )"
t = parseTree(patt)
traverse(t)
ans = inOrder(t, input)
print "here", ans
#print check(input, patt)


#A * ( B | C )
#( ( B | D ) * C ) | A