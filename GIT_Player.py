# project GIT GAME


import pygame
import time

# Initialiser Pygame
pygame.init()

# Définir la taille de l'écran
screen = pygame.display.set_mode((800, 600))

# Définir la taille de la carte
MAP_WIDTH = 10
MAP_HEIGHT = 5
TILE_SIZE = 80  # Supposons que chaque case mesure 80 pixels

# Définir la classe Joueur
class Player:
    def __init__(self, x, y, color):
        self.stamina = 50  # Endurance initiale
        self.base_health = 1000  # Points de vie de base
        self.health = self.calculate_health()  # Calculer les points de vie initiaux
        self.stamina_recovery_rate = 1  # Valeur de récupération d'endurance par seconde
        self.x = x
        self.y = y
        self.color = color  # Couleur du joueur

    def calculate_health(self):
        return self.base_health + (self.stamina * 10)

    def recover_stamina(self):
        if self.stamina < 100:  # Supposons que l'endurance maximale est de 100
            self.stamina += self.stamina_recovery_rate
            if self.stamina > 100:
                self.stamina = 100
            self.health = self.calculate_health()  # Mettre à jour les points de vie

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        # S'assurer que le joueur ne sort pas des limites de la carte
        if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
            self.x = new_x
            self.y = new_y

# Définir la sous-classe Ice
class Ice(Player):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 0, 255))  # Bleu

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        # S'assurer que le joueur reste dans la moitié gauche de la carte
        if 0 <= new_x < MAP_WIDTH // 2 and 0 <= new_y < MAP_HEIGHT:
            self.x = new_x
            self.y = new_y

# Définir la sous-classe Fire
class Fire(Player):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 0, 0))  # Rouge

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        # S'assurer que le joueur reste dans la moitié droite de la carte
        if MAP_WIDTH // 2 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
            self.x = new_x
            self.y = new_y

# Créer des instances de joueur
ice_player = Ice(2, 2)  # Coordonnées initiales (2, 2)
fire_player = Fire(7, 2)  # Coordonnées initiales (7, 2)

# Créer un objet horloge
clock = pygame.time.Clock()

# Boucle principale du jeu
running = True
last_recovery_time = time.time()  # Enregistrer la dernière fois de récupération d'endurance
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtenir le temps actuel
    current_time = time.time()
    # Récupérer l'endurance chaque seconde
    if current_time - last_recovery_time >= 1:
        ice_player.recover_stamina()
        fire_player.recover_stamina()
        last_recovery_time = current_time

    # Effacer l'écran
    screen.fill((0, 0, 0))

    # Afficher l'endurance et les points de vie des joueurs
    font = pygame.font.Font(None, 36)
    ice_stamina_text = font.render(f'Ice Stamina: {ice_player.stamina}', True, (0, 255, 255))
    ice_health_text = font.render(f'Ice Health: {ice_player.health}', True, (0, 255, 255))
    fire_stamina_text = font.render(f'Fire Stamina: {fire_player.stamina}', True, (255, 69, 0))
    fire_health_text = font.render(f'Fire Health: {fire_player.health}', True, (255, 69, 0))
    screen.blit(ice_stamina_text, (50, 50))
    screen.blit(ice_health_text, (50, 100))
    screen.blit(fire_stamina_text, (500, 50))
    screen.blit(fire_health_text, (500, 100))

    # Afficher la position des joueurs
    ice_pos_text = font.render(f'Ice Position: ({ice_player.x}, {ice_player.y})', True, (0, 255, 255))
    fire_pos_text = font.render(f'Fire Position: ({fire_player.x}, {fire_player.y})', True, (255, 69, 0))
    screen.blit(ice_pos_text, (50, 150))
    screen.blit(fire_pos_text, (500, 150))

    # Dessiner les joueurs
    ice_rect = pygame.Rect(ice_player.x * TILE_SIZE, ice_player.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    fire_rect = pygame.Rect(fire_player.x * TILE_SIZE, fire_player.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, ice_player.color, ice_rect)
    pygame.draw.rect(screen, fire_player.color, fire_rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Contrôler la cadence
    clock.tick(60)  # 60 images par seconde

# Quitter Pygame
pygame.quit()
