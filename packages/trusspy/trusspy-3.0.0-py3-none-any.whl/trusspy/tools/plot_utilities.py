# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import os
import shutil

import matplotlib.pyplot as plt
import numpy as np

from .helper_functions2 import plot_elems, plot_force, plot_hist, plot_nodes, plot_pth
from .movie_generator import png_to_gif


def p_nodes(self):
    plot_nodes(self.Nodes.coords + self.Results.U, color="C1")


def p_elements(self):
    plot_elems(self.Elements.conns, self.Nodes.coords + self.Results.U, color="C0")


def p_extforces(self, step=1):
    plot_force(
        self.ExtForces.forces[:, 3 * (step - 1) : 3 * step],
        self.Nodes.coords + self.Results.U,
    )


def p_model(
    self,
    view="xz",
    contour=None,
    lim_scale=1.0,
    force_scale=1.0,
    nodesize=10,
    cbar_limits="auto",
    inc=-1,
    step=1,
):
    con = None
    plt.figure()
    fig, ax = None, None

    if inc < 0:
        inc = len(self.Results.R) + inc

    if inc == 0:
        lpf = 1.0
        force_label = r"$[F_0]$"
        contour = None
        title = "UNDEFORMED"
    else:
        lpf = self.Results.R[inc].lpf
        force_label = r"$\lambda \cdot [F_0]$"
        title = f"INCREMENT: {inc}"

    if contour == "stretch":
        if cbar_limits == "auto":
            contour_lim = [
                1 - max(abs(self.Results.R[inc].stretch[:, 0] - 1)),
                1 + max(abs(self.Results.R[inc].stretch[:, 0] - 1)),
            ]
        else:
            contour_lim = cbar_limits
        con = contour, self.Results.R[inc].stretch[:, 0], contour_lim
    if contour == "force":
        if cbar_limits == "auto":
            contour_lim = [
                -max(abs(self.Results.R[inc].element_force[:, 0])),
                max(abs(self.Results.R[inc].element_force[:, 0])),
            ]
        else:
            contour_lim = cbar_limits
        con = contour, self.Results.R[inc].element_force[:, 0], contour_lim
    if contour == "stress":
        if cbar_limits == "auto":
            contour_lim = [
                -max(abs(self.Results.R[inc].element_stress[:, 0])),
                max(abs(self.Results.R[inc].element_stress[:, 0])),
            ]
        else:
            contour_lim = cbar_limits
        con = contour, self.Results.R[inc].element_stress[:, 0], contour_lim
    if type(contour) == tuple:
        if contour[0] == "stretch":
            con_data = self.Results.R[inc].stretch[:, 0]
        elif contour[0] == "force":
            con_data = self.Results.R[inc].element_force[:, 0]
        elif contour[0] == "stress":
            con_data = self.Results.R[inc].element_stress[:, 0]
        con = contour[0], con_data, contour[1]

    textstr = (
        r"$\mathbf{Plot}$ $\mathbf{Scale}$ "
        + force_label
        + " ="
        + "{:2.1g} ".format(force_scale)
        + r"$\cdot [L]$"
    )
    f0_const = self.Results.R[inc].ExtForces.forces_const
    step = self.Results.R[inc].step
    fig, ax = plot_force(
        f0_const + lpf * self.ExtForces.forces[:, 3 * (step - 1) : 3 * step],
        self.Nodes.coords + self.Results.R[inc].U,
        fig,
        ax,
        view=view,
        scale=force_scale,
    )

    fig, ax = plot_nodes(
        self.Nodes.coords + self.Results.R[inc].U,
        fig,
        ax,
        color="k",
        view=view,
        size=nodesize,
    )
    fig, ax = plot_elems(
        self.Elements.conns,
        self.Nodes.coords + self.Results.R[inc].U,
        fig,
        ax,
        color="C7",
        view=view,
        contour=con,
        lim_scale=lim_scale,
    )

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle="round", facecolor="C2", alpha=0.25)
    if view == "3d":
        ax.text2D(
            0.5,
            0.95,
            textstr,
            transform=ax.transAxes,
            fontsize=11,
            verticalalignment="top",
            horizontalalignment="center",
            bbox=props,
        )
    else:
        ax.text(
            0.5,
            0.95,
            textstr,
            transform=ax.transAxes,
            fontsize=11,
            verticalalignment="top",
            horizontalalignment="center",
            bbox=props,
        )

    if len(plt.gca().yaxis.get_label().get_text()) == 0:
        str_ins = ""
    else:
        str_ins = ", "
    if view == "3d":
        ax.set_title(title + str_ins + plt.gca().yaxis.get_label().get_text())
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
    else:
        plt.title(title + str_ins + plt.gca().yaxis.get_label().get_text())
        plt.xlabel(view[0])
        plt.ylabel(view[1])

    return fig, ax


def p_movie(
    self,
    view="xz",
    contour=None,
    lim_scale=1.5,
    force_scale=0.5,
    nodesize=10,
    cbar_limits="auto",
    incs="all",
    **kwargs,
):
    if incs == "all":
        incs = range(1, len(self.Results.R))

    if os.path.isdir("figures/"):
        shutil.rmtree("figures/")
    os.mkdir("figures/")
    os.mkdir("figures/png/")

    for i in incs:
        self.plot_model(view, contour, lim_scale, force_scale, nodesize, cbar_limits, i)
        plt.savefig("figures/png/fig_{:03d}.png".format(i), dpi=200)
        plt.close("all")

    png_to_gif(**kwargs)


def p_path(self, nodepath, increment=-1, Y="Displacement X", fig=None, ax=None):
    # loop over increments
    xx = []
    yy = []
    dir_dict = {"X": 0, "Y": 1, "Z": 2}

    x, y = np.nan, np.nan

    R = self.Results.R[increment]

    for node in nodepath:
        if "Displacement" in Y:
            y = R.U[np.where(self.Nodes.labels == node)][0][dir_dict[Y[-1]]]
        elif "LPF" in Y:
            y = R.lpf
        elif "Force" in Y:
            y = R.r[np.where(self.Nodes.labels == node)][0][dir_dict[Y[-1]]]
        elif "State Variable" in Y:
            stv_index = int(Y[-1]) - 1
            y = R.state_v[np.where(self.Nodes.labels == node)][0][stv_index]
        xx.append(x)
        yy.append(y)

    if fig is None:
        fig, ax = plt.subplots()
    fig, ax = plot_pth(nodepath, yy, increment, Y, fig, ax)

    return fig, ax


def p_history(self, nodes=[1, 1], X="Displacement X", Y="LPF", fig=None, ax=None):
    # loop over increments
    xx = [0]
    yy = [0]
    dir_dict = {"X": 0, "Y": 1, "Z": 2}

    x, y = np.nan, np.nan
    for R in self.Results.R:
        if "Displacement" in X:
            x = R.U[np.where(self.Nodes.labels == nodes[0])][0][dir_dict[X[-1]]]
        elif "LPF" in X:
            x = R.lpf
        elif "Force" in X:
            x = R.r[np.where(self.Nodes.labels == nodes[0])][0][dir_dict[X[-1]]]
        elif "State Variable" in X:
            stv_index = int(X[-1]) - 1
            x = R.state_v[np.where(self.Nodes.labels == nodes[0])][0][stv_index]

        if "Displacement" in Y:
            y = R.U[np.where(self.Nodes.labels == nodes[1])][0][dir_dict[Y[-1]]]
        elif "LPF" in Y:
            y = R.lpf
        elif "Force" in Y:
            y = R.r[np.where(self.Nodes.labels == nodes[1])][0][dir_dict[Y[-1]]]
        elif "State Variable" in Y:
            stv_index = int(Y[-1]) - 1
            y = R.state_v[np.where(self.Nodes.labels == nodes[1])][0][stv_index]
        xx.append(x)
        yy.append(y)

    if "Increments" in X:
        xx = np.arange(1 + len(self.Results.R), dtype=int)
    if "Increments" in Y:
        yy = np.arange(1 + len(self.Results.R))

    if fig is None:
        fig, ax = plt.subplots()
    fig, ax = plot_hist(xx, yy, nodes[0], X, Y, fig, ax)

    return fig, ax


def p_show(self):
    plt.show()
