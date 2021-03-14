def f21(lst):
    if 1986 in lst:
        if 'css' in lst:
            if 1987 in lst:
                return 0
            elif 2010 in lst:
                if 'xc' in lst:
                    return 1
                elif 'ninja' in lst:
                    return 2
                elif 'abap' in lst:
                    return 3
            elif 2009 in lst:
                return 4
        elif 'ruby' in lst:
            return 5
        elif 'urweb' in lst:
            if 1958 in lst:
                return 6
            elif 1973 in lst:
                return 7
            elif 1983 in lst:
                return 8
    elif 2009 in lst:
        if 1987 in lst:
            return 9
        elif 2010 in lst:
            return 10
        elif 2009 in lst:
            return 11
    elif 1994 in lst:
        return 12
    return None
print(f21([1994, 1958, 'urweb','xc',1987]))
print(f21([1986, 1983, 'urweb','xc',2010]))



