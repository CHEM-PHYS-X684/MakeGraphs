"""
Unit and regression test for the makegraphs package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import makegraphs


def test_makegraphs_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "makegraphs" in sys.modules
