"""
flask_flatpages_knitr
~~~~~~~~~~~~~~~~~~~~~~

Flask-FlatPages-Knitr preprocesses a Flask FlatPage such that code chunks
are evaluated before the next step in the rendering process occurs.

:copyright: (c) 2014 Fabian Hirschmann <fabian@hirschm.net>
:license: MIT, see LICENSE.txt for more details.

"""
from __future__ import print_function
import pkg_resources
from os import makedirs, path
from inspect import getargspec


from rpy2.robjects import r
r.library("knitr")

try:
    __version__ = pkg_resources.require("Flask-FlatPages-Knitr")[0]
except pkg_resources.DistributionNotFound:
    __version__ = "0.0-dev"


class FlatPagesKnitr(object):
    """
    Class that, when applied to a :class:`flask.Flask` instance,
    will evaluate code chunks using knitr.
    """
    def __init__(self, app=None, renderer=None):
        """
        Initializes Flask-FlatPages-Knitr

        :param app: your application. Can be omitted if you call
                    :meth:`init_app` later.
        :type app: :class:`flask.Flask`
        :param renderer: function that continues rendering the page; if
                         omitted, `FLATPAGES_HTML_RENDERER` will be used.
        :param renderer: function
        """
        self.postrenderer = renderer

        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        Used to initialize an application. This is useful when passing
        an app later.

        :param app: your application
        :type app: :class:`flask.Flask`
        """
        self.app = app

        if not self.postrenderer:
            self.postrenderer = self.app.config["FLATPAGES_HTML_RENDERER"]

        # The following lambda expression works around Flask-FlatPage's
        # reflection magic.
        self.app.config["FLATPAGES_HTML_RENDERER"] = lambda t, p, m: self.renderer(t, p, m)

    def renderer(self, text, flatpages, page):
        """
        Renders a flat page to HTML.

        :param text: the text of the flat page
        :type text: string
        :param flatpages: a list of flatpages
        :type flatpages: sequence
        :param page: a page instance
        :type page: :class:`flask_flatpages.Page`
        """
        figure_path = path.join(self.app.static_folder, "knitr", page.path)
        figure_url = "/".join([self.app.static_url_path, "knitr", page.path])

        if not path.exists(figure_path):
            makedirs(figure_path)

        r("opts_knit$set(base.dir='{0}')".format(figure_path))
        r("opts_knit$set(base.url='{0}/')".format(figure_url))

        out = r.knit(text=text)

        # This is pretty ugly, but we want to support all types of rendering
        # functions and Flask-FlatPages does this in a similar fashion.
        n_args = len([a for a in getargspec(self.postrenderer).args if a is not "self"])

        return self.postrenderer(*[out[0], flatpages, page][:n_args])
