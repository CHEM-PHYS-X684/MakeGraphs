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


def test_1():
    G = makegraphs.build_graph1(verbose=1)

def test_2():
    G = makegraphs.build_graph2(verbose=1)

if __name__== "__main__":
    test_makegraphs_imported()
    test_1()
    test_2()
