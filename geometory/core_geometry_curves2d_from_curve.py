#!/usr/bin/env python

##Copyright 2009-2014 Jelle Feringa (jelleferinga@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from OCCT.gp import gp_OX2d
from OCCT.GCE2d import GCE2d_MakeEllipse
from OCCT.Geom2d import Geom2d_TrimmedCurve
from OCCT.Geom2dConvert import geom2dconvert_CurveToBSplineCurve
from OCCT.Convert import Convert_TgtThetaOver2

from OCCT.Visualization import BasicViewer
display, start_display, add_menu, add_function_to_menu = init_display()


def curves2d_from_curves():
    major, minor = 12, 4
    axis = gp_OX2d()
    ellipse = GCE2d_MakeEllipse(axis, major, minor).Value()
    trimmed_curve = Geom2d_TrimmedCurve(ellipse, -1, 2, True)
    bspline = geom2dconvert_CurveToBSplineCurve(trimmed_curve,
                                                Convert_TgtThetaOver2)
    display.DisplayShape(bspline, update=True)


if __name__ == '__main__':
    curves2d_from_curves()
    start_display()
