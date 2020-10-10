## Add a line to your chart
To add a line to your chart, we will use the function:
```python
quicklook.add_line_to_chart
```

**Always copy and paste!** quicklook is designed as a copy-and-paste package. You should always copy the default code into your notebook from the documentation.
For tips on how to easily copy-and-paste quicklook code into your notebook, [click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/copy_and_paste_quicklook_code.md). 

## Basic Example:
1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data and save it as `x_values` and `y_values`.
3. Create your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
4. Add your line using `quicklook.add_line_to_chart`

```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create arbtrary data
x_values = np.linspace(-1,1,20)
y_values = [1/(1+np.exp(-5*i)) for i in x_values]

# ---- create the chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Making a Line Plot',
xlabel = 'X Values',
ylabel = 'Y\nValues',
x_min_max = (-1,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add line
quicklook.add_line_to_chart(chart_skeleton,
x = x_values,
y = y_values,
color_name = 'blue',
color_brightness = 'default',
linewidth = 7,
linestyle = '-',
marker_shape = '.',
opacity = 1,
label_for_legend = '',
layer_order = 1)
```
![basic_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/line/basic_example.png)
## Style options
- `color_name` can be 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'orange'
- `color_brightness` can be 'default', 'light', or 'dark'
- `linewidth` can be any number
- `linestyle` can be '-', '--', ':', '-.' ([click here](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html) to see an example of each line style)
- `marker_shape` can be 'o', '.', 'v', '^', 's', 'd', 'D', 'X', 'x' ([click here](https://matplotlib.org/api/markers_api.html) to see an example of each marker shape)
  - If you set marker_shape to '', there will not be any markers, just the line.
- `opacity` can be any number between 0 and 1
- `label_for_legend` is the name of the line; this will show up in the legend when you add one.
- `layer_order` can be any number. Layers are drawn from low to high numbers; this means that a line with `layer_order = 2` will be drawn on top of `layer_order = 1`. If you leave `layer_order = 1` for all lines, the lines will be drawn in the order that they show up in your code.

## Complete Example:
1. Make sure that quicklook is imported into your notebook.
2. Get your data! Here, I'll create some arbitrary data and save it as `x_values` and `y_values`.
3. Create your chart skeleton. [Click here](https://github.com/alexdsbreslav/quicklook/blob/master/how_to_use_quicklook/build_chart_skeleton.md) for more details on how to build a chart skeleton
4. Add multiple lines using `quicklook.add_line_to_chart` and adjust the style options.
5. Add a legend.
6. Save the chart to a folder on my computer.

```python
import pandas as pd
import numpy as np
import os
import quicklook
```
```python
# ---- create arbtrary x values
x_values = np.linspace(-1,1,20)

# ---- create y values for gray line
y_values = [1/(1+np.exp(-5*i)) for i in x_values]

# ---- create slightly different y values for blue line
blue_y_values = [0.75/(1+np.exp(-5*i))+0.25 for i in x_values]

# ---- create slightly different y values for purple line
purple_y_values = [0.75/(1+np.exp(-5*i)) for i in x_values]

# ---- create the chart skeleton
chart_skeleton = quicklook.build_chart_skeleton(size = 'default',
title = 'Making a Line Plot',
xlabel = 'X Values',
ylabel = 'Y\nValues',
x_min_max = (-1,1), y_min_max = (0,1),
xtick_interval = 0.25, ytick_interval = 0.25,
horizontal_gridlines_on = False,
vertical_gridlines_on = False);

# ---- add thin dark gray dotted line without markers
# ---- don't add label so it doesn't show up in legend
quicklook.add_line_to_chart(chart_skeleton,
x = x_values,
y = y_values,
color_name = 'gray',
color_brightness = 'dark',
linewidth = 3,
linestyle = ':',
marker_shape = '',
opacity = 1,
label_for_legend = '',
layer_order = 1)

# ---- add thick blue line with dot markers
# ---- make slightly transparent so grey line shows through
quicklook.add_line_to_chart(chart_skeleton,
x = x_values,
y = blue_y_values,
color_name = 'blue',
color_brightness = 'default',
linewidth = 7,
linestyle = '-',
marker_shape = '.',
opacity = 0.5,
label_for_legend = 'Blue Line',
layer_order = 2)

# ---- add medium grape line with hexagon markers
# ---- make slightly transparent so grey line shows through
quicklook.add_line_to_chart(chart_skeleton,
x = x_values,
y = purple_y_values,
color_name = 'grape',
color_brightness = 'default',
linewidth = 5,
linestyle = '-',
marker_shape = 'h',
opacity = 0.5,
label_for_legend = 'Purple Line',
layer_order = 2)

# ---- add legend
quicklook.add_legend(chart_skeleton,
legend_location = 'best', frame_around_legend=True);

# ---- save plot
quicklook.save_chart(chart_name = 'complete_example', 
                     path_to_folder_to_save_chart_in = fp.join(fp.abspath('images'), 'plots', 'line'),
                     print_confirmation=False);
```
![complete_example](https://github.com/alexdsbreslav/quicklook/blob/master/images/plots/line/complete_example.png)