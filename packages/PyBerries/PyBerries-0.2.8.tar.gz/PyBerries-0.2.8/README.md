# PyBerries

PyBerries is a Python package that can be used to import, manipulate and plot data from Bacmman measurement tables.

It relies mainly on Pandas for data handling and Seaborn/Matplotlib for plotting.

[[_TOC_]]

----

## Installation

<details>
  <summary markdown="span">Anaconda (recommended)</summary>

  Anaconda will install both Python and Jupyter-lab (used to run Python notebooks) easily. Note however that it requires ~5 Gb free disk space.
  For a lighter installation procedure, see the next section "Command line install".

  - Download Anaconda from the [official website](https://www.anaconda.com/)
  - Run the installer (leave all options as default)
  - Start "Anaconda Navigator"
  - In Anaconda, launch the "Jupyter Lab" module
</details>

<details>
  <summary markdown="span">Command line install (advanced users)</summary>

  - Open a terminal (macOS/Linux) or Powershell (Windows)
  - Install Python
      - Enter the command `python --version`
      - If an error or a version < 3.9 is shown, download and install Python from the [official website](https://www.python.org/downloads/)
  - After installing, restart your terminal/powershell; both of the above commands should display a version number
  - Install Jupyter Lab
      - In a terminal/powershell, run the command `python -m pip install jupyterlab`
      - After the installation completes, Jupyter Lab can be started using the command `jupyter-lab`
</details>

## Using existing notebooks

- Download the relevant notebooks from the [Notebook folder](https://gitlab.com/MEKlab/pyberries/-/tree/main/Notebooks) (you will have to click on individual notebooks and click on the "download" button at the top-right).
- Start Jupyter Lab
- In the left panel of Jupyter lab, click on "Upload file" and select the notebook you have downloaded
    - The notebook will appear in the list of files and folders
    - Click on the notebook on the list to open it

A Python notebook consists of a mix of text and code cells.
- Update the code where necessary (e.g. "Input" cell, plot options...)
- Run individual code cells by clicking on them and pressing Shift + Enter
- Once a dataset has been imported, you can run any cell from the "Figures" section (order is not important)
- If you change plot options, re-run the corresponding cell to update the plot
- When running your mouse over a plot, a "save" button should appear

## Using the PyBerries package in your own code (advanced users)

To install the package, use the following command in a terminal:

`python -m pip install PyBerries`

You can also install a specific version number (useful e.g. to make sure you code won't be broken by a future update):

`python -m pip install PyBerries==0.2.6.post1`

### Creating a DatasetPool

📖 [DatasetPool documentation](./doc/DatasetPool.md)

To import Bacmman measurement tables with PyBerries, you must create a "DatasetPool" (an object that will contain one or several Bacmman datasets). The minimum required arguments to create a DatasetPool are:
- `dsList`: name(s) of the Bacmman datasets to be imported
- `path`: path to the Bacmman folder containing the datasets

Optional arguments can be added:
- `groups`: set legend labels for the datasets. If two datasets have the same label, they will be concatenated (and error bars can be shown if supported)
  - Format: `groups = ['Group1', 'Group2', 'Group3']` with a number of groups equal to the number of datasets in dsList
- `filters`: filter the datasets using the syntax of [pandas.DataFrame.query](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html)
  - Format: `filters = {'object':'filter'}`, where object is the name of the target Bacmman object
  - Example: `filters = {'Bacteria':'SpineLength > 3'}` to keep only Bacteria that have a length > 3
  - Note that filtering an object will also filter out any child objects (e.g. if a bacteria is removed, the spots it contains will be removed as well)
- `metadata`: enter the name of a metadata field (found in the `SourceImageMetadata` folder of the dataset) to add a column with the corresponding metadata value for each position.
  - Format: `metadata = {'object':'metadata_name'}` where object is the Bacmman object to which the metadata should be added
  - Example: `metadata = {'Bacteria':'DateTime'}` will add the acquisition time for each position in the Bacteria table
- `preprocessing`: a function to be applied to each measurement table before it is added to the dataset
  - Format: `preprocessing = {'object':function}`
  - Tip: lambda functions can be an easy way to perform simple tasks such as renaming a column: `preprocessing = {'Bacteria':lambda df: df.rename(columns={'Old_name':'New_name'}}`

Note: all arguments can either take a single value to be applied to all datasets, or one value per dataset in dsList.
- Example: `filters = {'Bacteria':['SpineLength > 3','']}` will apply the cell length filter to the first, but not to the second dataset

Example of DatasetPool creation:
```python
from pyberries.data import DatasetPool
data = DatasetPool(path=['D:/Daniel/BACMMAN/Timelapse'], dsList=['230118_DT23'], groups=[], metadata={'Bacteria':'DateTime'}, filters={}, preprocessing={})
```

#### About filtering

Filtering is applied when creating a DatasetPool, but can also be applied afterwards with the `apply_filters` method. Example:
```python
data.apply_filters({'Bacteria':'SpineLength > 3'})
```


### Data format

The Bacmman measurement tables will be imported, and tables from objects that have the same name will be concatenated as a single Pandas DataFrame. The `Dataset` column specifies which Bacmman dataset a given line belongs to.

Measurement tables are stored in a dictionary (`{object_name:table}`) under the `table` property.

For example, to display the data contained in the 'Bacteria' table, run in a Jupyter Notebook:
```python
display(data.table['Bacteria'])
```


### Dataset summary

You can use the `describe` method to print a summary of all numerical columns in the DatasetPool. One or several aggregation methods can be specified, for example:
```python
data.describe('median')
```
to print the median value for each column, or
```python
data.describe(['mean', 'std'])
```
to print mean and standard deviation.

Other aggregations are possible, including (but not limited to): `'max'`, `'min'`, `'sum'`, `'sem'`. For more details on aggregations, consult [pandas.DataFrame.aggregate](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.aggregate.html).

Output can be limited to certain columns by using the keyword `include`:
```python
data.describe(['mean', 'std'], include=['SpineLength', 'SpineWidth'])
```


### Adding columns

The `add_columns` method allows adding predefined calculations (metrics) to the dataset. Current possible metrics are:
- `'heatmap'`
- `'is_col_larger'`
- `'bin_column'`
- `'Dapp'`

Example use:
```python
data.add_columns(object_name='Spots', metrics=['Heatmap'])
```

Details on metrics can be found in [DatasetPool.add_columns](./doc/DatasetPool.add_columns.md)


### Adding a column from a parent table

If 'Bacteria' is a parent of 'Spots', it is possible to add data from the parent table to the child's. For example if the 'Bacteria' table contains lineage information, we can add to each spot the lineage of its parent bacteria.

For example:
```python
data.add_from_parent(object_name='Spots', col='lineage')
```

Note that the parent table will be automatically inferred from the Bacmman configuration file.


### Timeseries data

If the metadata `'DateTime'` has been included in the dataset, it is possible to perform a time-binning on the data in order to plot metrics at different time resolutions. This is done by using the method `get_timeseries`. The different timeseries metrics available are:
- `'SpineLength'`
- `'ObjectCount'`
- `'ObjectClass'`
- `'Intensity'`
- `'Quantile'`
- `'Aggregation'`
- `'Fluo_intensity'`
- `'FOV_Positions'`

The resulting dataframe is stored in the `timeseries` property of the dataset (can be shown by `display(data.timeseries['Bacteria'])`).

Example use:
```python
timeseries_parameters = {'metric':'ObjectCount', # Metric to be plotted
                         'col':'SpotCount', # Column to be used from the source data
                         'timeBin':2, # Time interval in min
                         'thr':1 # For 'ObjectCount': threshold on number of objects to include in 'ObjectFrac' column
                        }
data.get_timeseries(object_name='Bacteria', **timeseries_parameters)
```

For more details on timeseries options, see [DatasetPool.get_timeseries](./doc/DatasetPool.get_timeseries.md)


### Making figures

PyBerries uses Seaborn and Matplotlib to plot data. There are three different ways to create plots:
- Through a DatasetPool method (`plot_preset`)
  - This is the preferred method, since it will take care of properly displaying all plot elements for the given task
  - Presets also include several plots which combine several elements (e.g. `plot_timeseries` which displays both a scatter and a lineplot)
- By importing plots from pyberries.plots
  - This allows a bit more flexibility, while still taking care of legend, axis labels, etc.
- By importing plot functions from Seaborn
  - This will give you the most flexibility, but will require a lot of manual fixing for plot limits, axis labels, legend,...

For more details on Seaborn, visit [](https://seaborn.pydata.org/api.html)

#### DatasetPool plotting methods

The plot preset function takes the following arguments:
- preset (str): type of plot to make
- object_name (str): table to plot from
- timeseries (bool): set to *True* to plot from a timeseries table, and to *False* (default) to plot from the normal measurement table
- drop_duplicates_by (list of str): before plotting, remove all lines that are duplicates according to the column (or combination of columns) specified
- return_axes (bool): return figure axis to enable further changes/additional plots to be added
- title (str): plot title
- xlabel, ylabel (str): X and Y axis labels
- xlim, ylim (2-tuple): X and Y axis limits
- **kwargs: any arguments to be passed to the seaborn plot

Available presets are:
- `histogram`
- `bar`
- `line`
- `scatter`
- `datapoints_and_mean`
- `heatmap`
- `timeseries`
- `boxenplot`
- `spot_tracks`

Example use:
```python
plot_args = {'x':'Bacteria_Size',
            'hue':'Group',
            'binwidth':2,
            'stat':'probability',
            'common_norm':False,
            'errorbars':None,
            'title':'',
            'xlabel':'Cell area (µm$^2$)',
            'ylabel':'Probability',
            'xlim':(None, None),
            'ylim':(None, None),
            'multiple':'layer',
            'element':'poly',
            'kde':False,
            'palette':'deep',
            }

data.plot_preset(preset='histogram', object_name='Bacteria', **plot_args)
```

The additional argument `return_axes` can be passed to all dataset plot methods to enable further modifications to the figure:
```python
import seaborn as sns

ax = data.plot_preset(preset='histogram', object_name='Bacteria', return_axes=True, **plot_args)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1), labelspacing=1)
```
moves the legend outside of the plot.


#### Importing from pyberries.plots

Seaborn plots can be imported from pyberries.plots.
The example above could then be written:
```python
from pyberries.plot import histplot

plot_args = {'x':'Bacteria_Size',
            'hue':'Group',
            'binwidth':2,
            'stat':'probability',
            'common_norm':False,
            'title':'',
            'xlabel':'Cell area (µm$^2$)',
            'ylabel':'Probability',
            'xlim':(None, None),
            'ylim':(None, None),
            'multiple':'layer',
            'element':'poly',
            'kde':False,
            'palette':'deep',
            }

_,ax = plt.subplots(dpi=130)
ax = histplot(data.table['Bacteria'], ax=ax, **plot_args)
```

Note that histogram errorbars are only available when plotting through the dataset method.


#### Importing from Seaborn

When directly using Seaborn, the histogram above can be produced like this:
```python
import seaborn as sns

plot_args = {'x':'Bacteria_Size',
            'hue':'Group',
            'binwidth':2,
            'stat':'probability',
            'common_norm':False,
            'multiple':'layer',
            'element':'poly',
            'kde':False,
            'palette':'deep',
            }

_,ax = plt.subplots(dpi=130)
g = sns.histplot(data=data.table['Bacteria'], **plot_args)
g.set(xlabel='Cell area (µm$^2$)', ylabel='Probability', title='Plot title', xlim=(None, None), ylim=(None, None))
if not g.get_legend() == None: g.get_legend().set_title("")
```



## File utilities
Collection of functions to manipulate:
- File names
  - Zero-padding on numbers
  - Replace a string by another
  - Add a string to the end of all file names
- Tiff files
  - Make a tiff stack from single tiff files that have the same ending
  - Update axis description in files metadata
  - Make copies of a tiff file with am increasing ID number as suffix
- Folders downloaded from Omero
  - Move files from nested Omero folders to the same folder
