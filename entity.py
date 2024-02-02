#Entity class
class Entity:
    _next_id = 0

    def __init__(self, id):
    
        self.components = {}
        self.id = id

    def add_component(self, component):
        component_type = type(component)
        self.components[component_type] = component

    def remove_component(self, component_type):
        if component_type in self.components:
            del self.components[component_type]

    def has_component(self, component_type):
        return component_type in self.components

    def get_component(self, component_type):
        return self.components.get(component_type, None)
