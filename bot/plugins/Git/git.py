import subprocess
import sys

from errbot import BotPlugin, botcmd


class Git(BotPlugin):
    """
    Git utilities
    """

    @botcmd
    def git(self, message, args):
        """Gets the git version of the bot"""
        try:
            cp = subprocess.run(["git", "describe"], stdout=subprocess.PIPE,
                                check=True)
            version_s = str(cp.stdout, sys.stdout.encoding).rstrip()
            return "Git version {}".format(version_s)
        except FileNotFoundError:
            return "**Error**: Git is not installed"
        except subprocess.CalledProcessError:
            return "**Error**: No git repository found"
        except UnicodeError:
            return "**Error**: Couldn't convert to string"
