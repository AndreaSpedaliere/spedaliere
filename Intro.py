import pgzrun

alien = Actor('alien')
alien.pos = 100,56
alien.topright = 0,10
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
        set_alien_hurt()

    else:
        print("You missed me!")
        alien.image = 'alien'

def set_alien_hurt():
        sounds.punch.play()
        alien.image = 'alien_hurt'
        clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
        alien.image = 'alien'        
        
WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

pgzrun.go()