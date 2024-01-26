import numpy as np
import matplotlib.pyplot as plt

class line_plot:
    """
    line = quicklook.add_line_plot(chart_skeleton,
    x = ,
    y = ,
    yerror = None, #If no values, None
    color = chart_skeleton.color_library.default
    linewidth = 7,
    linestyle = '-', #['-', '--', ':', '-.']
    marker_shape = '.', #['None', 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x']
    opacity = 1,
    label_for_legend = '',
    layer_order = 1)
    """

    def __init__(self, chart_skeleton, x, y, yerror, linewidth, linestyle,
    color, color_brightness, marker_shape, opacity, label_for_legend,
    layer_order):

        if not chart_skeleton.ax:
            raise Exception('The chart skeleton has not been built. \
            You must build a chart skeleton for each new plot that you \
            want to create.')
        # ---- check data types
        if type(x) in [str, int, float, bool]:
            raise TypeError('x is not properly defined. x should be a \
            1 dimensional array of values.')
        if type(y) in [str, int, float, bool]:
            raise TypeError('y is not properly defined. y should be a \
            1 dimensional array of values.')
        if type(yerror) in [str, int, float, bool]:
            raise TypeError('yerror is not properly defined. If you do not need \
            error represented on your line plot, set yerror = None.\n'
            'If you need yerror on your line plot, ensure that it is a \
            1 dimensional array of values.')

        # ---- check data shapes
        if np.shape(np.shape(x))[0] != 1:
            raise ValueError('x is not properly defined.; it is a {} x {} array.\
             x must be 1-dimensional array.'.format(np.shape(x)[0],
                                                    np.shape(x)[1]))
        if np.shape(np.shape(y))[0] != 1:
            raise ValueError('y is not properly defined.; it is a {} x {} array.\
             y must be 1-dimensional array.'.format(np.shape(y)[0],
                                                    np.shape(y)[1]))
        if np.shape(x) != np.shape(y):
            raise ValueError('x and y are not the same shape. x has {} values \
            and y has {} values'.format(np.shape(x)[0], np.shape(y)[0]))

        # ---- define shades of color
        line = color[0]
        fill = color[1]
        edge = color[2]

        # ---- define markersize
        markersize, markeredgewidth = define_markersize(chart_skeleton['size'],
                                                        marker_shape)

        # ---- plot y error as fill between
        if yerror is not None:
            fill = chart_skeleton.ax.fill_between(
                                  x,
                                  y - yerror,
                                  y + yerror,
                                  color = fill,
                                  label = None,
                                  alpha = 0.2,
                                  zorder = layer_order + 2);

        else:
            fill = None
        # ---- plot mean line
        mean = chart_skeleton.ax.plot(
                    x,
                    y,
                    linewidth = linewidth,
                    linestyle = linestyle,
                    color = line,
                    marker = marker_shape,
                    markersize = markersize,
                    markeredgecolor = edge,
                    markeredgewidth = markeredgewidth,
                    alpha = opacity,
                    label = label_for_legend,
                    solid_capstyle='round',
                    zorder = layer_order + 2);

        # ---- outline fill between
        if yerror is not None:
            ub = chart_skeleton.ax.plot(
                        x,
                        y + yerror,
                        linewidth = 0.5,
                        color = edge,
                        label = None,
                        zorder = layer_order + 2);
            lb = chart_skeleton.ax.plot(
                        x,
                        y - yerror,
                        linewidth = 0.5,
                        color = edge,
                        label = None,
                        zorder = layer_order + 2);
        else:
            ub = None
            lb = None

        self.line = mean
        self.yerr_fill = fill
        self.yerr_ub = ub
        self.yerr_lb = lb
