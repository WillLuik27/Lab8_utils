
from linkedbst import LinkedBST

def testtree():
    print("Adding A B C D E F G")
    skinny = LinkedBST("A B C D E F G".split())

    print("\nString for skinny tree:\n" + str(skinny))

    print("Adding D B A C F E G")
    bushy = LinkedBST("D B A C F E G".split())

    print("\nString for bushy tree:\n" + str(bushy))

    print("\nExpect True for A in bushy tree: ", "A" in bushy)

    clone = LinkedBST(bushy)
    print("\nClone of bushy tree:\n" + str(clone))
    
    print("Expect True for bushy tree == clone: ", bushy == clone)

    print("\nFor loop: ", end="")
    for item in bushy:
        print(item, end=" ")

    print("\n\ninorder traversal: ", end="")
    for item in bushy.inorder(): print(item, end = " ")
    
    print("\n\npreorder traversal: ", end="")
    for item in bushy.preorder(): print(item, end = " ")
    
    print("\n\npostorder traversal: ", end="")
    for item in bushy.postorder(): print(item, end = " ")
    
    print("\n\nlevelorder traversal: ", end="")
    for item in bushy.levelorder(): print(item, end = " ")

    print("\n\nRemoving all items:", end = " ")
    for item in "ABCDEFG":
        print(bushy.remove(item), end=" ")

    print("\n\nExpect 0: ", len(bushy))

    tree = LinkedBST(range(1, 16))
    print("\nAdded 1..15:\n" + str(tree))
    
    lyst = list(range(1, 16))
    import random
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree))

    tree = LinkedBST(list("DBACFEG"))
    print("Added " + str(list("DBACFEG")))
    print(tree)
    print("Expect exception, trying to mutate in a for loop")
    count = 1
    for item in tree:
        tree.add(item + str(count))
        count += 1



def testbalance():
    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print("\nString:\n" + str(tree))
    print("\nLength:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    tree = LinkedBST(range(1, 16))
    print("\nAdded 1..15:\n" + str(tree))
    print("\nLength:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    tree.rebalance()
    print("\nAfter rebalance:\n" + str(tree))
    print("\nLength:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    lyst = list(range(1, 16))
    import random
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree))
    print("\nLength:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())


if __name__ == "__main__":
    testtree()
    #testbalance()