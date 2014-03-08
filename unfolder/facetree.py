class Node:
    """ Nodes of a face tree.

    A face tree structure, where each sibling face only shares one edge with its parent.
    """
    def __init__(self, face):
        """ Create a new face tree with a root face.
        """
        self.face = face
        self.children = []
        self.parent = None

    def addChild(self, childFace):
        """ Create a child to this node and return it.
        """
        child = Node(childFace)
        self.children.append(child)
        return child

    def remove(self):
        """ Remove this node from the tree and return its parent.
        """
        parent = self.parent
        if self.parent:
            parent.children.remove(self)
            return parent
        return None

    def getFaces(self):
        """ Return all faces in the face tree.
        """
        faces = [self.face]
        for child in self.children:
            faces.extend(child.getFaces())
        return faces

    def findSubtree(self, rootValue):
        """ Find the node in the tree that matches a certain face.
        """
        if self.value == rootValue:
            return self
        for child in self.children:
            subtree = child.findSubtree(rootValue)
            if subtree:
                return subtree
        return None


    def sf(self, offset = 0):
        """ Debuging output of a face tree.
        """
        res = " " * offset + str(self.face) + '\n'
        for child in self.children:
            res += child.sf(offset + 1)
        return res
