# -*- coding: utf-8 -*-
import unittest
import os
from shutil import rmtree
from tempfile import mkdtemp
from codecs import open

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
            FLATPAGES_ENCODING="utf-8",
            FLATPAGES_MARKDOWN_EXTENSIONS=["fenced_code"],
        )
        self.pages = FlatPages(self.app)
        FlatPagesKnitr(self.app)

    def tearDown(self):
        rmtree(self.tmp)

    def get(self, body, ext=".Rmd", enc="utf-8"):
        self.app.config.update(FLATPAGES_EXTENSION=ext)
        with open(os.path.join(self.content, "test" + ext), "w", enc) as f:
            f.write("title:test\n\n" + body)
        return self.pages.get("test").html

    def test_rmd(self):
        self.assertEqual(self.get("#test"), "<h1>test</h1>")

    def test_r(self):
        self.assertTrue("3.14" in self.get("```{r}\npi\n```"))

    def test_plot(self):
        self.get("```{r, test}\nplot(1:4, 1:4)\n```")
        self.assertTrue(os.path.exists(os.path.join(
            self.tmp, "static", "knitr", "test", "figure", "test-1.png")))

    def test_unicode(self):
        self.assertTrue(u"萬大事都有得解決" in self.get(u"```{r}\npaste('萬大事都有得解決')\n```"))

    def test_unicode2(self):
        self.app.config.update(FLATPAGES_ENCODING="iso-8859-15")
        self.assertEqual(self.get(u"äöü", enc="iso-8859-15"), u"<p>äöü</p>")
