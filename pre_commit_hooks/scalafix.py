from pre_commit_hooks.runner import run_sbt_command
from colorama import init as colorama_init, Fore

TASK_SCALAFMT = '"scalafix RemoveUnused"'
MISSING_PLUGIN_CHECK_STRING = 'Not a valid key: scalafix RemoveUnused'
MISSING_PLUGIN_ERROR_MSG = f'{Fore.RED}ERROR: scalafix SBT plugin not present!'


def main(argv=None):
    colorama_init()

    return run_sbt_command(f'; clean ; {TASK_SCALAFMT}', MISSING_PLUGIN_CHECK_STRING, MISSING_PLUGIN_ERROR_MSG)


if __name__ == '__main__':
    exit(main())
