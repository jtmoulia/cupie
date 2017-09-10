import wiringpi
import curses


PWM_MIN_HZ = 50
PWM_MAX_HZ = 250


wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)


def set_angle(angle):
    hz = ((PWM_MAX_HZ - PWM_MIN_HZ) / 180.0) * angle + PWM_MIN_HZ
    wiringpi.pwmWrite(18, int(hz))


def draw_scr(scr, angle):
    scr.erase()
    scr.box()
    scr.addstr(1, 2, 'Angle: {}'.format(angle))
    scr.refresh()


def rotate(angle, delta):
    new_angle = angle + delta
    if new_angle > 180:
        return 180
    elif new_angle < 0:
        return 0
    else:
        return new_angle


if __name__ == '__main__':
    scr = curses.initscr()
    scr.keypad(1)
    curses.noecho()
    curses.cbreak()

    angle = 90
    while(True):
        set_angle(angle)
        draw_scr(scr, angle)
        char = scr.getch()
        if char == curses.KEY_RIGHT:
            angle = rotate(angle, 1)
        elif char == curses.KEY_LEFT:
            angle = rotate(angle, -1)
        else:
            break

    scr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
