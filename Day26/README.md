# Project 26: Music player

### Create a Music Player

Today, we're going to build a basic music player that resembles an iPod interface. You'll allow the user to select a song and play it, using `pygame` to handle the audio. The player will have options to **play**, **pause**, and **exit** the program.

### Steps:

1. **Pygame Setup:**
   - Import `pygame`, initialize it, and load the audio file using `pygame.mixer`.

   ```python
   import pygame

   pygame.init()
   pygame.mixer.init()
   sound = pygame.mixer.Sound('audio.wav')
    sound.play()

    def pause():
    pygame.mixer.pause()

    pause()
    def play():
    # Play the sound
    pygame.mixer.unpause()
    while True:
        # Start taking user input and doing something with it
        input()

    while True:
    # clear the screen

    # Show the menu

    # take user's input

    # check whether you should call the play() subroutine depending on user's input
    if True:
        play()
