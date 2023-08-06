import curses


def clicked(cul):
    try:
        _, x, y, _, click_type = curses.getmouse()
    except:
        x = -1
        y = -1
        click_type = -1
        click = "bug"
        cul.screen.addstr(1, 1, "bug detected")

    # the todo list has been clicked
    if cul.conf.todo and x >= cul._xmax:  # MOCHE²
        if not cul._todohl:  # MOCHE
            cul.toggle_TODO()
        if (y-2) in range(len(cul._todo.events)):
            # select a todo, starting on line 2, todohl starts at 1
            cul._todohl = y-2 + 1
            cul.draw_todo()

    elif x <= cul._xoffset:
        # clicked on the hour? Why?
        pass
    else:  # clicked on the main culendar
        if cul._todohl:  # todo list is highlighted
            cul._todohl = 0
            cul.draw_todo()  # not anymore

        # select the current day
        day_lines = cul._lines[0]
        iday = 0
        for i in range(len(day_lines)):
            if x > day_lines[i]:
                iday += 1
        # Monday is 1
        cur_iday = cul.day.isoweekday()
        cul.addday(iday - cur_iday)

        # have we clicked on an event?
        calday = cul._calweek[iday-1]  # MOCHE
        # Monday is 1, first value is 0
        for i, e in enumerate(calday.events):
            if y in e.vlines and x in e.hlines:
                cul._ehl = i  # MOCHE
        cul.draw_day()
