"""
Fileflood plugin used to ignore files that match a pattern.
"""


class Ignore:
    def __init__(self, *paths):
        self.paths = paths

    def __call__(self, app):

        for i in app.find(*self.paths):
            app.files.remove(i)
