import sys
import time
import pygame
import cv2
from pygame.locals import QUIT


def main(input_file, x_lines, y_chars, scroll_speed, record_duration):
    pygame.init()
    
    # Screen dimensions
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Text Animation')
    clock = pygame.time.Clock()

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Font
    font_size = 24
    font = pygame.font.Font(None, font_size)

    # Read the input file
    with open(input_file, 'r') as f:
        text = f.read().splitlines()

    # Initialize recording
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter('output.mp4', fourcc, 30.0, (width, height))

    start_time = time.time()
    scroll_offset = 0

    while time.time() - start_time < record_duration:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)

        # Draw the text
        for i in range(x_lines):
            line_idx = i + scroll_offset
            if line_idx < len(text):
                line = text[line_idx][:y_chars]
                text_surface = font.render(line, True, white)
                screen.blit(text_surface, (10, i * font_size))

        # Scroll the text
        scroll_offset += scroll_speed
        if scroll_offset > len(text) - x_lines:
            scroll_offset = 0

        # Record the frame
        frame = pygame.surfarray.array3d(pygame.display.get_surface())
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        video_writer.write(frame)

        pygame.display.update()
        clock.tick(30)

    video_writer.release()
    pygame.quit()


if __name__ == '__main__':
    if len(sys.argv) < 6:
        print('Usage: python script.py <input_file> <x_lines> <y_chars> <scroll_speed> <record_duration>')
    else:
        input_file = sys.argv[1]
        x_lines = int(sys.argv[2])
        y_chars = int(sys.argv[3])
        scroll_speed = int(sys.argv[4])
        record_duration = int(sys.argv[5])
        main(input_file, x_lines, y_chars, scroll_speed, record_duration)
