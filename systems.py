from components import Position, Velocity, Sprite

#System classes
class MovementSystem:
    @staticmethod
    def update(entities, dt):
        for entity in entities:
            if entity.has_component(Position) and entity.has_component(Velocity):
                position = entity.get_component(Position)
                velocity = entity.get_component(Velocity)
                position.x += velocity.dx * dt
                position.y += velocity.dy * dt


class RenderingSystem:
    @staticmethod
    def draw(entities, screen): 
        for entity in entities:
            if entity.has_component(Sprite) and entity.has_component(Position):
                sprite = entity.get_component(Sprite)
                position = entity.get_component(Position)
                screen.blit(sprite.image, (position.x, position.y))