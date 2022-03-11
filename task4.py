# Task 4
# We took a little look on os module. Write a small script which will print
# a string using all the types of string formatting which were considered
# during the lecture with the following context:
# This script has the following PID: <ACTUAL_PID_HERE>. It was ran by <ACTUAL_USERNAME_HERE> to work happily on <ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>.

import os
import platform

actual_pid = os.getpid()
actual_username = os.getlogin()
actual_os_name = os.name
actual_os_release = platform.release()

print("This script has the following PID: {}. It was ran by {} to work happily on {}-{}.".format(actual_pid, actual_username, actual_os_name, actual_os_release))