'''This is free software created by Boomer Rogers and distributed under the GNU General Public License (2013) and is intended for non-commercial education purposes.'''

from lib.board_settings.boardsettings import *
from lib.minimax_AI.minimaxAI import *

class gameStart(object):

    def mainGame(self):
        pygame.init()
        pygame.display.set_caption('Tic-Tac-War')
        mainBoard = graphical_board.generateNewBoard(80)
        turn = random.choice(['computer', 'player'])
        gamestate = 1


        toggle_on = (['on'])
        music_on = load_data.loadPng('musicon.png')
        toggle_yes = music_on.get_rect()
        music_off = load_data.loadPng('musicoff.png')
        toggle_off = music_off.get_rect()
        window_set.surface.blit(music_on, toggle_yes)

        while gamestate == 1:
            player = 'X'

            if board_data.boardComplete():

                computer_win = load_data.loadPng('resetcomputerwon.png')
                display_reset = computer_win.get_rect(center=(window_set.window_width/2, window_set.window_height/2))

                play_again = load_data.loadPng('playagain.png')
                reset_yes = play_again.get_rect(center=(window_set.window_width/2 + 80,window_set.window_height/2 + 60))

                exit_game = load_data.loadPng('exitbutton.png')
                exit_yes = play_again.get_rect(center=(window_set.window_width/2 - 80, window_set.window_height/2 + 60))

                draw_game = load_data.loadPng('drawbox.png')
                display_draw = draw_game.get_rect(center=(window_set.window_width/2, window_set.window_height/2))
                    
                if board_data.winner() == 'O':
                    window_set.surface.blit(computer_win, display_reset)
                    window_set.surface.blit(play_again, reset_yes)
                    window_set.surface.blit(exit_game, exit_yes)
                    
                if board_data.winner() == None:
                    window_set.surface.blit(draw_game, display_draw)
                    window_set.surface.blit(play_again, reset_yes)
                    window_set.surface.blit(exit_game, exit_yes)

                for event in pygame.event.get():
 
                    if event.type == MOUSEBUTTONUP:
                        load_data.soundEffect()
                        spotx, spoty = pygame.mouse.get_pos()
                        if reset_yes.collidepoint((spotx, spoty)):
                            mainBoard = graphical_board.generateNewBoard(80)
                            window_set.surface.blit(music_on, toggle_yes)
                            board_data.all_positions = [0,0,0,0,0,0,0,0,0]

                        if exit_yes.collidepoint((spotx, spoty)):
                            gameExit()

                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        gameExit()

            if turn == 'player':
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        load_data.soundEffect()
                        posx, posy = pygame.mouse.get_pos()
                        if toggle_yes.collidepoint((posx, posy)) and toggle_on == ['on']:
                            pygame.mixer.music.pause()
                            toggle_on = ['off']
                            window_set.surface.blit(music_off, toggle_off)

                        elif toggle_off.collidepoint((posx, posy)) and toggle_on == ['off']:
                            pygame.mixer.music.unpause()
                            toggle_on = ['on']
                            window_set.surface.blit(music_on, toggle_yes)

                        player_move = graphical_board.movePosition(mainBoard, board_data, player)
                        if not player_move in board_data.trackMovesLeft():
                            continue
                        board_data.makeMove(player_move, player)
                        turn = 'computer'

                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        gameExit()

            elif turn == 'computer':
                '''Make the computer seem like it's thinking'''
                pauseUntil = time.time() + random.randint(2,5)*0.2

                while time.time() < pauseUntil:
                    pygame.display.update()

                player = getEnemy(player)
                makecomp_move = computer_move.determine(board_data, player)
                board_data.makeMove(makecomp_move, player)
                load_data.soundEffect()
                turn = 'player'

            pygame.display.update()

game_start = gameStart()

if __name__ == '__main__':
    load_data.getMusic()
    game_start.mainGame()
