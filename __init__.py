###
# by SpiderDave
###

"""
Who knows?
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = "%%VERSION%%"

__author__ = 'SpiderDave'

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

from . import config
from . import plugin
from imp import reload
reload(config) # In case we're being reloaded.
reload(plugin)
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    from . import test

Class = plugin.Class
Uno = config.Uno


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
