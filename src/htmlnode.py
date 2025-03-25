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
    
