# Copyright © 2016 Bruce Cowan <bruce@bcowan.eu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import sys

from errbot import BotPlugin, botcmd

PREFIX = "https://github.com/unitycoders/uc_pyircbot/tree/"


class Git(BotPlugin):
    """Git utilities"""

    @staticmethod
    def _get_git_version():
        try:
            cp = subprocess.run(["git", "describe"], stdout=subprocess.PIPE,
                                check=True)
            return str(cp.stdout, sys.stdout.encoding).rstrip()
        except FileNotFoundError:
            return "**Error**: Git is not installed"
        except subprocess.CalledProcessError:
            return "**Error**: No git repository found"
        except UnicodeError:
            return "**Error**: Couldn't convert to string"

    @botcmd
    def git(self, message, args):
        """Gets the git version of the bot"""
        ret = self._get_git_version()
        if ret.startswith("**Error**"):
            return ret
        else:
            return "Git version {}".format(ret)

    @botcmd
    def git_link(self, message, args):
        """Get a link to the source code at github"""
        ret = self._get_git_version()
        if ret.startswith("**Error**"):
            return ret
        else:
            ver = self._get_git_version().split('g')
            if len(ver) == 1:
                link = PREFIX + ver[0]
            else:
                link = PREFIX + ver[1]
            return link
