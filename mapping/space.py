from mapping.transport import Transport

class Space:
    """
    A space on the map. May or may not be blocked/block sightself.
    """

    def __init__(self, is_blocked , block_sight=None, transport=None) :
        """
        is_blocked and block_sight are bool
        transport expoects a tba list
        ## TODO: define and implement transport space, should load to a coord-
                nate on a specified mapself.
        """
        self.blocked = is_blocked

        if block_sight is None:
            block_sight = is_blocked
        self.block_sight = block_sight

        self.discovered = False
        if not transport is None:
            self.transport = transport
        else:
            self.transport = None
