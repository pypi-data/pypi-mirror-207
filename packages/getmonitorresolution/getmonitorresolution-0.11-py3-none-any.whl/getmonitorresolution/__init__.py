import ctypes
from ctypes import wintypes
windll = ctypes.LibraryLoader(ctypes.WinDLL)
user32 = windll.user32


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
    """
    windll.shcore.SetProcessDpiAwareness(dpi_awareness)
    def _get_monitors_resolution():
        monitors = []
        monitor_enum_proc = ctypes.WINFUNCTYPE(
            ctypes.c_int,
            ctypes.c_ulong,
            ctypes.c_ulong,
            ctypes.POINTER(ctypes.wintypes.RECT),
            ctypes.c_double,
        )

        def callback(hMonitor, hdcMonitor, lprcMonitor, dwData):
            monitors.append(
                (
                    lprcMonitor.contents.right - lprcMonitor.contents.left,
                    lprcMonitor.contents.bottom - lprcMonitor.contents.top,
                )
            )
            return 1

        user32.EnumDisplayMonitors(None, None, monitor_enum_proc(callback), 0)
        return monitors

    resolutions = _get_monitors_resolution()
    allmoni = {}
    for i, res in enumerate(resolutions):
        allmoni[i] = {"width": res[0], "height": res[1]}
    moninfos = {
        'width_all_monitors': sum([q[1]["width"] for q in allmoni.items()]),
        'height_all_monitors': max([q[1]["height"] for q in allmoni.items()]),
        'max_monitor_width': max([q[1]["width"] for q in allmoni.items()]),
        'min_monitor_width': min([q[1]["width"] for q in allmoni.items()]),
        'max_monitor_height': max([q[1]["height"] for q in allmoni.items()]),
        'min_monitor_height': min([q[1]["height"] for q in allmoni.items()]),

    }
    return allmoni, moninfos


