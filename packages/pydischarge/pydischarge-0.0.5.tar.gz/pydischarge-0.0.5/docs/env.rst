#####################################
Configuring pyDischarge from the environment
#####################################

pyDischarge can be configured by setting environment variables at run time.
Each of the variables are boolean switches, meaning they just tell pyDischarge to
do something, or not to do something. The following values match as `True`:

- ``'y'``
- ``'yes'``
- ``'1'``
- ``'true'``

And these match as `False`:

- ``'n'``
- ``'no'``
- ``'0'``
- ``'false'``

The matching is **case-independent**, so, for example, ``'TRUE'`` will
match as `True`.

The following variables are defined:

+---------------------+---------+---------------------------------------------+
| Variable            | Default | Purpose                                     |
+=====================+=========+=============================================+
| ``PYDISCHARGE_CACHE``      | `False` | Whether to cache downloaded files from      |
|                     |         | GWOSC to prevent repeated downloads         |
+---------------------+---------+---------------------------------------------+
| ``PYDISCHARGE_RCPARAMS``   | `True`  | Whether to update `matplotlib.rcParams`     |
|                     |         | with custom pyDischarge defaults for rendering     |
|                     |         | images                                      |
+---------------------+---------+---------------------------------------------+
| ``PYDISCHARGE_USETEX``     | `False` | Whether to use LaTeX when rendering images, |
|                     |         | only used when ``PYDISCHARGE_RCPARAMS`` is `True`  |
+---------------------+---------+---------------------------------------------+
