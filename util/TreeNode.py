class TreeNode():
    # 初始化一个节点
    def __init__(self,val = None):
        self.val = val       # 节点值
        self.l_child = []    # 子节点列表
        self.now_node=None
        self.leaves=[]
    # 添加子节点
    def add_child(self,node):
        self.l_child.append(node)
    def search(self,tar,tn=None):
        if tn==None:
            tn=self
        if not tn:
            self.now_node = None
            return
        if tn.val['id']==tar:
            self.now_node=tn
            return
        for i in tn.l_child:
            self.search(tar,i)
    def findSons(self,father):
        self.search(father)
        return self.now_node.l_child
    def searchLeaves(self,tn=None):
        if tn==None:
            tn=self
        if not tn:
            return
        if len(tn.l_child)==0:
            self.leaves.append(tn.val)
            return
        for i in tn.l_child:
            self.searchLeaves(i)
    def findLeaves(self):
        self.leaves.clear()
        self.searchLeaves()
        return self.leaves
if __name__ == '__main__':
    root = TreeNode('A')
    B = TreeNode('B')
    root.add_child(B)
    root.add_child(TreeNode('C'))
    D = TreeNode('D')
    root.add_child(D)
    B.add_child(TreeNode('E'))
    B.add_child(TreeNode('F'))
    B.add_child(TreeNode('G'))
    D.add_child(TreeNode('H'))
    D.add_child(TreeNode('I'))

    root.search('A')
    print(root.now_node.l_child)

