# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import inspect
import warnings
from unittest import TestCase

from ipywidgets import Dropdown


class TestDropdown(TestCase):

    def test_construction(self):
        Dropdown()

    def test_deprecation_warning_mapping_options(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            # Clearing the internal __warningregistry__ seems to be required for
            # Python 2 (but not for Python 3)
            module = inspect.getmodule(Dropdown)
            getattr(module, '__warningregistry__', {}).clear()

            Dropdown(options={'One': 1, 'Two': 2, 'Three': 3})
            assert len(w) > 0
            assert issubclass(w[-1].category, DeprecationWarning)
            assert "Support for mapping types has been deprecated" in str(w[-1].message)
