import textwrap


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

    def log_message(self, message, fg = None, bg = None):
        if fg is None:
            fg = self.default_fg
        if bg is None:
            bg = self.default_bg
        self.log.append(Message(message, fg, bg))
        self.append_scroll_back(Message(message, fg, bg))

    def append_scroll_back(self, message):
        new_msg_lines = textwrap.wrap(message.message, self.scroll_width)

        for line in new_msg_lines:
            # If the buffer is full, remove the first line to make room for the new one
            if len(self.scrollback) == self.scroll_height - 1:
                del self.scrollback[0]

            self.scrollback.append(line)

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
    def __init__(self, message, fg, bg):
        self.message = message
        self.fg = fg
        self.bg = bg
