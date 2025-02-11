import pygame, sys, asyncio
from pygame.locals import *
from Platform import Platform
from Bridge import *
from Character import *
from Water import *
from Bubble import *
from Cloud import *
from Flora import *
from random import randint

WEIDGH = 800
HEIGHT = 600


def load_image(filename, transparent=False):  # Funcion de cargar imagenes
    image = pygame.image.load(filename)
    # image = image.convert()
    if transparent:
        color = image.get_at((869, 166))
        image.set_colorkey(color, RLEACCEL)
    return image

pygame.init()
pygame.key.set_repeat(1, 1)
screen = pygame.display.set_mode((WEIDGH, HEIGHT))
clock = pygame.time.Clock()



char_list = []
water_list = []
bubbles = []
# flora=[]
max_bubbles = 2

# Carga las imagenes

image = load_image("images/Puentes.png", True)  # Carga la imagen con todas las imagenes

image_plat = image.subsurface(698, 0, 203, 128)  # Imagen de Plataformas del Centro
image_bridge = image.subsurface(675, 256, 250, 48)  # Imagen del puente
image_char0 = image.subsurface(105, 518, 32, 32)  # Imagen personaje parado
image_char1 = image.subsurface(137, 518, 32, 32)  # Imagenes personaje en movimiento
image_char2 = image.subsurface(169, 518, 32, 32)
image_char3 = image.subsurface(201, 518, 32, 32)
image_char4 = image.subsurface(233, 518, 32, 32)
image_cloud = image.subsurface(672, 544, 160, 64)  # Imagen de la nube grande
image_cloud2 = pygame.transform.scale(image_cloud, (200, 60))  # Imagen de la nube pequenya
image_water = image.subsurface(704, 352, 32, 64)  # Imagen agua
image_bubble = image.subsurface(676, 390, 25, 22)  # Imagen agua
image_tree = image.subsurface(800, 416, 96, 96)  # Imagen Arbol
image_grass = image.subsurface(672, 496, 32, 16)  # Imagen Hierba
image_bush = image.subsurface(704, 480, 32, 32)  # Imagen Arbusto
image_flower = image.subsurface(676, 512, 24, 32)  # Imagen Flor
image_mushroom = image.subsurface(712, 528, 16, 16)  # Imagen Champinyon
image_bigmushroom = image.subsurface(736, 512, 32, 32)  # Imagen Champinyon Grande

# Crea las Plataformas

platform1L = Platform(image_plat)
platform1L.set_pos(-90, 150)

platform2L = Platform(image_plat)
platform2L.set_pos(-90, 400)

platform1R = Platform(image_plat)
platform1R.set_pos(684, 150)

platform2R = Platform(image_plat)
platform2R.set_pos(684, 400)

platform1C = Platform(image_plat)
platform1C.set_pos(296, 150)

platform2C = Platform(image_plat)
platform2C.set_pos(296, 400)

# Crea los arboles

tree = Flora(image_tree)
tree.set_pos(300, 304)

tree2 = Flora(image_tree)
tree2.set_pos(760, 54)

# Crea los arbustos

bush1 = Flora(image_bush)
bush1.set_pos(720, 368)

bush2 = Flora(image_bush)
bush2.set_pos(745, 368)

bush3 = Flora(image_bush)
bush3.set_pos(770, 368)

# Crea las hierbas

grass1 = Flora(image_grass)
grass1.set_pos(434, 384)

grass2 = Flora(image_grass)
grass2.set_pos(404, 384)

grass3 = Flora(image_grass)
grass3.set_pos(374, 384)

grass4 = Flora(image_grass)
grass4.set_pos(50, 384)

grass5 = Flora(image_grass)
grass5.set_pos(0, 134)

grass6 = Flora(image_grass)
grass6.set_pos(32, 134)

grass7 = Flora(image_grass)
grass7.set_pos(64, 134)

grass8 = Flora(image_grass)
grass8.set_pos(310, 134)

grass9 = Flora(image_grass)
grass9.set_pos(342, 134)

grass10 = Flora(image_grass)
grass10.set_pos(374, 134)

grass11 = Flora(image_grass)
grass11.set_pos(406, 134)

grass12 = Flora(image_grass)
grass12.set_pos(438, 134)

# Crea los champinyones

mush1 = Flora(image_mushroom)
mush1.set_pos(730, 134)

mush2 = Flora(image_mushroom)
mush2.set_pos(342, 134)

# Crea los champinyones grandes

bmush1 = Flora(image_bigmushroom)
bmush1.set_pos(374, 118)

# Crea las flores

flower1 = Flora(image_flower)
flower1.set_pos(10, 368)

flower2 = Flora(image_flower)
flower2.set_pos(420, 368)

# Crea las  2 nubes

cloud = Cloud(image_cloud)
cloud.set_pos(randint(-150, 300), randint(10, 40))

cloud2 = Cloud(image_cloud2)
cloud2.set_pos(randint(500, 600), randint(200, 250))

# Crea el agua

for i in range(-128, int(WEIDGH / 32) + 128):
    water = Water(image_water)
    water.set_pos(i * 32, HEIGHT - 64)
    water_list.append(water)

# Crea el puente

bridge = Bridge(image_bridge)
bridge.set_pos(-500, 0)

# Guarda los objetos (menos el agua) en listas

objects = (cloud, cloud2, bridge, platform1L, platform2L, platform1R, platform2R, platform1C,
            platform2C)  # Guarda en una lista TODOS los objetos a mostrar
char_moves = (image_char1, image_char2, image_char3,
                image_char4)  # Guarda los movimientos de personaje en una lista para poder ser dada a la funcion move de la clase character.
flora = [grass5, grass6, grass7, grass8, grass9, grass10, grass11, grass12, mush2, bmush1, mush1, tree2, flower1,
            grass4, tree, grass1, grass2, grass3, flower2, bush1, bush2, bush3]

# Bucle principal
async def main():
    time_passed = 0
    while True:

        time = clock.tick(60)
        a = randint(0, 10)  # Valor movimiento agua

        # Generador de personajes

        time_passed += time
        if time_passed % 50 == 0:  # Modificar n el futuro (+ distancia entre personajes tiene que ser mayor a X, siendo X constante)
            # Crea el personaje
            char = Character(image_char0)
            spawn_point = randint(0, 3)
            char.spawn(spawn_point)
            if len(char_list) < 2:
                char_list.append(char)

        # Generador de burbujas

        if len(bubbles) < max_bubbles:
            bubble = Bubble(image_bubble)
            bubble.set_pos(randint(0, WEIDGH), randint(HEIGHT, HEIGHT + 100))
            bubbles.append(bubble)

            # Control de los inputs del raton

        if pygame.mouse.get_pressed()[0] == 1:
            mousex, mousey = pygame.mouse.get_pos()

            # Posicion del puente segun donde se haya clickeado.

            if mousey <= HEIGHT / 2:
                if mousex <= WEIDGH / 2:
                    bridge.set_pos(80, 118)
                else:
                    bridge.set_pos(468, 118)
            else:
                if mousex <= WEIDGH / 2:
                    bridge.set_pos(80, 368)
                else:
                    bridge.set_pos(468, 368)

                    # Control de Escape

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()

                # Comprobador de colisiones

        for i in range(len(char_list)):
            for j in range(2, len(objects)):
                if char_list[i].Collision(objects[j].CollisionBox()):  # Comprueba si el personaje esta cayendo o no.
                    char_list[i].on_ground = True
                    break
                else:
                    char_list[i].on_ground = False

            # Hace caer el personaje si no esta en el suelo

            if char_list[i].on_ground == False or (char_list[i].centery() > HEIGHT / 2 and (
                    char_list[i].direction == 0 or char_list[i].direction == 2)):
                char_list[i].Gravity(
                    time)  # El or es para que los personajes que caen de las plataformas de arriba no seas capaces de colisionar con los puentes de abajo.

            # Mueve el personaje en la direccion correspondiente y devuelve la imagen del frame correspondiente
            char_list[i].image = char_list[i].move(time, char_moves)

            # Borrar Persoanjes

            if char_list[i].centery() > HEIGHT:
                char_list.remove(char_list[i])
                break

        # Mover nubes
        cloud.move(time, WEIDGH)
        cloud2.move(time, WEIDGH, 1)

        # Dibujo de la pantalla

        screen.fill((85, 180, 255))

        screen.blit(objects[0].image, objects[0].rect)  # Dibuja las nubes
        screen.blit(objects[1].image, objects[1].rect)

        for i in range(len(water_list)):  # Dibuja y MUEVE el agua
            water_list[i].move(a)
            screen.blit(water_list[i].image, water_list[i].rect)

        for i in range(len(bubbles)):  # Dibuja y MUEVE las burbujas
            bubbles[i].move(time, HEIGHT, WEIDGH)
            screen.blit(bubbles[i].image, bubbles[i].rect)

        for i in range(len(flora)):  # Dibuja la vegetacion del mapa(arboles,plantas,hierba)
            screen.blit(flora[i].image, flora[i].rect)

        for i in range(len(char_list)):  # Dibuja los personajes.
            screen.blit(char_list[i].image, char_list[i].rect)
            # pygame.draw.rect(screen,(255,0,0),char_list[i].CollisionBox(),1)

        for i in range(2, len(objects)):
            screen.blit(objects[i].image, objects[i].rect)  # Dibuja las plataformas y el puente.
            # pygame.draw.rect(screen,(255,0,0),objects[i].CollisionBox(),1)

        pygame.display.update()
        await asyncio.sleep(0)

asyncio.run(main())
