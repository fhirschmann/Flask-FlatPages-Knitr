import unittest
import os
from shutil import rmtree
from tempfile import mkdtemp


from flask import Flask
from flask_flatpages import FlatPages
from flask_flatpages_knitr import FlatPagesKnitr


class TestFlatPagesKnitr(unittest.TestCase):
    def setUp(self):
        self.tmp = mkdtemp()
        self.content = os.path.join(self.tmp, "content")
        os.makedirs(self.content)

        self.app = Flask(__name__, static_folder=os.path.join(self.tmp, "static"))
        self.app.config.update(
            FLATPAGES_ROOT=self.content,
            FLATPAGES_AUTO_RELOAD=True,
            FLATPAGES_MARKDOWN_EXTENSIONS=["fenced_code"],
        )
        self.pages = FlatPages(self.app)
        FlatPagesKnitr(self.app)

    def tearDown(self):
        rmtree(self.tmp)

    def get(self, body, ext=".Rmd"):
        self.app.config.update(FLATPAGES_EXTENSION=ext)
        with open(os.path.join(self.content, "test" + ext), "w") as f:
            f.write("title:test\n\n" + body)
        return self.pages.get("test").html

    def test_rmd(self):
        self.assertEqual(self.get("#test"), "<h1>test</h1>")

    def test_r(self):
        self.assertTrue("3.14" in self.get("```{r}\npi\n```"))

    def test_plot(self):
        self.get("```{r test}\nplot(1:4, 1:4)\n```")
        self.assertTrue(os.path.exists(os.path.join(
            self.tmp, "static", "knitr", "test", "figure", "test.png")))
