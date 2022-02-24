class Author:
    
    def __init__(self, name):
        self.name = name
        self.refs = list()
        
    def add_ref(self, ref):
        self.refs.append(ref)
        
    def get_refs(self):
        return self.refs
    
    def get_name(self):
        return self.name