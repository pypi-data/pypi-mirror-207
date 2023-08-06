# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf-8 -*-
#
# Copyright 2002 Ben Escoto <ben@emerose.org>
# Copyright 2007 Kenneth Loafman <kenneth@loafman.com>
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

u"""
Miscellaneous utilities.
"""

from __future__ import print_function

from future import standard_library
standard_library.install_aliases()
from builtins import isinstance
from builtins import map
from builtins import object
from builtins import str

import csv
import errno
import json
import os
import string
import sys
import traceback
import atexit

if sys.version_info.major == 2:
    from cStringIO import StringIO  # pylint: disable=import-error
else:
    from io import StringIO  # pylint: disable=import-error

from duplicity import tarfile
import duplicity.config as config
import duplicity.log as log

try:
    # For paths, just use path.name/uname rather than converting with these
    from os import fsencode, fsdecode  # pylint: disable=unused-import
except ImportError:
    # Most likely Python version < 3.2, so define our own fsencode/fsdecode.
    # These are functions that encode/decode unicode paths to filesystem encoding,
    # but the cleverness is that they handle non-unicode characters on Linux
    # There is a *partial* backport to python available here:
    # https://github.com/pjdelport/backports.os/blob/master/src/backports/os.py
    # but if it cannot be trusted for full-circle translation, then we may as well
    # just read and store the bytes version of the path as path.name before
    # creating the unicode version (for path matching etc) and ensure that in
    # real-world usage (as opposed to testing) we create the path objects from a
    # bytes string.
    # ToDo: Revisit this once we drop Python 2 support/the backport is complete

    def fsencode(unicode_filename):
        u"""Convert a unicode filename to a filename encoded in the system encoding"""
        # For paths, just use path.name rather than converting with this
        # If we are not doing any cleverness with non-unicode filename bytes,
        # encoding to system encoding is good enough
        if sys.version_info[:2] >= (3, 2):
            return os.fsencode(unicode_filename)
        else:
            return unicode_filename.encode(config.fsencoding, u"replace")

    def fsdecode(bytes_filename):
        u"""Convert a filename encoded in the system encoding to unicode"""
        # For paths, just use path.uc_name rather than converting with this
        # If we are not doing any cleverness with non-unicode filename bytes,
        # decoding using system encoding is good enough. Use "ignore" as
        # Linux paths can contain non-Unicode characters
        if sys.version_info[:2] >= (3, 2):
            return os.fsdecode(bytes_filename)
        else:
            return bytes_filename.decode(config.fsencoding, u"replace")


def exception_traceback(limit=50):
    u"""
    @return A string representation in typical Python format of the
            currently active/raised exception.
    """
    type, value, tb = sys.exc_info()  # pylint: disable=redefined-builtin

    lines = traceback.format_tb(tb, limit)
    lines.extend(traceback.format_exception_only(type, value))

    msg = u"Traceback (innermost last):\n"
    if sys.version_info.major >= 3:
        msg = msg + u"%-20s %s" % (str.join(u"", lines[:-1]), lines[-1])
    else:
        msg = msg + u"%-20s %s" % (string.join(lines[:-1], u""), lines[-1])

    if sys.version_info.major < 3:
        return msg.decode(u'unicode-escape', u'replace')
    return msg


def escape(string):
    u"""Convert a (bytes) filename to a format suitable for logging (quoted utf8)"""
    string = fsdecode(string).encode(u'unicode-escape', u'replace')
    return u"'%s'" % string.decode(u'utf8', u'replace').replace(u"'", u'\\x27')


def uindex(index):
    u"""Convert an index (a tuple of path parts) to unicode for printing"""
    if index:
        return os.path.join(*list(map(fsdecode, index)))
    else:
        return u'.'


def uexc(e):
    u"""Returns the exception message in Unicode"""
    # Exceptions in duplicity often have path names in them, which if they are
    # non-ascii will cause a UnicodeDecodeError when implicitly decoding to
    # unicode.  So we decode manually, using the filesystem encoding.
    # 99.99% of the time, this will be a fine encoding to use.
    if e and e.args:
        # Find arg that is a string
        for m in e.args:
            if isinstance(m, str):
                # Already unicode
                return m
            elif isinstance(m, bytes):
                # Encoded, likely in filesystem encoding
                return fsdecode(m)
        # If the function did not return yet, we did not
        # succeed in finding a string; return the whole message.
        # This fails for Python 2, so only do this in Python 3.
        if sys.version_info[0] > 2:
            return str(e)
        # For Python 2, fall back to returning an empty string.
        else:
            return u''
    else:
        return u''


def maybe_ignore_errors(fn):
    u"""
    Execute fn. If the global configuration setting ignore_errors is
    set to True, catch errors and log them but do continue (and return
    None).

    @param fn: A callable.
    @return Whatever fn returns when called, or None if it failed and ignore_errors is true.
    """
    try:
        return fn()
    except Exception as e:
        if config.ignore_errors:
            log.Warn(_(u"IGNORED_ERROR: Warning: ignoring error as requested: %s: %s")
                     % (e.__class__.__name__, uexc(e)))
            return None
        else:
            raise


class BlackHoleList(list):

    def append(self, x):
        pass


class FakeTarFile(object):
    debug = 0

    def __iter__(self):
        return iter([])

    def close(self):
        pass


def make_tarfile(mode, fp):
    # We often use 'empty' tarfiles for signatures that haven't been filled out
    # yet.  So we want to ignore ReadError exceptions, which are used to signal
    # this.
    try:
        tf = tarfile.TarFile(u"arbitrary", mode, fp)
        # Now we cause TarFile to not cache TarInfo objects.  It would end up
        # consuming a lot of memory over the lifetime of our long-lasting
        # signature files otherwise.
        tf.members = BlackHoleList()
        return tf
    except tarfile.ReadError:
        return FakeTarFile()


def get_tarinfo_name(ti):
    # Python versions before 2.6 ensure that directories end with /, but 2.6
    # and later ensure they they *don't* have /.  ::shrug::  Internally, we
    # continue to use pre-2.6 method.
    if ti.isdir() and not ti.name.endswith(r"/"):
        return ti.name + r"/"
    else:
        return ti.name


def ignore_missing(fn, filename):
    u"""
    Execute fn on filename.  Ignore ENOENT errors, otherwise raise exception.

    @param fn: callable
    @param filename: string
    """
    try:
        fn(filename)
    except OSError as ex:
        if ex.errno == errno.ENOENT:
            pass
        else:
            raise


@atexit.register
def release_lockfile():
    if config.lockfile:
        log.Debug(_(u"Releasing lockfile %s") % config.lockpath)
        try:
            config.lockfile.release()
            config.lockfile = None
            os.remove(config.lockpath)
            config.lockpath = u""
        except Exception as e:
            log.Error(u"Could not release lockfile: %s" % str(e))
            pass


def copyfileobj(infp, outfp, byte_count=-1):
    u"""Copy byte_count bytes from infp to outfp, or all if byte_count < 0

    Returns the number of bytes actually written (may be less than
    byte_count if find eof.  Does not close either fileobj.

    """
    blocksize = 64 * 1024
    bytes_written = 0
    if byte_count < 0:
        while 1:
            buf = infp.read(blocksize)
            if not buf:
                break
            bytes_written += len(buf)
            outfp.write(buf)
    else:
        while bytes_written + blocksize <= byte_count:
            buf = infp.read(blocksize)
            if not buf:
                break
            bytes_written += len(buf)
            outfp.write(buf)
        buf = infp.read(byte_count - bytes_written)
        bytes_written += len(buf)
        outfp.write(buf)
    return bytes_written


def which(program):
    u"""
    Return absolute path for program name.
    Returns None if program not found.
    """

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.path.isabs(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.getenv(u"PATH").split(os.pathsep):
            path = path.strip(u'"')
            exe_file = os.path.abspath(os.path.join(path, program))
            if is_exe(exe_file):
                return exe_file

    return None


def start_debugger():
    if u'--pydevd' in sys.argv or os.environ.get(u"PYDEVD", None):
        try:
            import pydevd_pycharm  # pylint: disable=import-error
        except ImportError:
            log.FatalError(u"Module pydevd_pycharm must be available for debugging.\n"
                           u"Remove '--pydevd' from command line and unset 'PYDEVD'\n"
                           u"from the environment to avoid starting the debugger.")

        # NOTE: this needs to be customized for your system
        debug_host = u'dione.local'
        debug_port = 6700

        # get previous pid:port if any
        # return if pid the same as ours
        prev_port = None
        debug_running = os.environ.get(u"DEBUG_RUNNING", False)
        if debug_running:
            prev_pid, prev_port = map(int, debug_running.split(u":"))
            if prev_pid == os.getpid():
                return

        # new pid, next port, start a new debugger
        if prev_port:
            debug_port = int(prev_port) + 1

        # ignition
        try:
            pydevd_pycharm.settrace(debug_host,
                                    port=debug_port,
                                    suspend=False,
                                    stdoutToServer=True,
                                    stderrToServer=True,
                                    # patch_multiprocessing=True,
                                    )
            log.Info(u"Connection {0}:{1} accepted for debug."
                     .format(debug_host, debug_port))
        except ConnectionRefusedError as e:
            log.Info(u"Connection {0}:{1} refused for debug: {2}"
                     .format(debug_host, debug_port, str(e)))

        # in a dev environment the path is screwed so fix it.
        base = sys.path.pop(0)
        base = base.split(os.path.sep)[:-1]
        base = os.path.sep.join(base)
        sys.path.insert(0, base)

        # save last debug pid:port used
        os.environ[u'DEBUG_RUNNING'] = u"{0}:{1}".format(os.getpid(), debug_port)


def merge_dicts(*dict_args):
    u"""
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def csv_args_to_dict(arg):
    u"""
    Given the string arg in single line csv format, split into pairs (key, val)
    and produce a dictionary from those key:val pairs.
    """
    mydict = {}
    with StringIO(arg) as infile:
        rows = csv.reader(infile)
        for row in rows:
            for i in range(0, len(row), 2):
                mydict[row[i]] = row[i + 1]
    return mydict


# TODO: just use util.fsdecode().casefold() directly when python27 is gone
def casefold_compat(s):
    u"""
    Compatability function for casefolding which provides an acceptable for
    older pythons. Can likely be removed once python2 support is no longer o
    any interest.
    """
    if sys.version_info.major >= 3 and sys.version_info.minor >= 3:
        return s.casefold()
    else:
        return s.lower()
