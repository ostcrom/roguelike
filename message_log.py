import textwrap
from utils import *

class MessageLog:
    def __init__(self, scroll_width = 10, scroll_height = 10, default_fg = 0, default_bg=1, ascending = True):
        self.log = []
        self.default_fg = default_fg
        self.default_bg = default_bg
        self.scroll_height = scroll_height
        self.scroll_width = scroll_width
        self.ascending = ascending
        self.wrapper = textwrap.TextWrapper(width=self.scroll_width)
        self.scrollback = []

    def log_message(self, message, color='white'):
        m = Message(message, color)
        self.log.append(m)
        self.append_scroll_back(m)

    def append_scroll_back(self, message):
        new_msg_lines = textwrap.wrap(message.message, self.scroll_width)

        for line in new_msg_lines:
            # If the buffer is full, remove the first line to make room for the new one
            if len(self.scrollback) == self.scroll_height - 1:
                del self.scrollback[0]

            self.scrollback.append(color_tag_string(message.color) + line)

        if len(self.scrollback) == self.scroll_height - 1:
            del self.scrollback[0]
        if self.scrollback[0] == "":
            del self.scrollback[0]


        self.scrollback.append("")

    def get_scroll_back(self):
        scrollback_text = ''
        for line in self.scrollback:
            scrollback_text += "\r\n" + line
        return scrollback_text
class Message:
    def __init__(self, message, color='white'):
        self.message = message
        self.color = color
