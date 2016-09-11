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
