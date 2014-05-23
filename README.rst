Flask-FlatPages-Knitr
---------------------

Flask-FlatPages-Knitr preprocesses a `Flask <http://flask.pocoo.org/>`_
`FlatPage <http://pythonhosted.org/Flask-FlatPages/>`_
using `knitr <http://yihui.name/knitr/>`_ such that
code chunks are evaluated before the next step in the rendering
process occurs.

Quickstart
``````````

First, install the `knitr <http://yihui.name/knitr>`_ R package:

.. code:: bash

    Rscript -e "install.packages('knitr')"

Right now, Flask-FlatPages-Knitr requires at least version 0.6 of Flat-FlatPages,
which has not been released yet. Hence, you'll have to install it from Github:

.. code:: bash

    pip install git+git://github.com/SimonSapin/Flask-FlatPages/

Second, install Flask-FlatPages-Knitr from the Python Package Index:

.. code:: bash

    pip install Flask-FlatPages-Knitr

Finally, you can simply add Flask-FlatPages-Knitr to your app:

.. code:: python

    from flask import Flask
    from flask_flatpages import FlatPages
    from flask_flatpages_knitr import FlatPagesKnitr

    app = Flask(__name__)
    app.config.from_object(__name__)

    pages = FlatPages(app)
    FlatPagesKnitr(app)

By default, ``FLATPAGES_HTML_RENDERER`` will be reused, which defaults
to a Markdown implementation for Python. For more advanced Markdown
rendering, `Flask-FlatPages-Pandoc <http://github.com/fhirschmann/Flask-FlatPages-Pandoc>`_
is recommended:

.. code:: python

    from flask_flatpages_pandoc import FlatPagesPandoc

    FLATPAGES_EXTENSION = ".Rmd"

    pages = FlatPages(app)
    FlatPagesPandoc("markdown", "app", ["--mathjax"], pre_render=True)
    FlatPagesKnitr(app)


Links
`````

* `Demo Page <http://0x0b.de/sandbox/knitr/>`_
* `GitHub Page <http://github.com/fhirschmann/Flask-FlatPages-Knitr>`_
* `PyPI <http://pypi.python.org/pypi/Flask-FlatPages-Knitr>`_
