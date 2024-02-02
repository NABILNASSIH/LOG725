from components import *

#System classes
class MovementSystem:
    @staticmethod
    def update(entities, dt):
        for entity in entities:
            if entity.has_component(Position_Component) and entity.has_component(Velocity_Component):
                position = entity.get_component(Position_Component)
                velocity = entity.get_component(Velocity_Component)
                position.x += velocity.dx * dt
                position.y += velocity.dy * dt


class RenderingSystem:
    @staticmethod
    def draw(entities, screen): 
        for entity in entities:
            if entity.has_component(Sprite_Component) and entity.has_component(Position_Component):
                sprite = entity.get_component(Sprite_Component)
                position = entity.get_component(Position_Component)
                screen.blit(sprite.image, (position.x, position.y))