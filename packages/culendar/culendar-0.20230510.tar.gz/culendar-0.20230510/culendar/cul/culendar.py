import curses
import datetime
import re

from . import (
    calendar,
    culdav,
    getkey,
    inputs,
)


class Culendar:
    def __init__(self, screen, conf, day, cal, caldav, todo):
        self._screen = screen
        self.conf = conf  # use the specific setter

        self._xoffset = 6  # left offset to draw hours
        self._yoffsettop = 3  # top offset to draw the header
        self._yoffsetbot = 4  # bottom offset to draw the footer

        self._day = day
        self._prevday = datetime.date(1, 1, 1)

        self._cal = cal
        self._caldav = caldav
        self._todo = todo
        # self._calweek is first computed in draw_cal()→draw_week()
        # self._todocol is todowidth in columns, computed in update()

        self._ehl = 0  # highlighted event of current day
        self._prevehl = 0  # idem, previous one
        # highlighted todo, if any, index starts at 1
        self._todohl = 0  # focus on calendar on start
        self._count = 0  # repetitions of the next command
        # compute useful stuff
        self.update()

###############################################################################
#       access and mutate functions
###############################################################################

    @property
    def screen(self):
        return self._screen

    @property
    def conf(self):
        return self._conf

    @conf.setter
    def conf(self, c):
        self._conf = c
        self._hmin = c.hmin
        self._hmax = c.hmax
        self._daynb = 5 + 2*c.WE  # + if WE included

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, d):
        self._prevday = self._day
        self.changehl(-self._ehl)  # resets highlight
        self._day = d

    @property
    def cal(self):
        return self._cal

    @cal.setter
    def cal(self, c):
        self._cal = c

    @property
    def caldav(self):
        return self._caldav

    @property
    def hmin(self):
        return self._hmin

    @property
    def hmax(self):
        return self._hmax

    @property
    def hour_size(self):
        return self._hour_size

    @property
    def ymax(self):
        return self._ymax

    @property
    def lines(self):
        return self._lines

    @property
    def daynb(self):
        return self._daynb

    @property
    def day_size(self):
        return self._day_size

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

###############################################################################
#       update functions
###############################################################################
    def dead_duck(self):
        self.clear_cal()
        text = _("\_x< A dead duck. That's all such a small terminal deserves.")
        self._screen.addstr(0, 0, text[0:(self._width-1)*(self._ymax-1)])

        key = ""
        while key not in self.conf.keys['quit'] and key != 'KEY_RESIZE':
            key = self.getkey()
        if key in self.conf.keys['quit']:
            exit()
        else:
            self.update()

    def update(self):
        self._ymax, self._xmax = self._screen.getmaxyx()
        if self.conf.mouse:  # limit to clickable without bug
            self._xmax = min(self._xmax, 223)

        self._caldav.resize()  # update the ymax and xmax in Caldav
        if self.conf.todo:  # keep space for a todo
            xmax = self._xmax - round(self._xmax*self.conf.todowidth)
            self._day_size = (xmax-self._xoffset) // self._daynb
            # update xmax to be hour place + a multiple of day_size
            xmax = 7 + self._day_size * self._daynb
            self._todocol = self._xmax - xmax
            self._xmax = xmax
        else:
            self._todocol = 0
            self._day_size = (self._xmax-self._xoffset) // self._daynb
        self._width = self._xmax + self._todocol
        self._hour_size = (self._ymax - self._yoffsettop - self._yoffsetbot
                           ) // (self._hmax - self._hmin)
        self.linepos()

        if self.conf._debug:
            self.clear_cal()
            self.draw_cal()
        else:
            try:
                # everything changes, clear screen and redraw stuff
                self.clear_cal()
                self.draw_cal()
            except:
                # culendar couldn't draw it: it's ridiculously small terminal
                self.dead_duck()

    def linepos(self):
        # locations of [day lines, hour lines]
        self._lines = [[], []]

        self._lines[0].append(self._xoffset)
        for id in range(self._daynb-1):
            self._lines[0].append(self._lines[0][id] + self._day_size)
        # the last one is in the last position
        self._lines[0].append(self._xmax-1)

        self._lines[1].append(self._yoffsettop)
        for ih in range(self._hmax-self._hmin):
            self._lines[1].append(self._lines[1][ih] + self._hour_size)

    def toggle_WE(self):
        if self._daynb == 5:
            self._daynb = 7
        elif self._daynb == 7:
            self._daynb = 5
            while self._day.isoweekday() in [6, 7]:
                self._day = datetime.date.fromordinal(
                                self._day.toordinal() - 1)
        self.update()

    def avoid_WE(self, shift):
        if (self._day.isoweekday() in [6, 7]) & (self._daynb == 5):
            while self._day.isoweekday() in [6, 7]:
                if shift > 0:
                    self._day = datetime.date.fromordinal(
                                    self._day.toordinal() + 1)
                else:
                    self._day = datetime.date.fromordinal(
                                    self._day.toordinal() - 1)

    def toggle_TODO(self):
        # if todohl > 1, Todo bar is in highlight mode, remove it
        if self._todohl > 0:
            self.conf.todo = False
            self._todohl = 0
            self.update()  # recompute everything
        elif self.conf.todo:  # Todo bar is unhighlighted
            self._todohl = 1
            self.draw_day()  # remove the day hl
            self.draw_header()  # remove the week hl
            self.draw_hl()  # hl the Todo item
        else:  # make appear the Todo bar
            self.conf.todo = True
            self._todohl = 1
            self.update()  # recompute everything

    def addyear(self, shift):
        try:
            daytmp = self.day.replace(year=self.day.year + shift)
            delta = daytmp - self.day
            self.addday(delta.days)  # use the proper function
        except:     # we can't, that's a daytmp is out of range for month
                    # ie, from 19 February to 31 February
            self.addday(shift*365)  # fallback function

    def addmonth(self, shift):
        newmonth = (self.day.month - 1 + shift) % 12 + 1
        try:
            if abs(self.day.month-newmonth) != abs(shift):  # year changed
                self.addyear(int(shift/abs(shift)))  # sign(shift)
            daytmp = self.day.replace(month=newmonth)
            delta = daytmp - self.day
            self.addday(delta.days)  # use the proper function
        except:  # we can't, that's a day is out of range for month
                 # ie, from 31 January to 31 February
            self.addday(shift*30)  # fallback function

    def addday(self, shift):
        # change day: autoswitch from todo bar if any
        if self._todohl:
            self._todohl = 0
            self.draw_header()  # hl the weekbar
            self.draw_todo()  # un-hl the todo bar
        # set a new day
        self._prevday = self._day
        self._day = datetime.date.fromordinal(self._day.toordinal()+shift)
        self.avoid_WE(shift)
        # new day, new week?
        if self._day.isocalendar()[1] != self._prevday.isocalendar()[1]:
            # if it's a new week, recompute calweek
            self._calweek = calendar.extract_week(self._cal, self._caldav,
                                                  self._day, self,
                                                  self.conf.autosync)
        # update the highlight, which remembers old values of day and ehl
        self.changehl(0)
        # redraw useful stuff
        prevweek = self._prevday.toordinal() - self._prevday.isoweekday()
        curweek = self._day.toordinal() - self._day.isoweekday()
        self.draw_week()

    def changehl(self, inc):
        if self._todohl:  # Todo bar is highlighted
            maxhl = len(self._todo.events)
            self._todohl = (self._todohl + inc) % (maxhl+1)
            if self._todohl == 0:
                self._todohl = 1  # todo hl starts at index 1
        else:
            self._prevehl = self._ehl
            iday = self._day.isoweekday()-1
            maxhl = len(self._calweek[iday].events)
            if maxhl > 0:
                self._ehl = (self._ehl + inc) % maxhl
            else:
                self._ehl = 0

    def sameday(self):
        self._prevday = self._day

    def changeday(self, day=None):
        self.clear_footer()
        if not day:
            day = self.ask_day()
            if day == "CUL_CANCEL":
                return  # cancel the change of day
        if self.daynb == 5:
            while day.isoweekday() in [6, 7]:
                day = datetime.date.fromordinal(day.toordinal() - 1)
        self.day = day
        self.draw_week()

###############################################################################
#       event functions
###############################################################################

    def del_event(self):
        if self._todohl > 0:
            self.del_todo()
            return
        inform = 0
        # select highlighted event if existing
        iday = self._day.isoweekday()-1
        if len(self._calweek[iday].events) > self._ehl:
            event = self._calweek[iday].events[self._ehl]
            # clear the footer event
            self.clear_footer()
            if event.caldav:
                if event.caldav == "webcal":
                    # webcals are read-only
                    msg = _("Error: can't delete webcal event or offline copy")
                    self._screen.addstr(self._ymax-2, 0, msg)
                    self._screen.addstr(self._ymax-1, 0,
                                        _("Press any key to continue"))
                    key = self.getkey()
                    if key == "KEY_RESIZE":
                        self.update()
                    self.clear_footer()
                else:
                    # delete from local cal in order to
                    # avoid syncing caldav to update events
                    # inform when deleting is slow
                    msg = _("Deleting event from ")
                    url = event.caldav.url.url_raw
                    culdav.del_event(event)
                    self._caldav.events.remove(event)
            else:
                # delete it from the cal
                self._cal.del_event(event)
            # update cal of the week
            self._calweek = calendar.extract_week(self._cal, self._caldav,
                                                  self._day, self,
                                                  autosync=0)
            # redraw day without the deleted event
            self.changehl(0)  # to update the highlighted event

            self.draw_day()
            if inform:
                self.inform(msg+event.url)

    def del_todo(self):
        # reminder: todo_hl starts at index 1
        self._todo.del_event(self._todo.events[self._todohl-1])
        self.changehl(0)  # to update the highlighted event
        self.clear_todo()
        self.draw_todo()

    def edit_event(self):
        if self._todohl > 0:
            self.edit_todo()
            return
        # select highlighted event if existing
        iday = self._day.isoweekday()-1
        if len(self._calweek[iday].events) > self._ehl:
            event = self._calweek[iday].events[self._ehl]

            # we can't edit webcal events
            if event.caldav == "webcal":
                # webcals are read-only
                self.clear_footer()
                msg = _("Error: can't delete webcal event")
                self._screen.addstr(self._ymax-2, 0, msg)
                self._screen.addstr(self._ymax-1, 0,
                                    _("Press any key to continue"))
                key = self.getkey()
                if key == "KEY_RESIZE":
                    self.update()
                self.clear_footer()
                return  # exit here

            # the footer will be useful, clear it
            self.clear_footer()
            # ask question
            label = _("Edit: (1) [s]tart time, (2) [e]nd time, (3) [d]escription, (4) [p]lace")
            keys = re.findall('\[(.)\]', label)
            self._screen.addstr(self._ymax-2, 0, label)
            s = self.getkey()
            if s == "KEY_RESIZE":
                self.update()
                return
            self.clear_footer()
            if s in ('1', keys[0]):
                ed = event.date+datetime.timedelta(seconds=event.duration)
                sd = self.ask_starttime()
                if sd == "CUL_CANCEL":
                    return   # cancel edit event
                if sd > ed:  # shift the event to the new starting hour
                    d = event.duration
                else:  # keep the same end hour
                    # recompute duration
                    d = (ed-sd).seconds
                event.date = sd
                event.duration = d
            elif s in ('2', keys[1]):
                ed = self.ask_endtime(event.date)
                if ed == "CUL_CANCEL":
                    return  # cancel edit event
                d = (ed - event.date).seconds
                event.duration = d
            elif s in ('3', keys[2]):
                desc, place = self.ask_description(event)
                if desc == "CUL_CANCEL":
                    return  # canceled edition
                event.summary = desc
                if place:  # non empty
                    event.place = place
            elif s in ('4', keys[3]):
                place = self.ask_place(event)
                if place == "CUL_CANCEL":
                    return  # canceled edition
                event.place = place
            else:
                return

            # sort the events
            self._cal.sort()
            # recompute calweek
            self._calweek = calendar.extract_week(self._cal, self._caldav,
                                                  self._day, self,
                                                  autosync=0)
            if event.caldav:  # update the corresponding caldav
                culdav.del_event(event)
                culdav.add_event(event, event.caldav)
            # redraw full day
            self.draw_day()

    def edit_todo(self):
        # the footer will be useful, clear it
        self.clear_footer()
        if len(self._todo.events) < self._todohl-1:
            return
        todo = self._todo.events[self._todohl-1]
        question = _("Edit: (1) [i]tem, (2) [d]ate, (3) [r]emove date")
        self._screen.addstr(self._ymax-2, 0, question)
        s = self.getkey()
        if s == "KEY_RESIZE":
            self.update()
            return
        if not (s in ['1', '2', '3', 'i', 'd', 'r']):
            self.draw_todo()
            return
        if s in ['1', 'i']:
            item, day = self.ask_todo(todo)
            if day:
                todo.date = day
            todo.summary = item
        if s in ['2', 'd']:
            day = self.ask_day()
            if type(day) == datetime.date:
                todo.date = day
        if s in ['3', 'r']:
            todo.date = None
        self._todo.sort()
        self.clear_todo()
        self.draw_todo()

    def add_event(self):
        # the footer will be useful, clear it
        self.clear_footer()

        if self._todohl > 0:
            self.add_todo()
            return

        sd = self.ask_starttime()
        if sd == "CUL_CANCEL":
            return  # cancel add event
        ed = self.ask_endtime(sd)
        if ed == "CUL_CANCEL":
            return  # cancel add event
        duration = (ed - sd).seconds
        desc, place = self.ask_description()
        if desc == "CUL_CANCEL":
            return  # cancel add event

        # create event
        e = calendar.Event(sd, duration, desc, place)
        self._cal.add_event(e)
        self._cal.sort()
        # recompute calweek
        self._calweek = calendar.extract_week(self._cal, self._caldav,
                                              self._day, self,
                                              autosync=0)
        calday = self._calweek[self._day.isoweekday()-1]

        # determine the ehl to set to hl this event
        self._prevehl = self._ehl
        self._ehl = calday.events.index(e)
        # draw new event
        self.draw_day()

    def add_todo(self):
        summ, date = self.ask_todo()
        if summ == "CUL_CANCEL":
            return  # canceled new item
        item = calendar.Event(date, None, summary=summ, tag=0)
        self._todo.add_event(item)
        self._todo.sort()
        self.clear_todo()
        self.draw_todo()

###############################################################################
#       ask questions
###############################################################################

    def ask_generic(self, question, default=""):
        self.clear_footer()
        self._screen.addstr(self._ymax-2, 0, question[:self._width])
        data = inputs.Input(self._screen, default)
        r = data.get_input()
        while r == -1:
            self.update()  # we got a KEY_RESIZE while getting input
            self.clear_footer()
            self._screen.addstr(self._ymax-2, 0, question[:self._width])
            data.screen_update()
            r = data.get_input()

        self.clear_footer()
        if r == 0:
            return data
        else:  # cancel the question
            return "CUL_CANCEL"

    def ask_starttime(self):
        question = _("Enter start time ([hh:mm], [hhmm], [hh] or [h]):")
        start_time = None
        while start_time is None:
            data = self.ask_generic(question)
            if data != "CUL_CANCEL":
                start_time = data.check_hour(self._day, start=True)
            else:
                data = "CUL_CANCEL"
                start_time = 0
        return self.post_check_input(data, start_time)

    def ask_endtime(self, start_date):
        # ask endtime, return duration of event
        question = (
            _("Enter end time ([hh:mm], [hhmm], [hh] or [h]) or duration ([+mm]):")
        )
        end_date = None
        while end_date is None:
            data = self.ask_generic(question)
            if data != "CUL_CANCEL":
                end_date = data.check_duration(self._day, start_date)
            else:
                data = "CUL_CANCEL"
                end_date = 0
        return self.post_check_input(data, end_date)

    def ask_description(self, event=None):
        question = _("Enter description[@location]:")
        if event:
            data = self.ask_generic(question, event.summary)
        else:
            data = self.ask_generic(question)
        try:
            desc = data.text
        except:
            return "CUL_CANCEL", ""  # empty place
        # is there a location in the description?
        if "@" in desc:
            place = desc[desc.find("@")+1:]
            desc = desc[:desc.find("@")]
        else:
            place = ""
        return desc, place

    def ask_place(self, event):
        question = _("Enter location:")
        data = self.ask_generic(question, event.place)
        try:
            return data.text
        except:
            return "CUL_CANCEL"

    def ask_day(self):
        question = (
            _("Enter day ([yyyy/]mm/dd] or [yyyy]mmdd, [Enter for today]):")
        )
        new_day = None
        while new_day is None:
            data = self.ask_generic(question)
            if data != "CUL_CANCEL":
                new_day = data.check_day(self._day)
            else:
                data = "CUL_CANCEL"
                new_day = 0
        return self.post_check_input(data, new_day)

    def ask_filename(self, mode, question):
        filename = None
        while filename is None:
            data = self.ask_generic(question)
            if data != "CUL_CANCEL":
                filename = data.check_filename(mode)
            else:
                data = "CUL_CANCEL"
                filename = 0
        return self.post_check_input(data, filename)

    def tag_event(self):
        if self._todohl > 0:
            return  # we're in the todolist, nothing to do

        self.clear_footer()
        # select highlighted event if existing
        iday = self._day.isoweekday()-1
        if len(self._calweek[iday].events) > self._ehl:
            event = self._calweek[iday].events[self._ehl]
            # the footer will be useful, clear it
            self.clear_footer()
            # ask question
            self._screen.addstr(self._ymax-2, 0,
                                _("Enter tag number [0-7] or [a-z]:"))
            str_tmp = _("(Current tag: ") + str(event.tag) + ")"
            self._screen.addstr(self._ymax-1, 0, str_tmp)
            prekey = self.getkey()
            if prekey == "KEY_RESIZE":
                self.update()
            key = prekey[0]
            if key.isdigit() and (0 <= int(key) <= 7):  # local event
                event.tag = int(key)
                self.clear_footer()
            elif key.isalpha():  # caldav event
                if key in self._caldav._tags:
                    idx = self._caldav._tags.index(key)
                    caldav = self._caldav._icals[idx]

                    if self._caldav._iscaldav[idx]:  # caldav
                        try:  # remove from local events
                            self._cal.del_event(event)
                        except:  # it's a switch from another caldav
                            # not a local event; duplicate
                            e = calendar.Event(event.date, event.duration,
                                               event.summary, event.place,
                                               event.tag, event.url,
                                               event.caldav, event.colour)
                            event = e
                        # switch from local to caldav local culendars
                        event.tag = key
                        event.colour = self._caldav._list[idx]["colour"]
                        self._caldav._cal.add_event(event)
                        # properly add to the extern caldav
                        culdav.add_event(event, caldav)
                        # inform the switch
                        msg = _("Event moved to ")
                        url = caldav.url.url_raw
                        self.inform(msg+url)
                    else:  # it's a webcal, read-only
                        msg = _("Error: can't add an event to a webcal")
                        self._screen.addstr(self._ymax-2, 0, msg)
                        self._screen.addstr(self._ymax-1, 0,
                                            _("Press any key to continue"))
                        key = self.getkey()
                    if key == "KEY_RESIZE":
                        self.update()
                    self.clear_footer()
                else:
                    errmsg = _(" is not an exisiting calDAV tag")
                    self.inform(key+errmsg)
            else:
                self.clear_footer()
                self.inform(_("Incorrect tag"))
            # redraw with new colour
            self._calweek = calendar.extract_week(self._cal, self._caldav,
                                                  self._day, self,
                                                  autosync=0)
            self.draw_day()

    def copy_event(self, repetitions=1):
        if self._todohl > 0:
            return  # we're in the todolist, nothing to do

        iday = self._day.isoweekday()-1
        if len(self._calweek[iday].events) > self._ehl:
            # only if an event is selected
            if repetitions > 1:
                question = _("Copy to next [d]ays, [w]eeks, [m]onths or [y]ears?")
            else:
                question = _("Copy to next [d]ay, [w]eek, [m]onth or [y]ear?")
            self.inform(question)
            key = self.getkey()
            if key == "KEY_RESIZE":
                self.update()
            if key not in ["d", "D", "w", "W", "m", "M", "y", "Y"]:
                errmsg = _("Invalid answer -- canceled")
                self.inform(errmsg)
                return
            event = self._calweek[iday].events[self._ehl]
            date = event.date
            duration = event.duration
            summary = event.summary
            place = event.place
            tag = event.tag
            colour = event.colour
            for ind in range(repetitions):
                if key in ["d", "D"]:
                    new_date = date + datetime.timedelta(days=(ind+1))
                if key in ["w", "W"]:
                    new_date = date + datetime.timedelta(weeks=(ind+1))
                elif key in ["m", "M"]:
                    years = (date.month + ind)//12
                    month = date.month + ind + 1 - 12*years
                    try:
                        new_date = date.replace(year=date.year+years,
                                                month=month)
                    except:
                        new_date = None
                elif key in ["y", "Y"]:
                    new_date = date.replace(year=date.year+(ind+1))
                if new_date:
                    e = calendar.Event(new_date, duration, summary,
                                       place, tag, colour=colour)
                    # deal with tags
                    if type(tag) == int:  # local event
                        self._cal.add_event(e)
                        msg = _("Event copied")
                    elif tag in self._caldav._tags:  # caldav event
                        idx = self._caldav._tags.index(tag)
                        caldav = self._caldav._icals[idx]
                        if self._caldav._iscaldav[idx]:  # caldav
                            self._caldav._cal.add_event(e)
                            # properly add to the extern caldav
                            culdav.add_event(e, caldav)
                            msg = _("Caldav event remotely copied")
                        else:  # webcal
                            self._cal.add_event(e)
                            msg = _("Webcal event locally copied")
            self._cal.sort()
            if key in ["d", "D"]:
                self.draw_week()  # cause the current week changed
            self.inform(msg)
        # no else: do nothing without an selected event

    def shift_event(self, hours):
        if self._todohl > 0:
            return  # we're in the todolist, nothing to do

        # select highlighted event if existing
        iday = self._day.isoweekday()-1
        if len(self._calweek[iday].events) > self._ehl:
            event = self._calweek[iday].events[self._ehl]

            # we can't edit webcal events
            if event.caldav == "webcal":
                # webcals are read-only
                msg = _("Error: can't change webcal event")
                return  # exit here

            sd = event.date+datetime.timedelta(hours=hours)
            event.date = sd

            if event.caldav:  # update the corresponding caldav
                culdav.del_event(event)
                culdav.add_event(event, event.caldav)

            # give focus to moved event

            # set a new day
            self._prevday = self._day
            self._day = sd.date()
            self.avoid_WE(-1)  # new day a non displayed WE: go on Friday

            # update the days of the current week
            self._calweek = calendar.extract_week(self._cal, self._caldav,
                                                  self._day, self,
                                                  self.conf.autosync)

            # search for the event of the new day to highlight the moved one
            iday = self._day.isoweekday()-1
            for i, e in enumerate(self._calweek[iday].events):
                if e.summary == event.summary and e.place == event.place:
                    self._ehl = i
            self.draw_week()

    def ask_todo(self, todo=None):
        question = _("Enter Todo[@date] ([yyyy/]mm/dd] or [yyyy]mmdd):")
        if todo:
            data = self.ask_generic(question, todo.summary)
        else:
            data = self.ask_generic(question)
        if data == "CUL_CANCEL":
            return "CUL_CANCEL"
        try:
            desc = data.text
            day = None
        except:
            return "CUL_CANCEL", None  # None date
        if "@" in desc:  # is there a date?
            date = desc[desc.find("@")+1:]
            item = desc[:desc.find("@")]
            data.text = date
            day = data.check_day(self._day)
        else:
            item = desc
        if not type(day) == datetime.date:
            day = None
        return item, day

    def post_check_input(self, data, processed_data):
        if (data == "KEY_RESIZE") or (processed_data == "KEY_RESIZE"):
            self.update()
            return "CUL_CANCEL"
        if (data == "CUL_CANCEL") or (processed_data == "CUL_CANCEL"):
            self.clear_footer()
            return "CUL_CANCEL"
        else:
            return processed_data

###############################################################################
#       drawing functions
###############################################################################

    def draw_cal(self):
        if self.conf.mouse:  # limit to clickable without bug
            self.draw_mousedeath()
        self.draw_table()
        self.draw_hours()
        self.draw_week()
        if self.conf.todo:
            self.draw_todo()

    def draw_mousedeath(self):
        ymax, real_xmax = self._screen.getmaxyx()
        if self.conf.todo:
            xmax = self._xmax + self._todocol
        else:
            xmax = self._xmax
        if real_xmax > xmax:
            msg = _(" ☠ DON'T CLICK HERE ☠ ")
            nbmsg = (real_xmax-xmax) // len(msg)
            remain = (real_xmax-xmax) - len(msg)*nbmsg
            msg = msg*nbmsg + msg[:remain]
            for y in range(self._ymax-1):
                self._screen.addstr(y, xmax, msg, curses.A_REVERSE)
            self._screen.addstr(self._ymax-1, xmax, msg[:-1], curses.A_REVERSE)

    def draw_table(self):
        # draw vertical lines to bottom point
        bottom = self._lines[1][-1]-2
        self._screen.vline(2, 0, curses.ACS_VLINE, bottom)
        for ld in self._lines[0]:
            self._screen.vline(2, ld, curses.ACS_VLINE, bottom)

        # draw horizontal lines up to the end
        self._screen.hline(1, 1, curses.ACS_HLINE, self._xmax-2)
        for lh in self._lines[1]:
            self._screen.hline(lh, 1, curses.ACS_HLINE, self._xmax-2)

        for lh in self._lines[1]:
            for ld in self._lines[0]:
                # draw crosses
                self._screen.addch(lh, ld, curses.ACS_PLUS)
            # draw left and right tees
            self._screen.addch(lh, 0, curses.ACS_LTEE)
            self._screen.addch(lh, self._lines[0][-1], curses.ACS_RTEE)

        for ld in self._lines[0]:
            # draw top and bottom tees
            self._screen.addch(1, ld, curses.ACS_TTEE)
            self._screen.addch(self._lines[1][-1], ld, curses.ACS_BTEE)

        # draw corners
        self._screen.addch(1, 0, curses.ACS_ULCORNER)
        self._screen.addch(1, self._lines[0][-1], curses.ACS_URCORNER)
        self._screen.addch(self._lines[1][-1], 0, curses.ACS_LLCORNER)
        self._screen.addch(self._lines[1][-1], self._lines[0][-1],
                           curses.ACS_LRCORNER)

    def draw_hours(self):
        self._screen.addstr(2, 1, _('hours'))
        for i, h in enumerate(range(self._hmin, self._hmax)):
            if h < 10:
                self._screen.addstr(self._lines[1][i], 3, '{}h'.format(h))
            else:
                self._screen.addstr(self._lines[1][i], 2, '{}h'.format(h))

    def draw_header(self):
        # erase previous header
        self._screen.hline(0, 0, " ", self._xmax-1)
        if self._todohl:
            style = curses.A_NORMAL
        else:
            style = curses.A_BOLD
        w = (_(' Week ') + str(self._day.isocalendar()[1]) + ', '
             + self._day.strftime("%B") + ' '
             + str(self._day.isocalendar()[0]))
        self._screen.addstr(0, (self._xmax-len(w))//2+1, w, style)
        self._screen.addstr(0, 0, str(self.conf.keys['help'][0]),
                            curses.A_BOLD)
        self._screen.addstr(0, 1, _(": help"), curses.A_BOLD)

    def draw_footer(self, e):
        enddate = e.date + datetime.timedelta(seconds=e.duration)
        self._screen.addstr(self._ymax-3, 0,
                            _('Begin date: {}').format(e.date))
        self._screen.addstr(self._ymax-2, 0,
                            _('End date:   {}').format(enddate))
        if e.place:
            desc = e.summary + " @ " + e.place
        else:
            desc = e.summary
        text = _('Summary: ') + desc
        self._screen.addstr(self._ymax-1, 0, text[:self._width-1])

    def draw_week(self):
        self.draw_header()
        self.draw_daynames()  # redraw day names
        # extraction of the agenda of all interesting days
        self._calweek = calendar.extract_week(self._cal, self._caldav,
                                              self._day, self,
                                              self.conf.autosync)

        if self.conf._debug:
            for iday in range(self._daynb):
                self.draw_day(iday)
            self.draw_hl()
        else:
            try:
                for iday in range(self._daynb):
                    self.draw_day(iday)
                self.draw_hl()
            except:  # couldn't draw it: too small terminal
                self.dead_duck()

    def draw_day(self, iday=-1, hl=0):
        self.clear_day(iday)

        if iday == -1:  # defaults to current day
            iday = self._day.isoweekday()-1
            hl = 1  # not in draw_week, we'll draw the highlight
        calday = self._calweek[iday]

        for e in calday.events:
            self.draw_event(e, curses.A_NORMAL)
        if hl:
            self.draw_hl()

    def draw_hl(self):
        if self.conf.todo and self._todohl > 0:
            self.draw_todo()  # erase previous hl, draw new one
            return
        # else: normal event hl
        self.clear_hl()
        self.draw_daynames()
        iday = self._day.isoweekday()-1
        maxhl = len(self._calweek[iday].events)
        # is there anything to highlight?
        if (self._ehl < maxhl) & (maxhl > 0):
            self.draw_event(self._calweek[iday].events[self._ehl],
                            curses.A_BOLD)
            self.draw_footer(self._calweek[iday].events[self._ehl])

    def draw_daynames(self):
        # first day is monday = 1
        curday = datetime.date.fromordinal(
                    self._day.toordinal() - self._day.isoweekday() + 1)
        for id in range(self._daynb):
            d = curday.strftime("%a %d/%m")
            pos = self._lines[0][id] + (self._day_size - len(d)) // 2 + 1
            if curday == self._day:
                self._screen.addstr(2, pos, d, curses.A_BOLD)
            else:
                self._screen.addstr(2, pos, d)
            # increment day
            curday = datetime.date.fromordinal(curday.toordinal() + 1)

    def draw_event(self, e, flag):
        # flag is bold if highlighted, normal if not
        try:
            colour = self.conf.colours[e.tag] + curses.A_REVERSE + flag
        except:  # alphabetic tag, that's a caldav, use e.color
            colour = self.conf.colours[e.colour] + curses.A_REVERSE + flag

        normal = curses.A_REVERSE + flag

        if type(e.hlines) == tuple:  # cf calendary.py compute_hlines()
            dduck = [_("\_x<  too   >x_/")[0:e.hlines[1]],
                     _("\_x<  many  >x_/")[0:e.hlines[1]],
                     _("\_x< events >x_/")[0:e.hlines[1]]]
            for iv, v in enumerate(e.vlines):
                self._screen.addstr(v, e.hlines[0], dduck[iv % 3])
            return

        width = len(e.hlines)
        # draw background
        for v in e.vlines:
            if self.conf.colourset == 0:
                self._screen.hline(v, e.hlines[0], " ", width, colour)
            elif self.conf.colourset == 1:
                self._screen.addstr(v, e.hlines[0], " ", colour)
                self._screen.addstr(v, e.hlines[0]+width-1, " ", colour)
                self._screen.hline(v, e.hlines[0]+1, " ", width-2, normal)
            elif self.conf.colourset == 2:
                self._screen.hline(v, e.hlines[0], " ", width, normal)
            else:
                self._screen.hline(v, e.hlines[0], " ", width, normal)

        # prepare the text
        t = e.summary
        if len(t) > (width):
            t = t[0:width]

        # draw text for all cases, bold for highlighted event
        posx = e.hlines[0] + (width - len(t))//2
        posy = e.vlines[0] + (e.vlines[-1]-e.vlines[0])//2
        if self.conf.colourset == 0:
            self._screen.addstr(posy, posx, t, colour)
        elif self.conf.colourset == 1:
            self._screen.addstr(posy, posx, t, normal)
            if len(t) == width:
                self._screen.addstr(posy, posx, t[0], colour)
                self._screen.addstr(posy, posx+width-1, t[-1], colour)
        elif self.conf.colourset == 2:
            self._screen.addstr(posy, posx, t, colour)
        else:
            self._screen.addstr(posy, posx, t, normal)

        # if there is a location, add it if it's a two lines event
        if (e.place != "") & (e.vlines[-1] > e.vlines[0]):
            # prepare the text
            p = e.place
            if len(p) > (width):
                p = p[0:width]
            posx = e.hlines[0] + (width - len(p))//2
            if self.conf.colourset == 0:
                self._screen.addstr(posy+1, posx, p, colour)
            elif self.conf.colourset == 1:
                self._screen.addstr(posy+1, posx, p, normal)
                if len(p) == width:
                    self._screen.addstr(posy+1, posx, p[0], colour)
                    self._screen.addstr(posy+1, posx+width-1, p[-1], colour)
            elif self.conf.colourset == 2:
                self._screen.addstr(posy+1, posx, p, colour)
            else:
                self._screen.addstr(posy+1, posx, p, normal)

    def draw_todo(self):
        if self._todohl:
            style = curses.A_BOLD
        else:
            style = curses.A_NORMAL
        title = _("TODO")
        xpos = self._xmax + (self._todocol-len(title))//2
        self._screen.addch(0, self._xmax-1, curses.ACS_VLINE)
        self._screen.addch(1, self._xmax-1, curses.ACS_PLUS)
        self._screen.addch(self._lines[1][-1], self._xmax-1, curses.ACS_RTEE)
        self._screen.vline(self._lines[1][-1]+1, self._xmax-1,
                           curses.ACS_VLINE, self._ymax-self._lines[1][-1]-4)
        self._screen.hline(1, self._xmax, curses.ACS_HLINE, self._todocol)
        self._screen.addstr(0, xpos, title, style)

        for idx, item in enumerate(self._todo.events):
            if idx+1 == self._todohl:
                style = curses.A_BOLD
            else:
                style = curses.A_NORMAL
            if item.date:
                date = item.date.strftime("%d/%m")
                self._screen.addstr(2+idx, self._xmax+self._todocol-len(date),
                                    date, style)
            if len(item.summary) < self._todocol:
                # + " " to ensure a space before the date
                text = item.summary + " "
            else:
                text = item.summary[:self._todocol-1]
            self._screen.addstr(2+idx, self._xmax+1, text, style)
        if self._todohl > 0 and len(self._todo.events) > 0:
            self.draw_todohl()

    def draw_todohl(self):
        # draw highlighted todo in the footer
        self.clear_footer()
        if len(self._todo.events)+1 > self._todohl:
            item = self._todo.events[self._todohl-1]
            date = ""
            if item.date:
                date = (" -- " + str(item.date.day) + "/"
                               + str(item.date.month) + "/"
                               + str(item.date.year))
            text = item.summary + date
            self._screen.addstr(self._ymax-1, 0, text[:self._width-1])

###############################################################################
#       clearing functions
###############################################################################

    def clear_cal(self):
        self._screen.clear()

    def clear_week(self):
        self.clear_footer()
        # clear the previous week
        prevcalweek = calendar.extract_week(self._cal, self._caldav,
                                            self._prevday, self,
                                            autosync=0)
        for A in prevcalweek[0:self._daynb]:
            for e in A.events:
                self.clear_event(e)

    def clear_day(self, iday=-1):
        if iday == -1:  # defaults to current day
            iday = self._day.isoweekday()-1

        # if last iday, the day size is not self._day_size
        if iday == self.daynb-1:
            width = self.lines[0][-1] - self.lines[0][-2] - 1
        else:
            width = self.day_size - 1
        # day_size - 1: doesn't include vertical separating lines

        for v in range(self.lines[1][0], self.lines[1][-1]+1):
            # +1 to be sure to include last line
            self._screen.hline(v, self.lines[0][iday]+1, " ", width)
            if v in self.lines[1]:
                # if it's a horizontal line, redraw it
                self._screen.hline(v, self.lines[0][iday]+1,
                                   curses.ACS_HLINE, width)

    def clear_event(self, e):
        # draw spaces to erase the background
        width = len(e.hlines)
        for v in e.vlines:
            self._screen.hline(v, e.hlines[0], " ", width)
            if v in self.lines[1]:
                # if it's a horizontal line, redraw it
                self._screen.hline(v, e.hlines[0],
                                   curses.ACS_HLINE, width)

    def clear_hl(self):
        self.clear_footer()
        iday = self._day.isoweekday()-1
        previday = self._prevday.isoweekday()-1
        # we toggled the WE off; nothing to do
        if previday >= self._daynb:
            pass
        # if we change the hl of current day
        elif self._prevday == self._day:
            # just redraw in normal font
            iday = self._day.isoweekday()-1
            maxhl = len(self._calweek[iday].events)
            # is there anything to highlight?
            if (self._prevehl < maxhl) & (maxhl > 0):
                self.draw_event(self._calweek[iday].events[self._prevehl],
                                curses.A_NORMAL)
        # if we change from less than a week
        # same isoweek and same year
        elif self._day.isocalendar()[:2] == self._prevday.isocalendar()[:2]:
            # redraw previous day
            calday = self._calweek[self._prevday.isoweekday()-1]
            for e in calday.events:
                self.draw_event(e, curses.A_NORMAL)
        # else: nothing to do, new week clears everything

    def clear_todo(self):
        for y in range(2, self._ymax):
            self._screen.hline(y, self._xmax, " ", self._todocol)

    def clear_footer(self):
        for y in range(self._ymax-3, self._ymax):
            self._screen.hline(y, 0, " ", self._width)

###############################################################################
# save/import/export
###############################################################################

    def save(self):
        calendar.save(self._cal, self._todo, self._conf, self._caldav)

    def importcal(self):
        question = (
            _("Enter the file name to import (ical or calcurse): (filename [tag])")
        )
        filename = self.ask_filename("rb", question)
        tag = 0  # default value
        if filename == "CUL_CANCEL":
            return
        if ((filename[-2] == " ")
                and (filename[-1] in [str(i) for i in range(8)])):
            tag = int(filename[-1])
            filename = filename[:-2]
        try:  # is it an ical?
            cal = calendar.import_ical(filename, self.conf.categories, tag)
        except:
            try:  # is it from calcurse?
                cal = calendar.import_calcurse(filename, tag)
            except:
                self._screen.addstr(self._ymax-2, 0, _("Unable to load file"))
                self._screen.addstr(self._ymax-1, 0,
                                    _("Press any key to continue"))
                key = self.getkey()
                if key == "KEY_RESIZE":
                    self.update()
                self.clear_footer()
                return

        # check for already present event
        # 1) create simple list from self._cal
        existingevents = []
        for se in self._cal.events:
            existingevents.append(se.date.strftime('%Y%m%d%H%M')
                                  + str(se.duration)
                                  + se.summary.replace(' ', ''))
        for e in cal.events:
            currentevent = (e.date.strftime('%Y%m%d%H%M')
                            + str(e.duration)
                            + e.summary.replace(' ', ''))
            if currentevent not in existingevents:
                self._cal.add_event(e)
        self._cal.sort()
        self.draw_cal()
        self.inform(_("New events imported!"))

    def exportcal(self):
        # returns 1 if successful
        self.clear_footer()
        key = ""
        while key not in ["i", "I", "c", "C", "q", "Q", ""]:
            self._screen.addstr(self._ymax-2, 0,
                                _("Export to [i]cal or to [c]alcurse?"))
            self._screen.addstr(self._ymax-1, 0, "[i/c]")
            key = self.getkey()
            if key == "KEY_RESIZE":
                self.update()
                return
            if key in ["q", "Q", ""]:
                self.clear_footer()
                return
        question = _("Enter the file name to export:")
        filename = self.ask_filename("wb", question)
        if filename == "CUL_CANCEL":
            return

        if key in ["c", "C"]:
            calendar.export_calcurse(self._cal, filename)
        else:
            calendar.export_ical(self._cal, filename, self.conf.categories)
        self.inform(_("Calendar exported!"))

###############################################################################
# other stuff (waiting for a better section name)
###############################################################################

    def getkey(self):
        return getkey.getkey(self._screen, self.conf._debug)

    # use footer to give feedback
    def inform(self, msg):
        self.clear_footer()
        self._screen.addstr(self._ymax-1, 0, msg[0:self._width-1])
        self._screen.refresh()

    def debug(self, elt):
        self._screen.addstr(self._ymax-2, 50,
                            'debug:   {}'.format(elt))
        self._screen.getch()  # just a pause
        self._screen.hline(self._ymax-2, 1, " ", self._width-2)

    def sync_caldav(self):
        # update caldavs only
        self._caldav.sync()
        # redraw if something changed
        self.clear_cal()
        self.draw_cal()
