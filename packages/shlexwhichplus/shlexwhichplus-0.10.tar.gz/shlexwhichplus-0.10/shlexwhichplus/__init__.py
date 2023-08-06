import os
import sys

def _access_check(fn, mode):
    return (os.path.exists(fn)
            and not os.path.isdir(fn))

def which_plus(cmd, mode='all', path=None):
    """
    Given a command, mode, and a PATH string, return the path which conforms to the given mode on the PATH,
    or None if there is no such file.

    :param cmd: A string specifying the command to be searched.
    :type cmd: str
    :param mode: A string indicating whether to return one or all matches on the PATH.
                 If 'one', return the first match found on the PATH.
                 If 'all', return a list of all matches found on the PATH.
                 If any other string, mode defaults to 'one'.
    :type mode: str
    :param path: A string representing the search path. If None, uses the current system PATH variable.
    :type path: str|None
    :return: If mode is 'one', returns the first path found to the given command, or None if not found.
             If mode is 'all', returns a list of all paths found to the given command, or an empty list if not found.
    :rtype: str or list of str

    """
    # If we're given a path with a directory part, look it up directly rather
    # than referring to PATH directories. This includes checking relative to the
    # current directory, e.g. ./script
    mode = str(mode).lower().strip()
    parseallfiles =  mode == 'all'

    if os.path.dirname(cmd):
        if _access_check(cmd, mode):
            return cmd
        return None

    use_bytes = isinstance(cmd, bytes)

    if path is None:
        path = os.environ.get("PATH", None)
        if path is None:
            try:
                path = os.confstr("CS_PATH")
            except (AttributeError, ValueError):
                # os.confstr() or CS_PATH is not available
                path = os.defpath
        # bpo-35755: Don't use os.defpath if the PATH environment variable is
        # set to an empty string

    # PATH='' doesn't match, whereas PATH=':' looks in the current directory
    if not path:
        return None

    if use_bytes:
        path = os.fsencode(path)
        path = path.split(os.fsencode(os.pathsep))
    else:
        path = os.fsdecode(path)
        path = path.split(os.pathsep)
    twodots = ':'
    if sys.platform == "win32":
        # The current directory takes precedence on Windows.
        curdir = os.curdir
        if use_bytes:
            curdir = os.fsencode(curdir)
        if curdir not in path:
            path.insert(0, curdir)
        try:
            suffi = cmd.split('.')[-1]
        except Exception:
            suffi = cmd.split(b'.')[-1]
        pathext=[suffi]

        if use_bytes:
            pathext = [os.fsencode(ext) for ext in pathext]
            twodots = b':'
        # See if the given file matches any of the expected path extensions.
        # This will allow us to short circuit when given "python.exe".
        # If it does match, only test that one, otherwise we have to try
        # others.
        if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
            files = [cmd]
        else:
            files = [cmd + ext for ext in pathext]
    else:
        # On other platforms you don't have things like PATHEXT to tell you
        # what file suffixes are executable, so just pass on cmd as-is.
        files = [cmd]

    seen = set()
    allfiles =[]
    for dir_ in path:
        normdir = os.path.normcase(dir_)
        if not normdir in seen:
            seen.add(normdir)
            for thefile in files:
                name = os.path.join(dir_, thefile)
                if _access_check(name, mode):

                    thefilel = thefile.lower()
                    for q in os.listdir(dir_):
                        if q.lower() == thefilel:
                            if parseallfiles:
                                newp=os.path.join(dir_, q)
                                if twodots not in newp[:3]:
                                    continue
                                allfiles.append(os.path.normpath(newp))
                            else:
                                return os.path.normpath(os.path.abspath(q))
    if parseallfiles:
        return list(set(allfiles))
    return None

