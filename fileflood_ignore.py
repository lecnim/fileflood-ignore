"""
Fileflood plugin used to ignore files that match a pattern.
"""

from fileflood import debug


class Ignore:
    def __init__(self, *paths):
        # TODO: Log here about usage?
        self.paths = paths

    def __call__(self, app):

        for p in self.paths:

            files = [i for i in app.find(p)]
            for i in files:
                debug('ignoring file: ' + i.path)
                app.files.remove(i)
