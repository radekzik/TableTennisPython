import pygame

from pong_game.config.settings import Settings
from pong_game.handler.keybinds import KeyBinds
from pong_game.loop_functions.functions import LoopFunctions, Collisions
from pong_game.objects.ball import Ball
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class MatchLoop:
    @staticmethod
    def loop(f_player, s_player, ball, background, table, match_restart):

        pygame.event.set_allowed(pygame.KEYDOWN)

        game_loop = 1

        Settings.countdown = 5
        Settings.last_count = pygame.time.get_ticks()

        while 1:

            clock = pygame.time.Clock()

            f_player = f_player()
            s_player = s_player()

            ball = ball()

            Settings.started = False

            while game_loop:

                clock.tick(Settings.game_tick)

                LoadingImages.GAME_SCREEN.blit(background, (0, 0))
                LoadingImages.GAME_SCREEN.blit(table, (600, 300))

                LoopFunctions.start_countdown(f_player, s_player, ball)

                f_player.render_position(LoadingImages.GAME_SCREEN)
                s_player.render_position(LoadingImages.GAME_SCREEN)

                ball.render_position(LoadingImages.GAME_SCREEN)

                DrawUI.game_show_fps(clock)
                f_player.xy_position()
                s_player.xy_position()

                f_player.score()
                s_player.score()

                LoopFunctions.start_game()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                KeyBinds.f_player_key_binds(f_player, match_restart)
                KeyBinds.s_player_key_binds(s_player, match_restart)

                #f_player.max_pos()
                #s_player.max_pos()

                Collisions.f_player_vs_ball(ball, f_player.get_rect(), ball.get_rect())
                Collisions.s_player_vs_ball(ball, s_player.get_rect(), ball.get_rect())

            pygame.display.update()
