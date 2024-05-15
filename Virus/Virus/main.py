import rotatescreen
import time

screen = rotatescreen.get_primary_display()
for i in range(60):
    time.sleep(0.5)
    screen.rotate_to(i*90%360)