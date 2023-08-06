# A function that locates files in python environments and compiled exe files (Nuitka)

## [ nuitka ](https://nuitka.net/doc/download.html) is certainly the best py2exe- compiler, but it is not always easy to include additional files. 

The first time I tried that, the compiled EXE wasn't able to find the included files, and it took me some time to make all the necessary code adjustments.  This is why I wrote a little function that locates files in the most likely locations (python env/nuikta exe).

## pip install getfilenuitkapython 

This module contains a function called get_filepath which returns the full path to a file, given its filename. It uses the os and sys modules to search for the file in multiple locations.

```python
Parameters
----------
filename: A string representing the name of the file to locate.

Returns
----------
A string representing the full path to the file, if it is found.
If the file is not found in any of the locations, the function returns the filename itself.

Description
----------
The get_filepath function searches for the file in the following locations:

1. The directory containing the script that was invoked from the command line.
2. The directory containing the current module file (__file__).
3. The parent directory of the directory containing the script that was invoked from the command line.
4. The parent directory of the directory containing the current module file (__file__).
5. The directory containing the calling function (sys._getframe(1)).
6. The parent directory of the directory containing the calling function.
7. Search in PATH
8. Search in every folder in basedirs 

If the file is found in any of these locations, the function returns the full path to the file. If the file is not found in any of these locations, the function returns the filename itself.


from getfilenuitkapython import get_filepath
get_filepath('pythonw.exe')
Out[3]: 'C:\\ProgramData\\anaconda3\\envs\\dfdir\\pythonw.exe'
```