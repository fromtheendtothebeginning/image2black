from level import *
from win import *

if __name__ == '__main__':
    win = Win(WIN_NAME, SIZE)
    level = Level(win.win)
    level.win_item()
    
    win.win.mainloop()
    