import circleshape, pygame, random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_state, log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y, radius)

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            old_position = self.position
            old_velocity = self.velocity
            self.kill()
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            new_first_vector = old_velocity.rotate(new_angle)
            new_second_vector = old_velocity.rotate(new_angle * (-1))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            daugther_asteroid = Asteroid(old_position[0], old_position[1], new_radius)
            daugther_asteroid.velocity = new_first_vector * 1.2
            son_asteroid = Asteroid(old_position[0], old_position[1], new_radius)
            son_asteroid.velocity = new_second_vector * 1.2
