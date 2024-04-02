import pygame
import sys

from basesita_personajes import list_personajes

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir la configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu Arrow Key")

# Definir las opciones del menú
#menu_options = ["Option 1", "Option 2", "Option 3"]
menu_options = list_personajes
selected_option = 0

# Definir la fuente
font = pygame.font.Font(None, 36)

# Función para dibujar el menú
def draw_menu():
    screen.fill(WHITE)
    for i, option in enumerate(menu_options):
        text = font.render(option.nombre, True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + i * 40 - len(menu_options)*20))
        screen.blit(text, text_rect)
        if i == selected_option:
            pygame.draw.rect(screen, RED, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20), 3)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                print("Selected:", menu_options[selected_option])
                # Aquí puedes añadir la lógica para lo que quieras hacer con la opción seleccionada

    # Dibujar el menú
    draw_menu()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de cuadros por segundo
    pygame.time.Clock().tick(30)

# Salir del programa
pygame.quit()
sys.exit()



    