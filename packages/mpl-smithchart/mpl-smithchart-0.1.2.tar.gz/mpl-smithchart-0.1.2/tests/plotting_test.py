from itertools import product

import numpy as np
import pytest
from matplotlib import pyplot as pp

from mpl_smithchart import SmithAxes


@pytest.fixture
def mpl_figure(tmpdir):
    pp.figure(figsize=(6, 6))
    pp.subplot(1, 1, 1, projection='smith')
    yield
    pp.savefig(tmpdir/'out.png', format='png')


def s11_of_cap(freq):
    # port1 to cap to ground
    return (1-1j*freq*1e-9)/(1+1j*freq*1e-9)


def s11_of_parallel_cap_res(freq, z0=50):
    # port1 to cap||res to ground (res=50ohm) (c=1nF)
    s = 2j*np.pi*freq
    return (50 - z0*(1+s*1e-9*50))/(50 + z0*(1+s*1e-9*50))


@pytest.mark.parametrize(
    "point",
    (
        200+100j,
        50.0,
        50-10j,
    ),
)
def test_plot_point(mpl_figure, point):
    pp.plot(point, datatype=SmithAxes.Z_PARAMETER)


def test_plot_s_param(mpl_figure):
    freqs = np.logspace(0, 9, 200)
    s11 = s11_of_cap(freqs)
    pp.plot(s11, markevery=1, datatype=SmithAxes.S_PARAMETER)


def test_plot_labels(mpl_figure):
    freqs = np.logspace(0, 9, 200)
    s11 = s11_of_cap(freqs)
    pp.plot(s11, markevery=1, datatype=SmithAxes.S_PARAMETER, label='s11')
    pp.legend()


def test_plot_normalized_axes(tmpdir):
    freqs = np.logspace(0, 9, 200)
    pp.figure(figsize=(18, 12)).set_layout_engine("tight")

    for i, (do_normalize_axes, impedance) in enumerate(product([True, False], [10, 50, 200])):
        s11 = s11_of_parallel_cap_res(freqs, z0=impedance)
        pp.subplot(
            2, 3, i+1,
            projection='smith',
            axes_impedance=impedance,
            axes_normalize=do_normalize_axes,
        )
        pp.plot(s11)
        pp.title(f"Impedance: {impedance}$\\Omega$ -- Normalized Axes: {do_normalize_axes}")
    pp.savefig(tmpdir/'out.png', format='png')


def test_plot_grid_styles(tmpdir):
    freqs = np.logspace(0, 9, 200)
    s11 = s11_of_parallel_cap_res(freqs)
    pp.figure(figsize=(18, 12)).set_layout_engine("tight")

    offset = 0
    for i, (major_fancy, minor_enable, minor_fancy) in enumerate(
        product(
            [True, False],
            [True, False],
            [True, False],
        ),
    ):
        if not minor_enable and minor_fancy:
            offset = offset + 1
            continue
        pp.subplot(
            2, 3, i + 1 - offset,
            projection='smith',
            grid_major_fancy=major_fancy,
            grid_minor_enable=minor_enable,
            grid_minor_fancy=minor_fancy,
        )
        major_str = "fancy" if major_fancy else "standard"
        minor_str = "off" if not minor_enable else ("fancy" if minor_fancy else "standard")

        pp.plot(s11)
        print(f"Major: {major_str} -- Minor: {minor_str}")
    pp.savefig(tmpdir/'out.png', format='png')
