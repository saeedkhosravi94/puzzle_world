import pygame

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def puzzle(self):

        pass

    def pannel(self):

        pass


    def update(self):

        self.puzzle()
        self.pannel()

    def run(self):

        while self.running:

            self.handle_events()
            self.update()
            pygame.display.flip()

if __name__ == "__main__":

    Game().run()
