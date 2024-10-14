import pyautogui as pg
import time

image_list = [
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar2.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa2.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar3.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar3.2.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectartrigo1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa3.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar4.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar4.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa4.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\gobio5.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\salvia5.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa5.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\gobio6.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\gobio6.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa6.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar7.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa7.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar8.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa8.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa8.5.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar9.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa9.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar10.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar10.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar10.2.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar10.3.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa10.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar11.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar11.2.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar11.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa11.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar12.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa12.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar13.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar13.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar13.2.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa13.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar14.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar14.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar14.2.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar14.3.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa14.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar15.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar15.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar15.2.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa15.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar16.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar16.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa16.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar17.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\recolectar17.1.png",
    r"C:\Users\Sebastian\OneDrive\Escritorio\AlquimistaAstrub\pasamapa17.png",
    
]

def checkImage(image_path):
    try:
        pos = pg.locateOnScreen(image_path, confidence=0.8)
        if pos:
            # Mover al centro de la imagen detectada
            center_x = pos.left + pos.width // 2
            center_y = pos.top + pos.height // 2
            pg.moveTo(center_x, center_y)
            pg.click()
            time.sleep(1)  # Espera antes de seguir con la siguiente imagen
        else:
            print(f"No se encontró la imagen: {image_path}")
    except:
        print(f"Error al procesar la imagen: {image_path}")

for image in image_list:
    checkImage(image)
    time.sleep(7)  # Espera 2 segundos entre cada búsqueda