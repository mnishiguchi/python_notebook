class Member(object):
    """ represents a single person in the family """
    
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


## **** TODO ****
## You may assume that the class Member is defined for you.
## You should not alter Member in any way,
## but may alter any part of Family that you deem necessary.

class Family(object):
    """ represents the whole family tree """
    
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """
        self.names_to_nodes = {}      # a dict of name => Member object
        self.founder = founder           # name of the founder (type str)
        self.root = Member(founder)      # create the root node (type Member)
        self.names_to_nodes[founder] = self.root   # set the root on the tree
              
    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         

    def get_children(self, mother):
        """
        Get all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        return: list_of_children
        """ 
        return [ child.name for child in self.names_to_nodes[mother].children ]
        
    def get_node(self, name):
        """
        Find a node by name

        Keyword arguments: 
        name -- mother's name as a string
        return: a Member object
        """ 
        return self.names_to_nodes[name]  
        
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)
        
    def get_ancestors(self, name):
        """
        param: name - a string
        return: ancestors - a list of Member objects
        """
        if name == self.founder:
            return []
        
        ancestors = []    # a list of ancestors
            
        # initialize ancestor to parent
        node = self.names_to_nodes[name]
        ancestor = node.get_parent()
            
        while True:   
            # append to list
            ancestors.append(ancestor)
            #  quit if founder is reached
            if ancestor == self.root:
                break
            # move up the tree
            ancestor = ancestor.get_parent()
        return ancestors
            
    def cousin(self, a, b):
        """
        Evaluate the cousin type of two Member objects 
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        **** cousin type ****
          -1 if a and b are the SAME NODE.
          -1 if either one is a DIRECT DESCENDANT of the other
          
          >=0 otherwise,  
          DISTANCE from each node to the common ancestor.
          Then cousin type is set to the smaller of the two distances,
          as described in the exercises above

        **** degrees removed ****
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        # get nodes
        node_a = self.get_node(a)
        node_b = self.get_node(b)
        
        # get anscestors
        ancestors_a = self.get_ancestors(a)
        ancestors_b = self.get_ancestors(b)
        
        #==== eliminate non-cousins ====
        # a and b are the same node.
        if node_a == node_b:
            return (-1, 0) 
                                            
        # either a, nor b is the root node
        if node_a == self.root or node_b == self.root:
            degreeRemoved = abs( len(ancestors_a) - len(ancestors_b) )
            return (-1, degreeRemoved)
                             
        # either one is a DIRECT DESCENDANT of the other
        if  node_a in ancestors_b or   node_b in ancestors_a:
            degreeRemoved = abs( len(ancestors_a) - len(ancestors_b) )
            return (-1, degreeRemoved)       
            
        #==== evaluate cousins ====
        # remove common anscestors from the lists, except the closest one
        def removeCommonAncestors(ancestors_a, ancestors_b)  :
            """(ancestors_a, ancestors_b)  --- lists of Member objects"""
                    
            while True:
                len_a, len_b = len(ancestors_a), len(ancestors_b)
                
                # if either list length is 1, do nothing
                if len_a == 1 or len_b == 1:
                    return None  
                       
                # if last elems and 2nd last ones are identical
                if ancestors_a[-1] ==  ancestors_b[-1] and ancestors_a[-2] ==  ancestors_b[-2]:
                    ancestors_a.pop()    # shrink by one elem
                    ancestors_b.pop()    # shrink by one elem
                else:
                    return None
        removeCommonAncestors(ancestors_a, ancestors_b)       
            
        # determine cousin type
        len_a, len_b = len(ancestors_a), len(ancestors_b)
        if len_a == len_b:
            ( cousinType, degreeRemoved ) = ( len_a - 1 , 0 )
        elif  len_a > len_b:
            ( cousinType, degreeRemoved ) = ( len_b - 1 , abs(len_a - len_b) )
        else:
            ( cousinType, degreeRemoved ) = ( len_a - 1 , abs(len_a - len_b) )

        # Returns a tuple of (the cousin type, degree removed) 
        return ( cousinType, degreeRemoved )
    
f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

## These are your test cases. 

## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'
t, r = f.cousin("b", "c")
print "'b' is a", words[t],"cousin", r, "removed from 'c'"

## For the remaining test cases, use the graph to figure out what should 
## be printed, and make sure that your code prints out the appropriate values.

t, r = f.cousin("d", "f")
print "'d' is a", words[t],"cousin", r, "removed from 'f'"

t, r = f.cousin("i", "n")
print "'i' is a", words[t],"cousin", r, "removed from 'n'"

t, r = f.cousin("q", "e")
print "'q' is a", words[t], "cousin", r, "removed from 'e'"

t, r = f.cousin("h", "c")
print "'h' is a", words[t], "cousin", r, "removed from 'c'"

t, r = f.cousin("h", "a")
print "'h' is a", words[t], "cousin", r, "removed from 'a'"

t, r = f.cousin("h", "h")
print "'h' is a", words[t], "cousin", r, "removed from 'h'"

t, r = f.cousin("a", "a")
print "'a' is a", words[t], "cousin", r, "removed from 'a'"

t, r = f.cousin("h", "e")
print "'h' is a", words[t], "cousin", r, "removed from 'e'"

t, r = f.cousin("f", "n")
print "'f' is a", words[t], "cousin", r, "removed from 'n'"

t, r = f.cousin("d", "e")
print "'d' is a", words[t],"cousin", r, "removed from 'e'"

t, r = f.cousin("q", "n")
print "'q' is a", words[t], "cousin", r, "removed from 'n'"