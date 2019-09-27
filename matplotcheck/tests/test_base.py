"""Tests for the base module"""
import pytest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotcheck.base import PlotTester

import pdb


def test_line_plot(pt_line_plt):
    """Test that the line plot returns true for line but false for bar or
    scatter."""
    pt_line_plt.assert_plot_type("line")

    with pytest.raises(AssertionError):
        pt_line_plt.assert_plot_type("bar")
    with pytest.raises(AssertionError):
        pt_line_plt.assert_plot_type("scatter")
    plt.close()


def test_scatter_plot(pt_scatter_plt):
    """Test that the scatter plot returns true for line but false for bar or
    line."""
    pt_scatter_plt.assert_plot_type("scatter")

    with pytest.raises(AssertionError):
        pt_scatter_plt.assert_plot_type("bar")
    with pytest.raises(AssertionError):
        pt_scatter_plt.assert_plot_type("line")
    plt.close()


def test_bar_plot(pt_bar_plt):
    """Test that the scatter plot returns true for line but false for bar or
    line."""
    pt_bar_plt.assert_plot_type("bar")

    with pytest.raises(AssertionError):
        pt_bar_plt.assert_plot_type("scatter")
    with pytest.raises(AssertionError):
        pt_bar_plt.assert_plot_type("line")
    plt.close()


def test_options(pt_line_plt):
    """Test that a ValueError is raised if an incorrect plot type is provided.
    Should this test be unique of within a suite of tests?"""

    with pytest.raises(
        ValueError,
        match="Plot_type to test must be either: scatter, bar or line",
    ):
        pt_line_plt.assert_plot_type("foo")
    plt.close()


"""
Test fo geopandas. Commenting out until later.
def test_assert_xydata_geo(pd_gdf, pt_geo_plot):
    pt_geo_plot.assert_xydata(pd_gdf)
    plt.close()
"""


def test_assert_line():
    pd_df = pd.DataFrame({"A": np.arange(100), "B": np.arange(100, 200)})
    fig, ax = plt.subplots()

    x = np.linspace(-10, 10, 1000)
    ax.plot(x, x * 2 + 1)

    # pt_plt = pd_df.plot("A", "B", ax=ax, kind="scatter")

    axis = plt.gca()

    plot_tester = PlotTester(axis)

    plot_tester.assert_line(1, 99)

    plt.close()


def test_assert_num_bins(pd_df):
    bins = 7

    fig, ax = plt.subplots()
    # pd_df['B'].plot.hist(bins=7, ax=ax)
    pd_df.plot.hist(bins=17, ax=ax, histtype="step")
    axis = plt.gca()
    t = PlotTester(axis)
    pdb.set_trace()
    a = 1
