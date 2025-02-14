# guidata Releases #

## Version 3.0.1 ##

API changes (fixes inconsistencies in API):

* Moved `guidata.dataset.iniio.WriterMixin` to `guidata.dataset.io.WriterMixin`
* Moved `guidata.dataset.iniio.BaseIOHandler` to `guidata.dataset.io.BaseIOHandler`
* Moved `guidata.dataset.iniio` to `guidata.dataset.io.inifmt` and renamed:
  * `UserConfigIOHandler` to `INIHandler`
  * `UserConfigWriter` to `INIWriter`
  * `UserConfigReader` to `INIReader`
* Moved `guidata.dataset.jsonio` to `guidata.dataset.io.jsonfmt`
* Moved `guidata.dataset.hdf5io` to `guidata.dataset.io.h5fmt`

Bug fixes:

* Modules `guidata.dataset.datatypes` and `guidata.dataset.dataitems` should not
  critically depend on Qt (only modules specific to GUI should depend on Qt, such
  as `guidata.dataset.qtwidgets`). This was a regression introduced in version 3.0.0.
  A new unit test was added to prevent this kind of regression in the future.

* Fixed documentation generation ``.readthedocs.yaml`` file (Qt 5.15 was not
  installed on ReadTheDocs servers, causing documentation build to fail)

Other changes:

* [Pull Request #55](https://github.com/Codra-Ingenierie-Informatique/guidata/pull/55) - DateItem and DateTimeItem: added 'format' parameter for formatting, by [@robochat](https://github.com/robochat)

* Packaging: still using `setuptools`, switched from `setup.cfg` to `pyproject.toml`
  for configuration (see [PEP 517](https://www.python.org/dev/peps/pep-0517/))

## Version 3.0.0 ##

New major release:

* New BSD 3-Clause License
* Black code formatting on all Python files
* New automated test suite:
  * Added module `guidata.env` to handle execution environment
  * Added support for an "unattended" execution mode (Qt loop is bypassed)
  * Added support for pytest fixtures
  * Added support for coverage testing: 70% coverage to date
* Documentation was entirely rewritten using Sphinx
* Reorganized modules:
  * Moved `guidata.hd5io` to `guidata.dataset.hdf5io`
  * Moved `guidata.jsonio` to `guidata.dataset.jsonio`
  * Renamed `guidata.userconfigio` to `guidata.dataset.iniio`
  * New package `guidata.utils` for utility functions:
    * Removed deprecated or unused functions in old `guidata.utils` module
    * Moved old `guidata.utils` module to `guidata.utils.misc`, except the
      functions `update_dataset` and `restore_dataset` which are still in
      `guidata.utils` (root module)
    * Moved `guidata.encoding` to `guidata.utils.encoding`
    * Moved `guidata.gettext_helpers` to `guidata.utils.gettext_helpers`
  * Splitted `guidata.qtwidgets` in two modules:
    * `guidata.widgets.dockable` for dockable widgets
    * `guidata.widgets.rotatedlabel` for rotated label
* Other changes:
  * `guidata.guitest`:
    * Added support for subpackages
    * New comment directive (``# guitest: show``) to add test module to test suite or
      to show test module in test launcher (this replaces the old ``SHOW = True`` line)
  * `guidata.dataset.datatypes.DataSet`: new `create` class method for concise
    dataset creation, allowing to create a dataset with a single line of code by
    passing default item values as keyword arguments

## Version 2.3.1 ##

Bug fixes:

* Fixed critical compatibility issue with Python 3.11 (`codeset` argument was removed
  from `gettext.translation` function)
* Fixed support for `DateTimeItem` and `DateItem` objects serializing (HDF5 and JSON)
* Fixed JSONReader constructor documentation: more explicit docstring
* Fixed test_dataframeeditor.py test script (issue with QApplication creation)

## Version 2.3.0 ##

Changes:

* Added JSON serialize/deserialize support for `DataSet` objects (from CodraFT project,
  <https://codra-ingenierie-informatique.github.io/CodraFT/>)
* Array editor: switching to read-only mode when array is not writeable
* Object editor (`oedit` function): cleaner implementation, handling widget
  parenting (code specifically related to Spyder internal shell was removed)

Bug fixes:

* Array editor: fixed error when NumPy array flag "writeable" is False,
  do not try to change flag value since it's a deprecated feature since NumPy v1.17
* Do not install Qt translator and set color mode (dark/light) on Qt application if
  it already has been initialized (QApplication instance is not None)

## Version 2.2.1 ##

Bug fixes:

* Collection editor: fixed "Save array" feature
* Console widget context menu: added missing icons

## Version 2.2.0 ##

Changes:

* FloatArrayItem: added data type information on associated widget
* guitest.TestModule.run: added timeout argument to wait for process termination

Bug fixes:

* FloatArrayItem: avoid RuntimeWarning when dealing with complex data
* external/darkdetect: fixed compatibility issue with Windows Server 2008 R2

## Version 2.1.1 ##

Bug fixes:

* win32_fix_title_bar_background: not working in 32bits

## Version 2.1.0 ##

Changes:

* Dark mode may be overriden by QT_COLOR_MODE environment variable

## Version 2.0.4 ##

Bug fixes:

* Fixed missing import for DictItem callback

## Version 2.0.3 ##

Changes:

* Code editor: added support for other languages than Python (C++, XML, ...)

Bug fixes:

* Fixed Qt5 translation standard support
* Fixed code editor/console widgets dark mode default settings

## Version 2.0.2 ##

Bug fixes:

* Fixed PySide6 compatibility issues
* Fixed remaining Python 3 compatibility issues

## Version 2.0.1 ##

Bug fixes:

* Fixed Python 3 compatibility issues

## Version 2.0.0 ##

Changes:

* Removed support for Python 2.7 and PyQt4 (guidata supports Python >=3.6 and PyQt5, PySide2, PyQt6, PySide6 through QtPy 2)
* Added support for dark theme mode on Windows (including windows title bar background),
  MacOS and GNU/Linux.
* Added embbeded Qt-based Python console widget
* Dataset edit layout: now disabling/enabling "Apply" button depending on widget value changes
* Code editor: widget minimum size area may now be set using rows and columns size
* Test launcher: redesigned, added support for dark mode

## Version 1.8.0 ##

Changes:

* Added generic widgets: array, dictionnary, text and code editors.
* Removed `spyderlib`/`spyder` dependency.
* Added setter method on DataItem object for "help" text (fixed part of the tooltip).

## Version 1.7.9 ##

Changes:

* Added PySide2 support: guidata is now compatible with Python 2.7, Python 3.4+, PyQt4,
  PyQt5 and PySide2!

## Version 1.7.8 ##

Changes:

* Added PyQt4/PyQt5/PySide automatic switch depending on installed libraries
* Moved documentation to <https://docs.readthedocs.io/>

## Version 1.7.7 ##

Bug fixes:

* Fixed Spyder v4.0 compatibility issues.

## Version 1.7.6 ##

Bug fixes:

* Fixed Spyder v3.0 compatibility issues.

## Version 1.7.5 ##

Bug fixes:

* `FilesOpenItem.check_value` : if value is None, return False (avoids "None Type object is not iterable" error)

## Version 1.7.4 ##

Bug fixes:

* Fixed compatibility issue with Python 3.5.1rc1 (Issue #32: RecursionError in `userconfig.UserConfig.get`)
* `HDF5Reader.read_object_list`: fixed division by zero (when count was 1)
* `hdf5io`: fixed Python3 compatibility issue with unicode_hdf type converter

## Version 1.7.3 ##

Features:

* Added CHM documentation to wheel package
* hdf5io: added support for a progress bar callback in "read_object_list" (this allows implementing a progress dialog widget showing the progress when reading an object list in an HDF5 file)

Bug fixes:

* Python 3 compatibility: fixed `hdf5io.HDF5Writer.write_object_list` method
* data items:
  * StringItem: when `notempty` parameter was set to True, item value was not checked at startup (expected orange background)
* disthelpers:
  * Supporting recent versions of SciPy, h5py and IPython
  * Fixed compatibility issue (workaround) with IPython on Python 2.7 (that is the "collection.sys cx_Freeze error")

## Version 1.7.2 ##

Bug fixes:

* Fixed compatibility issues with old versions of Spyder (<v2.3)

## Version 1.7.1 ##

Bug fixes:

* Fixed Issue #25: ConfigParser.get unexpected keyword argument 'raw'
* Fixed tests failures: disthelpers, guiqwt/tests/loadsaveitems_hdf5.py

Features:

* userconfigio: added support for serializing/deserializing NumPy scalars
* Fixed Issue #47: added support for DateTimeItem/DateItem (de)serialization

Setup:

* Using setuptools "entry_points" instead of distutils "scripts"

## Version 1.7.0 ##

Possible API compatibility issues:

* Added support for PyQt5 (removed old-style signals)

## Version 1.6.1 ##

Possible API compatibility issues:

* disthelpers:
  * Changed arguments from "architecture=None, python_version=None" to "msvc_version, architecture=None"

## Version 1.6.0 ##

Added support for Python 3 (see module `guidata.py3compat`).

New features:

* disthelpers:
  * Added support for Python 3.3
  * Added support for pygments (and partial support for zmq: still failing)
* FloatArrayItem: added support for `unit` property value

Bug fixes:

* disthelpers.prepend_module_to_path: unload modules which were already imported to be able to replace them by other versions (mostly `guidata` should be concerned by this if the function is used -as it should be- in package's __init__.py script)

## Version 1.5.1 ##

New features:

* HDF5 serialization (HDF5 reader/writer):
  * Added context manager
  * Added convenience methods `read` and `write`
  * Added convenience methods `write_object_list` and `read_object_list` to save/restore objects implementing DataSet-like `serialize` and `deserialize` methods
* Datasets I/O (HDF5/ini): None values (unset items) can now be saved/loaded for FloatItem, IntItem and BoolItem objects
* disthelpers: added option 'exclude_dirs' to 'add_module_data_files' and 'add_module_data_dir' methods
* Added slider support for FloatItem objects (contributor: julien.jaeck)
* (Issue 21) Added option 'size' in dataset `edit` and `view` methods to resize the generated dialog box (size may be a tuple of integers (width, height) or a QSize object)

Possible API compatibility issues:

* guidata now requires Python 2.6 (Python 2.5 support has been dropped)

Bug fixes:

* DataSet objects (de)serialization: fixed HDF5 reader/writer for FilesOpenItem and FloatArrayItem serialize/deserialize methods
* Fixed DataSet userconfig read/write test
* StringItem/ColorItem: fixed unicode/str issues in deserialization methods
* Added support for strings encoded in file system charset to avoid an error like "String %r is not UTF-8 encoded" when trying to set an item to a string value (path) obtained with a file system command
* configtools/image paths: handling file system encoded paths
* (Issue 14) Restored compatiblity with PyQt v4.4

## Version 1.5.0 ##

Bug fixes:

* Fixed 'callback' property related issue: when updating a DataSetShowGroupBox or
DataSetEditGroupBox internal dataset, the callback property was causing a reset
of the data items to their default values

Possible API compatibility issues:

* datatypes.OperatorProperty was renamed to FuncProp

Other changes:

* Added test for the FuncProp item property: how to change an item active state depending on another item's value
* Added support for dictionaries for `update_dataset` and `restore_dataset` (functions of `guidata.utils`):
  * `update_dataset` may update the destination dataset from a source dictionary
  * `restore_dataset` may update the destination dictionary from a source dataset
* FloatArrayItem: added option "large" to show all the array values in read-only mode
* Added new guidata svg logo
* disthelpers:
  * added support for PySide
    * disthelpers: new function 'get_visual_studio_dlls' -- returns the list of Visual
Studio DLLs (and create manifest) associated to Python architecture and version

## Version 1.4.2 ##

Bug fixes:

* disthelpers:
  * the vs2008 option was accidently turned off by default on Windows platforms
  * build_chm.bat: added support for Windows x64

Other changes:

* dataset.qtwidgets:
  * QLabel widgets word wrapping is now disabled for read-only items and may be disabled for dataset comments: this is necessary because when the parent widget height is constrained, Qt is unexpectedly reducing the height of word-wrapped QLabel widgets below their minimum size, hence truncating their contents...
* disthelpers:
  * raising an exception when the right version of Ms Visual C++ DLLs was not found
  * now creating the manifest and distributing from the redistribuable package installed in WinSxS

## Version 1.4.1 ##

Bug fixes:

* ColorItem for recent versions of Qt: in QLineEdit widget, the text representation of color was str(QColor(...)) instead of str(QColor(...).name())
* guidata.qt compat package: fixed _modname typo
* hdf5io:
  * optional attribute mechanism generalized to both Attr and DSet objects (for both saving and loading data)
  * H5Store/`close` method: now checking if h5 file has already been closed before trying to close it (see <http://code.google.com/p/h5py/issues/detail?id=220>)
* disthelpers:
  * vs2008 option was ignored
  * added 'C:\Program Files (x86)' to bin includes (cx_Freeze)
* Data items/callbacks: fixed callbacks for ChoiceItem (or derived items) which were triggered when other widgets were triggering their own callbacks...

Other changes:

* Added test for item callbacks
* dataset.datatypes.FormatProp/new behavior: added `ignore_error` argument, default to True (ignores string formatting error: ValueError)
* disthelpers:
  * Distribution.Setup: added `target_dir` option
  * Distribution.build: added `create_archive` option to create a ZIP archive after building the package
  * cx_Freeze: added support for multiple executables
  * added support for h5py 2.0
  * added support for Maplotlib 1.1
* Allow DateTime edit widgets to popup calendar

## Version 1.4.0 ##

Possible API compatibility issues:

* disthelpers: removed functions remove_build_dist, add_module_data_files,
    add_text_data_file, get_default_excludes, get_default_includes,
    get_default_dll_excludes, create_vs2008_data_files (...) which were
    replaced by a class named Distribution,
    see the new disthelpers test for more details (tests/dishelpers.py)
* reorganized utils and configtools modules

Other changes:

* disthelpers: replaced almost all functions by a class named Distribution,
    and added support for cx_Freeze (module remains compatible with py2exe),
    see the new disthelpers test for more details (tests/dishelpers.py)
* reorganized utils and configtools modules

## Version 1.3.2 ##

Since this version, `guidata` is compatible with PyQt4 API #1 *and* API #2.
Please read carefully the coding guidelines which have been recently added to
the documentation.

Possible API compatibility issues:

* Removed deprecated wrappers around QFileDialog's static methods (use the wrappers provided by `guidata.qt.compat` instead):
  * getExistingDirectory, getOpenFileName, getOpenFileNames, getSaveFileName

Bug fixes:

* qtwidgets.ShowFloatArrayWidget: fixed string float formatting issue (replaced %f by %g)
* Fixed compatiblity issues with PyQt v4.4 (Contributor: Carlos Pascual)
* Fixed missing 'child_title' attribute error with FileOpenItem, FilesOpenItem, FileSaveItem and DirectoryItem
* (Fixes Issue 8) disthelpers.add_modules was failing when vs2008=False

Other changes:

* added *this* changelog
* qtwidgets: removed ProgressPopUp dialog (it is now recommended to use QProgressDialog instead, which is pretty much identical)
* Replaced QScintilla by spyderlib (as a dependency for array editor, code editor (test launcher) and dict editor)
* qtwidgets.DockWidgetMixin: added method 'setup_dockwidget' to change dockwidget's features, location and allowed areas after class instantiation
* guidata.utils.utf8_to_unicode: translated error message in english
* Add support for 'int' in hdf5 save function
* guidata.dataset/Numeric items (FloatItem, IntItem): added option 'unit' (automatically add suffix ' (unit)' to label in edit mode and suffix ' unit' to value in read-only mode)
* Improved dataset __str__ method: code refactoring with read-only dataset widgets (DataItem: added methods 'format_string' and 'get_string_value', DataSet: added method 'to_string')
* Added coding guidelines to the documentation
* guidata.dataset.qtwidget: added specific widget (ShowBooleanWidget) for read-only display of bool items (text is striked out when value is False)
* guidata.hdf5io.Dset: added missing keyword argument 'optional' (same effect as parent class Attr)
* guidata.dataset.dataitems.IntItem objects: added support for sliders (fixes Issue 9) with option slider=True (see documentation)

## Version 1.3.1 ##

Bug fixes:

* setup.py: added svg icons to data files
* gettext helpers were not working on Linux (Windows install pygettext was hardcoded)

Other changes:

* hdf5io: printing error messages in sys.stderr + added more infos when failing to load attribute

## Version 1.3.0 ##

Bug fixes:

* setup.py: added svg icons to data files
* gettext helpers were not working on Linux (Windows install pygettext was hardcoded)
* DataSet/bugfix: comment/title options now override the DataSet class __doc__ attribute
* Added missing option 'basedir' for FilesOpenItem
* DirectoryItem: fixed missing child_title attribute bug
* For all DataSet GUI representation, the comment text is now word-wrapped
* Bugfix: recent versions of PyQt don't like the QApplication reference to be stored in modules (why is that?)
* Bugfix/tests: always keep a reference to the QApplication instance

Other changes:

* setup.py: added source archive download url
* Tests: now creating real temporary files and cleaning up at exit
* qtAllow a callback on LineEditWidget to notify about text changes (use set_prop("display", "callback", callback))
* qthelpers: provide wrapper for qt.getOpen/SaveFileName to work around win32 bug
* qtwidgets: optionally hide apply button in DataSetEditGroupBox
* added module guidata.qtwidgets (moved some generic widgets from guidata.qthelpers and from other external packages)
* qthelpers: added helper 'create_groupbox' (QGroupBox object creation)
* Array editor: updated code from Spyder's array editor (original code)
* Added package guidata.editors: contains editor widgets derived from Spyder editor widgets (array editor, dictionary editor, text editor)
* Array editor: added option to set row/col labels (resp. ylabels and xlabels)
* ButtonItem: changed callback arguments to*instance* (DataSet object), *value* (item value), *parent* (button's parent widget)
* editors.DictEditor.DictEditor: moved options from constructor to 'setup' method (like ArrayEditor's setup_and_check), added parent widget to constructor options
* Added DictItem type: simple button to edit a dictionary
* editors.DictEditor.DictEditor/bugfixes: added action "Insert" to context menu for an empty dictionary + fixed inline unicode editing (was showing the error message "Unable to assign data to item")
* guidata.qtwidgets: added 'DockableWidgetMixin' to fabricate any dockable QWidget class
* gettext helpers: added support for individual module translation (until now, only whole packages were supported)
* DataSetShowGroupBox/DataSetEditGroupBox: **kwargs may now be passed to the DataSet constructor
* disthelpers: added 'scipy.io' to supported modules (includes)
* Added new "value_callback" display property: this function is called when QLineEdit text has changed (item value is passed)
* Added option to pass a text formatting function in DataSetShowWidget
