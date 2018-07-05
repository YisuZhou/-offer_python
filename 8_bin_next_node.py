'''
给定一个二叉树和其中的一个结点，
请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

class BinTree:
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:


    
    def getnext_node(self,p_node):
        if p_node.right != None:#有右子树，找到右子树的最左节点
            while(p_node.left != None):
                p_node = p_node.left
            return p_node

        if p_node.right == None:#没有右子树，回溯找到父节点，并且判断自己是左支还是右支
            while (p_node.parent != None):
                if p_node.parent.right == p_node:#自己就是右支，继续回溯
                    p_node = p_node.parent
                elif p_node.parent.left == p_node:#自己是左支，那就是父节点
                    return p_node.parent
            #就它一个
            return None
            


        #空
        return 
            
            
        
