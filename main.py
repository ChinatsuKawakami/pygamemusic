import pygame.mixer
import time


#create main to listen to music
def main():
    pygame.mixer.init(frequency=44100)
    pygame.mixer.music.load("9784864715225.mp3")
    pygame.mixer.music.play(1)
    time.sleep(100)
    pygame.mixer.music.stop()


if __name__ == '__main__':
    main()
