class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
       

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        result = ""
        
        for key, value in self.props.items():
            
            result += f' {key}="{value}"'
        
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("All leaf nodes must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
        
       
        

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag == None:
            
            return self.value
        
        props_html = super().props_to_html()
       
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
    def __eq__(self, other):
        
        if not isinstance(other, LeafNode):
            return False

        
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props)
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("All ParentNodes must have a tag")
        if not children:
            raise ValueError("All ParentNodes must have children")
        
        for child in children:
            if not isinstance(child, HTMLNode):
                raise TypeError("All children of ParentNode must be instances of HTMLNode")
        
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All ParentNodes must have a tag")
        if self.children is None:
            raise ValueError("All ParentNodes must have children")
        
        props_html = self.props_to_html()
        
        children_html = "".join(child.to_html() for child in self.children)
        
        if self.tag == "code":
            return f"<{self.tag}{props_html}>{children_html}\n</{self.tag}>"
      
     
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"



    
