# Sample programs for chapter 8, input-output

Requirements: Python 3.3+

## Notes:

In the current (python 3.3) edition of the manual, `pipe1.py` and `pipe2.py` used the `platform.popen()`
function to illustrate piping processes between python programs and the operating system. `platform.popen()` 
was deprecated in python 3.3 and was removed from python 3.8+ (which is the version of python that was
used by learners as of December 2024).

Therefore, the two scripts have been rewritten to use the `subprocess.run()` function instead, which is the
recommended method of piping data streams.