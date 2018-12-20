import libtcodpy as libtcod

class PromptHelper:
        def __init__(self, con, height, width, pos_x, pos_y, target_con, text = '', border=True):
            self.height = height
            self.width = width
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.dialog_con = libtcod.console_new(self.height, self.width)
            self.target_con = target_con
            self.border = border
            self.text = text

        def update(self):
            libtcod.console_blit(self.dialog_con,0, 0,0,0, self.target_con,self.pos_x, self.pos_y )

        def set_text(self,text, update=False):
            self.text = text
            libtcod.console_print_ex(self.dialog_con, 1, 1, libtcod.BKGND_NONE, libtcod.LEFT, self.text )
            if self.border:
                self.add_border()
            if update:
                self.update
        def append_text(self,text, update=False):
            self.text += text
            if update:
                self.update()

        def add_border(self):
            libtcod.console_hline(self.dialog_con,0,0,self.width)
            libtcod.console_vline(self.dialog_con,0,0,self.height)
            libtcod.console_hline(self.dialog_con,0,self.height,self.width)
            libtcod.console_vline(self.dialog_con,self.width-1,0,self.height)

        def clear(self):
            libtcod.console_clear(self.dialog_con)
