import curses
import curses.textpad

def key_map(ch,window):
    cursor = window.getyx()
    x=cursor[1]
    y=cursor[0]

    def moveleft():
        if x>0 and window.getch(y,x-1)>=0:
            window.move(y,x-1)

    def moveup():
        if y>0 and window.getch(y-1,x)>=0:
            window.move(y-1,x)

    def moveright():
        if x<window.getmaxyx()[1] and window.getch(y,x+1)>=0:
            window.move(y,x+1)

    def movedown():
        if y<window.getmaxyx()[0]:
            #window.move(y+1,x)
            window.addstr(30,30,str(window.inch(y+1,x)))

    def backspace():
        moveleft()
        window.delch()

    mapping = {
        curses.KEY_DOWN: movedown,
        curses.KEY_LEFT: moveleft,
        curses.KEY_UP: moveup,
        curses.KEY_RIGHT: moveright,
        curses.KEY_DC: lambda: window.delch(),
        curses.KEY_BACKSPACE: backspace
    }
    func = mapping.get(ch,lambda: window.addch(ch))
    return func()

def main(window):
    window.clear()
    box = curses.textpad.Textbox(window, insert_mode=False)
    box.stripspaces = 1
    curses.nl()
    box.edit()
    print(box.gather())


curses.wrapper(main)


