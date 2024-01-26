#! /usr/bin/python3
# -*- coding:Utf-8 -*-
"""
tkcalendar - System tray unread mail checker
Copyright 2016-2018 Juliette Monsel <j_4321@protonmail.com>

tkcalendar is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

tkcalendar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


Tooltip and TooltipWrapper
"""
from sys import platform
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk


class Tooltip(tk.Toplevel):
    """Tooltip widget displays a ttk.Label in a Toplevel without window decoration."""

    _initialized = False

    def __init__(self, parent, **kwargs):
        """
        Construct a Tooltip with parent master.

        Keyword Options
        ---------------

        ttk.Label options,

        alpha: float. Tooltip opacity between 0 and 1.
        """
        tk.Toplevel.__init__(self, parent, padx=0, pady=0)
        self.transient(parent)
        self.overrideredirect(True)
        self.update_idletasks()
        self.attributes('-alpha', kwargs.pop('alpha', 0.8))
        if platform == 'linux':
            self.attributes('-type', 'tooltip')

        if not Tooltip._initialized:
            # default tooltip style
            style = ttk.Style(self)
            style.configure('tooltip.TLabel',
                            foreground='gray90',
                            background='black',
                            font='TkDefaultFont 9 bold')
            Tooltip._initialized = True

        # default options
        kw = {'compound': 'left', 'style': 'tooltip.TLabel', 'padding': 4}
        # update with given options
        kw.update(kwargs)

        self.label = ttk.Label(self, **kw)
        self.label.pack(fill='both')

        self.config = self.configure

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def __getitem__(self, key):
        return self.cget(key)

    def cget(self, key):
        if key == 'alpha':
            return self.attributes('-alpha')
        else:
            return self.label.cget(key)

    def configure(self, **kwargs):
        if 'alpha' in kwargs:
            self.attributes('-alpha', kwargs.pop('alpha'))
        self.label.configure(**kwargs)

    def keys(self):
        keys = list(self.label.keys())
        keys.insert(0, 'alpha')
        return keys


class TooltipWrapper:
    """
    Tooltip wrapper widget handle tooltip display when the mouse hovers over
    widgets.
    """
    def __init__(self, master, **kwargs):
        """
        Construct a Tooltip wrapper with parent master.

        Keyword Options
        ---------------

        Tooltip options,

        delay: time (ms) the mouse has to stay still over the widget before
        the Tooltip is displayed.

        """
        self.widgets = {}  # {widget name: tooltip text, ...}
        # keep track of binding ids to cleanly remove them
        self.bind_enter_ids = {}  # {widget name: bind id, ...}
        self.bind_leave_ids = {}  # {widget name: bind id, ...}

        # time delay before displaying the tooltip
        self._delay = 2000
        self._timer_id = None

        self.tooltip = Tooltip(master)
        self.tooltip.withdraw()
        # widget currently under the mouse if among wrapped widgets:
        self.current_widget = None

        self.configure(**kwargs)

        self.config = self.configure

        self.tooltip.bind('<Leave>', self._on_leave_tooltip)

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def __getitem__(self, key):
        return self.cget(key)

    def cget(self, key):
        if key == 'delay':
            return self._delay
        else:
            return self.tooltip.cget(key)

    def configure(self, **kwargs):
        try:
            self._delay = int(kwargs.pop('delay', self._delay))
        except ValueError:
            raise ValueError('expected integer for the delay option.')
        self.tooltip.configure(**kwargs)

    def add_tooltip(self, widget, text):
        """Add new widget to wrapper."""
        self.widgets[str(widget)] = text
        self.bind_enter_ids[str(widget)] = widget.bind('<Enter>', self._on_enter)
        self.bind_leave_ids[str(widget)] = widget.bind('<Leave>', self._on_leave)

    def set_tooltip_text(self, widget, text):
        """Change tooltip text for given widget."""
        self.widgets[str(widget)] = text

    def remove_all(self):
        """Remove all tooltips."""
        for name in self.widgets:
            widget = self.tooltip.nametowidget(name)
            widget.unbind('<Enter>', self.bind_enter_ids[name])
            widget.unbind('<Leave>', self.bind_leave_ids[name])
        self.widgets.clear()
        self.bind_enter_ids.clear()
        self.bind_leave_ids.clear()

    def remove_tooltip(self, widget):
        """Remove widget from wrapper."""
        try:
            name = str(widget)
            del self.widgets[name]
            widget.unbind('<Enter>', self.bind_enter_ids[name])
            widget.unbind('<Leave>', self.bind_leave_ids[name])
            del self.bind_enter_ids[name]
            del self.bind_leave_ids[name]
        except KeyError:
            pass

    def _on_enter(self, event):
        """Change current widget and launch timer to display tooltip."""
        if not self.tooltip.winfo_ismapped():
            self._timer_id = event.widget.after(self._delay, self.display_tooltip)
            self.current_widget = event.widget

    def _on_leave(self, event):
        """Hide tooltip if visible or cancel tooltip display."""
        if self.tooltip.winfo_ismapped():
            x, y = event.widget.winfo_pointerxy()
            if not event.widget.winfo_containing(x, y) in [event.widget, self.tooltip]:
                self.tooltip.withdraw()
        else:
            try:
                event.widget.after_cancel(self._timer_id)
            except ValueError:
                pass
        self.current_widget = None

    def _on_leave_tooltip(self, event):
        """Hide tooltip."""
        x, y = event.widget.winfo_pointerxy()
        if not event.widget.winfo_containing(x, y) in [self.current_widget, self.tooltip]:
            self.tooltip.withdraw()

    def display_tooltip(self):
        """Display tooltip with text corresponding to current widget."""
        if self.current_widget is None:
            return
        try:
            disabled = "disabled" in self.current_widget.state()
        except AttributeError:
            disabled = self.current_widget.cget('state') == "disabled"

        if not disabled:
            self.tooltip['text'] = self.widgets[str(self.current_widget)]
            self.tooltip.deiconify()
            x = self.current_widget.winfo_pointerx() + 14
            y = self.current_widget.winfo_rooty() + self.current_widget.winfo_height() + 2
            self.tooltip.geometry('+%i+%i' % (x, y))
