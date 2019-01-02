from bearlibterminal import terminal
def handle_keys(action):
    # Movement keys
    if action == terminal.TK_UP:
        return {'move': (0, -1)}
    elif action == terminal.TK_DOWN:
        return {'move': (0, 1)}
    elif action == terminal.TK_LEFT:
        return {'move': (-1, 0)}
    elif action == terminal.TK_RIGHT:
        return {'move': (1, 0)}


    # No key was pressed
    return {}
