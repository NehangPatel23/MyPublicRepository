# Tree Implementation Example

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()
        
        


def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("MacBook"))
    laptop.addChild(TreeNode("SurfaceBook"))
    laptop.addChild(TreeNode("ThinkPad"))
    
    cellphone = TreeNode("Cell Phones")
    cellphone.addChild(TreeNode("iPhone"))
    cellphone.addChild(TreeNode("Google Pixel"))
    cellphone.addChild(TreeNode("OnePlus"))
    
    tv = TreeNode("Television")
    tv.addChild(TreeNode("LG"))
    tv.addChild(TreeNode("Samsung"))
    
    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(tv)
    
    return root


if __name__ == "__main__":
    root = build_product_tree()
    print(root.getLevel())
    root.printTree()
    pass
