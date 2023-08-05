# Uses ctypes to get the resolution information of all available monitors

## pip install getmonitorresolution

#### Tested against Windows 10 / Python 3.10 / Anaconda

```python
The get_monitors_resolution() function retrieves the resolution information of all available monitors on a Windows machine. It takes an optional parameter dpi_awareness, which sets the DPI awareness level. The function returns a tuple containing two dictionaries, allmoni and moninfos.

allmoni is a dictionary containing the resolution details of all available monitors, with the monitor index as the key. The values of the dictionary are also dictionaries containing the width and height of each monitor.

moninfos is a dictionary containing the following resolution information of all the available monitors:

width_all_monitors: The combined width of all the monitors.
height_all_monitors: The maximum height among all the monitors.
max_monitor_width: The maximum width of all the monitors.
min_monitor_width: The minimum width of all the monitors.
max_monitor_height: The maximum height of all the monitors.
min_monitor_height: The minimum height of all the monitors.


def get_monitors_resolution(dpi_awareness=2):
    """
    Retrieves the resolution information of all the available monitors and returns the resolution details in a dictionary format.

    Args:
        dpi_awareness (int): Optional parameter to set DPI awareness level. Default is 2, which is the highest level of DPI awareness.

    Returns:
        tuple: A tuple containing two dictionaries, `allmoni` and `moninfos`.
        - `allmoni` (dict): A dictionary containing the resolution details of all available monitors, with the monitor index as key.
        - `moninfos` (dict): A dictionary containing the following resolution information of all the available monitors:
            * width_all_monitors (int): The combined width of all the monitors.
            * height_all_monitors (int): The maximum height among all the monitors.
            * max_monitor_width (int): The maximum width of all the monitors.
            * min_monitor_width (int): The minimum width of all the monitors.
            * max_monitor_height (int): The maximum height of all the monitors.
            * min_monitor_height (int): The minimum height of all the monitors.
			
			

from getmonitorresolution import get_monitors_resolution
eachmonitor,general = get_monitors_resolution()
print(eachmonitor)
print(general)

# output 
{0: {'width': 1920, 'height': 1080}, 1: {'width': 1920, 'height': 1080}}
{'width_all_monitors': 3840, 'height_all_monitors': 1920, 'max_monitor_width': 1920, 'min_monitor_width': 1920, 'max_monitor_height': 1080, 'min_monitor_height': 1080}

```