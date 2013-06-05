from lib.window_settings.windowsettings import *

class loadMedia(object):

    def loadPng(self, name):

        fullname = os.path.join('lib/data/images', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error:
            print 'Seems like I lost your image:', fullname
            raise SystemExit
        return image

    def drawPlayer(self, tilex, tiley, number, adjx = 0, adjy = 0):
    
        left, top = window_set.getLeftTopCoords(tilex, tiley)
        player_image = self.loadPng("player.png")
        resizePlayer = pygame.transform.scale(player_image, (window_set.x_size, window_set.x_size))
        window_set.surface.blit(resizePlayer, (left + adjx, top + adjy))

    def drawComputer(self, tilex, tiley, number, adjx = 0, adjy = 0):
        
        left, top = window_set.getLeftTopCoords(tilex, tiley)
        computer_image = self.loadPng("computer.png")
        resizeComputer = pygame.transform.scale(computer_image, (window_set.x_size, window_set.x_size))
        window_set.surface.blit(resizeComputer, (left + adjx, top + adjy))

    def drawSquare(self, tilex, tiley, number, adjx = 0, adjy = 0):

        left, top = window_set.getLeftTopCoords(tilex, tiley,) 
        pygame.draw.rect(window_set.surface, ((0,0,0)), (left + adjx, top + adjy, window_set.box_size, window_set.box_size))

    def soundEffect(self):
        sound_effect = pygame.mixer.Sound("lib/data/sounds/soundeffect.ogg")
        sound_effect.set_volume(0.5)
        sound_effect.play()

    def getMusic(self):
        pygame.mixer.init()
	pygame.mixer.music.load('lib/data/sounds/skye.ogg')
	pygame.mixer.music.play(-1)

load_data = loadMedia()
