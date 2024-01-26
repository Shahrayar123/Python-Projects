# -*- coding: utf-8 -*-
"""
tkcalendar - Calendar and DateEntry widgets for Tkinter
Copyright 2017-2019 Juliette Monsel <j_4321@protonmail.com>
with contributions from:
  - Neal Probert (https://github.com/nprobert)
  - arahorn28 (https://github.com/arahorn28)

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


DateEntry widget
"""


from sys import platform
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar.calendar_ import Calendar

# temporary fix for issue #61 and https://bugs.python.org/issue38661
MAPS = {'winnative': {'focusfill': [('readonly', 'focus', 'SystemHighlight')],
                      'foreground': [('disabled', 'SystemGrayText'),
                                     ('readonly', 'focus', 'SystemHighlightText')],
                      'selectforeground': [('!focus', 'SystemWindowText')],
                      'fieldbackground': [('readonly', 'SystemButtonFace'),
                                          ('disabled', 'SystemButtonFace')],
                      'selectbackground': [('!focus', 'SystemWindow')]},
        'clam': {'foreground': [('readonly', 'focus', '#ffffff')],
                 'fieldbackground': [('readonly', 'focus', '#4a6984'), ('readonly', '#dcdad5')],
                 'background': [('active', '#eeebe7'), ('pressed', '#eeebe7')],
                 'arrowcolor': [('disabled', '#999999')]},
        'alt': {'fieldbackground': [('readonly', '#d9d9d9'),
                                    ('disabled', '#d9d9d9')],
                'arrowcolor': [('disabled', '#a3a3a3')]},
        'default': {'fieldbackground': [('readonly', '#d9d9d9'), ('disabled', '#d9d9d9')],
                    'arrowcolor': [('disabled', '#a3a3a3')]},
        'classic': {'fieldbackground': [('readonly', '#d9d9d9'), ('disabled', '#d9d9d9')]},
        'vista': {'focusfill': [('readonly', 'focus', 'SystemHighlight')],
                  'foreground': [('disabled', 'SystemGrayText'),
                                 ('readonly', 'focus', 'SystemHighlightText')],
                  'selectforeground': [('!focus', 'SystemWindowText')],
                  'selectbackground': [('!focus', 'SystemWindow')]},
        'xpnative': {'focusfill': [('readonly', 'focus', 'SystemHighlight')],
                     'foreground': [('disabled', 'SystemGrayText'),
                                    ('readonly', 'focus', 'SystemHighlightText')],
                     'selectforeground': [('!focus', 'SystemWindowText')],
                     'selectbackground': [('!focus', 'SystemWindow')]}}


class DateEntry(ttk.Entry):
    """Date selection entry with drop-down calendar."""

    entry_kw = {'exportselection': 1,
                'invalidcommand': '',
                'justify': 'left',
                'show': '',
                'cursor': 'xterm',
                'style': '',
                'state': 'normal',
                'takefocus': 'ttk::takefocus',
                'textvariable': '',
                'validate': 'none',
                'validatecommand': '',
                'width': 12,
                'xscrollcommand': ''}

    def __init__(self, master=None, **kw):
        """
        Create an entry with a drop-down calendar to select a date.

        When the entry looses focus, if the user input is not a valid date,
        the entry content is reset to the last valid date.

        Keyword Options
        ---------------

        usual ttk.Entry options and Calendar options.
        The Calendar option 'cursor' has been renamed
        'calendar_cursor' to avoid name clashes with the
        corresponding ttk.Entry option.

        Virtual event
        -------------

        A ``<<DateEntrySelected>>`` event is generated each time
        the user selects a date.

        """
        # sort keywords between entry options and calendar options
        kw['selectmode'] = 'day'
        entry_kw = {}

        style = kw.pop('style', 'DateEntry')

        for key in self.entry_kw:
            entry_kw[key] = kw.pop(key, self.entry_kw[key])
        entry_kw['font'] = kw.get('font', None)
        self._cursor = entry_kw['cursor']  # entry cursor
        kw['cursor'] = kw.pop('calendar_cursor', None)

        ttk.Entry.__init__(self, master, **entry_kw)

        self._determine_downarrow_name_after_id = ''

        # drop-down calendar
        self._top_cal = tk.Toplevel(self)
        self._top_cal.withdraw()
        if platform == "linux":
            self._top_cal.attributes('-type', 'DROPDOWN_MENU')
        self._top_cal.overrideredirect(True)
        self._calendar = Calendar(self._top_cal, **kw)
        self._calendar.pack()

        # locale date parsing / formatting
        self.format_date = self._calendar.format_date
        self.parse_date = self._calendar.parse_date

        # style
        self._theme_name = ''   # to detect theme changes
        self.style = ttk.Style(self)
        self._setup_style()
        self.configure(style=style)

        # add validation to Entry so that only dates in the locale's format
        # are accepted
        validatecmd = self.register(self._validate_date)
        self.configure(validate='focusout',
                       validatecommand=validatecmd)

        # initially selected date
        self._date = self._calendar.selection_get()
        if self._date is None:
            today = self._calendar.date.today()
            year = kw.get('year', today.year)
            month = kw.get('month', today.month)
            day = kw.get('day', today.day)
            try:
                self._date = self._calendar.date(year, month, day)
            except ValueError:
                self._date = today
        self._set_text(self.format_date(self._date))

        # --- bindings
        # reconfigure style if theme changed
        self.bind('<<ThemeChanged>>',
                  lambda e: self.after(10, self._on_theme_change))
        # determine new downarrow button bbox
        self.bind('<Configure>', self._determine_downarrow_name)
        self.bind('<Map>', self._determine_downarrow_name)
        # handle appearence to make the entry behave like a Combobox but with
        # a drop-down calendar instead of a drop-down list
        self.bind('<Leave>', lambda e: self.state(['!active']))
        self.bind('<Motion>', self._on_motion)
        self.bind('<ButtonPress-1>', self._on_b1_press)
        # update entry content when date is selected in the Calendar
        self._calendar.bind('<<CalendarSelected>>', self._select)
        # hide calendar if it looses focus
        self._calendar.bind('<FocusOut>', self._on_focus_out_cal)

    def __getitem__(self, key):
        """Return the resource value for a KEY given as string."""
        return self.cget(key)

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def _setup_style(self, event=None):
        """Style configuration to make the DateEntry look like a Combobbox."""
        self.style.layout('DateEntry', self.style.layout('TCombobox'))
        self.update_idletasks()
        conf = self.style.configure('TCombobox')
        if conf:
            self.style.configure('DateEntry', **conf)
        maps = self.style.map('TCombobox')
        if maps:
            try:
                self.style.map('DateEntry', **maps)
            except tk.TclError:
                # temporary fix for issue #61 and https://bugs.python.org/issue38661
                maps = MAPS.get(self.style.theme_use(), MAPS['default'])
                self.style.map('DateEntry', **maps)
        try:
            self.after_cancel(self._determine_downarrow_name_after_id)
        except ValueError:
            # nothing to cancel
            pass
        self._determine_downarrow_name_after_id = self.after(10, self._determine_downarrow_name)

    def _determine_downarrow_name(self, event=None):
        """Determine downarrow button name."""
        try:
            self.after_cancel(self._determine_downarrow_name_after_id)
        except ValueError:
            # nothing to cancel
            pass
        if self.winfo_ismapped():
            self.update_idletasks()
            y = self.winfo_height() // 2
            x = self.winfo_width() - 10
            name = self.identify(x, y)
            if name:
                self._downarrow_name = name
            else:
                self._determine_downarrow_name_after_id = self.after(10, self._determine_downarrow_name)

    def _on_motion(self, event):
        """Set widget state depending on mouse position to mimic Combobox behavior."""
        x, y = event.x, event.y
        if 'disabled' not in self.state():
            if self.identify(x, y) == self._downarrow_name:
                self.state(['active'])
                ttk.Entry.configure(self, cursor='arrow')
            else:
                self.state(['!active'])
                ttk.Entry.configure(self, cursor=self._cursor)

    def _on_theme_change(self):
        theme = self.style.theme_use()
        if self._theme_name != theme:
            # the theme has changed, update the DateEntry style to look like a combobox
            self._theme_name = theme
            self._setup_style()

    def _on_b1_press(self, event):
        """Trigger self.drop_down on downarrow button press and set widget state to ['pressed', 'active']."""
        x, y = event.x, event.y
        if (('disabled' not in self.state()) and self.identify(x, y) == self._downarrow_name):
            self.state(['pressed'])
            self.drop_down()

    def _on_focus_out_cal(self, event):
        """Withdraw drop-down calendar when it looses focus."""
        if self.focus_get() is not None:
            if self.focus_get() == self:
                x, y = event.x, event.y
                if (type(x) != int or type(y) != int or self.identify(x, y) != self._downarrow_name):
                    self._top_cal.withdraw()
                    self.state(['!pressed'])
            else:
                self._top_cal.withdraw()
                self.state(['!pressed'])
        elif self.grab_current():
            # 'active' won't be in state because of the grab
            x, y = self._top_cal.winfo_pointerxy()
            xc = self._top_cal.winfo_rootx()
            yc = self._top_cal.winfo_rooty()
            w = self._top_cal.winfo_width()
            h = self._top_cal.winfo_height()
            if xc <= x <= xc + w and yc <= y <= yc + h:
                # re-focus calendar so that <FocusOut> will be triggered next time
                self._calendar.focus_force()
            else:
                self._top_cal.withdraw()
                self.state(['!pressed'])
        else:
            if 'active' in self.state():
                # re-focus calendar so that <FocusOut> will be triggered next time
                self._calendar.focus_force()
            else:
                self._top_cal.withdraw()
                self.state(['!pressed'])

    def _validate_date(self):
        """Date entry validation: only dates in locale '%x' format are accepted."""
        try:
            date = self.parse_date(self.get())
            self._date = self._calendar.check_date_range(date)
            if self._date != date:
                self._set_text(self.format_date(self._date))
                return False
            else:
                return True
        except (ValueError, IndexError):
            self._set_text(self.format_date(self._date))
            return False

    def _select(self, event=None):
        """Display the selected date in the entry and hide the calendar."""
        date = self._calendar.selection_get()
        if date is not None:
            self._set_text(self.format_date(date))
            self._date = date
            self.event_generate('<<DateEntrySelected>>')
        self._top_cal.withdraw()
        if 'readonly' not in self.state():
            self.focus_set()

    def _set_text(self, txt):
        """Insert text in the entry."""
        if 'readonly' in self.state():
            readonly = True
            self.state(('!readonly',))
        else:
            readonly = False
        self.delete(0, 'end')
        self.insert(0, txt)
        if readonly:
            self.state(('readonly',))

    def destroy(self):
        try:
            self.after_cancel(self._determine_downarrow_name_after_id)
        except ValueError:
            # nothing to cancel
            pass
        ttk.Entry.destroy(self)

    def drop_down(self):
        """Display or withdraw the drop-down calendar depending on its current state."""
        if self._calendar.winfo_ismapped():
            self._top_cal.withdraw()
        else:
            self._validate_date()
            date = self.parse_date(self.get())
            x = self.winfo_rootx()
            y = self.winfo_rooty() + self.winfo_height()
            if self.winfo_toplevel().attributes('-topmost'):
                self._top_cal.attributes('-topmost', True)
            else:
                self._top_cal.attributes('-topmost', False)
            self._top_cal.geometry('+%i+%i' % (x, y))
            self._top_cal.deiconify()
            self._calendar.focus_set()
            self._calendar.selection_set(date)

    def state(self, *args):
        """
        Modify or inquire widget state.

        Widget state is returned if statespec is None, otherwise it is
        set according to the statespec flags and then a new state spec
        is returned indicating which flags were changed. statespec is
        expected to be a sequence.
        """
        if args:
            # change cursor depending on state to mimic Combobox behavior
            states = args[0]
            if 'disabled' in states or 'readonly' in states:
                self.configure(cursor='arrow')
            elif '!disabled' in states or '!readonly' in states:
                self.configure(cursor='xterm')
        return ttk.Entry.state(self, *args)

    def keys(self):
        """Return a list of all resource names of this widget."""
        keys = list(self.entry_kw)
        keys.extend(self._calendar.keys())
        keys.append('calendar_cursor')
        return list(set(keys))

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self.entry_kw:
            return ttk.Entry.cget(self, key)
        elif key == 'calendar_cursor':
            return self._calendar.cget('cursor')
        else:
            return self._calendar.cget(key)

    def configure(self, cnf={}, **kw):
        """
        Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method :meth:`~DateEntry.keys`.
        """
        if not isinstance(cnf, dict):
            raise TypeError("Expected a dictionary or keyword arguments.")
        kwargs = cnf.copy()
        kwargs.update(kw)

        entry_kw = {}
        keys = list(kwargs.keys())
        for key in keys:
            if key in self.entry_kw:
                entry_kw[key] = kwargs.pop(key)
        font = kwargs.get('font', None)
        if font is not None:
            entry_kw['font'] = font
        self._cursor = str(entry_kw.get('cursor', self._cursor))
        if entry_kw.get('state') == 'readonly' and self._cursor == 'xterm' and 'cursor' not in entry_kw:
            entry_kw['cursor'] = 'arrow'
            self._cursor  = 'arrow'
        ttk.Entry.configure(self, entry_kw)

        kwargs['cursor'] = kwargs.pop('calendar_cursor', None)
        self._calendar.configure(kwargs)
        if 'date_pattern' in kwargs or 'locale' in kwargs:
            self._set_text(self.format_date(self._date))

    config = configure

    def set_date(self, date):
        """
        Set the value of the DateEntry to date.

        date can be a datetime.date, a datetime.datetime or a string
        in locale '%x' format.
        """
        try:
            txt = self.format_date(date)
        except AssertionError:
            txt = str(date)
            try:
                self.parse_date(txt)
            except Exception:
                raise ValueError("%r is not a valid date." % date)
        self._set_text(txt)
        self._validate_date()

    def get_date(self):
        """Return the content of the DateEntry as a datetime.date instance."""
        self._validate_date()
        return self.parse_date(self.get())
