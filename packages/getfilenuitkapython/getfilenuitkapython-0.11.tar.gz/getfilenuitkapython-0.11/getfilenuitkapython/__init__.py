import os
import sys

from list_all_files_recursively import get_folder_file_complete_path
from shlexwhichplus import which_plus


def get_filepath(filename: str) -> str:
    sys_argv = sys.argv.copy()
    fi = sys._getframe(1)
    dct = fi.f_globals
    f = dct.get("__file__", "")
    if os.path.exists(f):
        sys_argv.append(f)
    else:
        sys_argv.append(sys.executable)

    filepath = os.path.dirname(sys_argv[0])

    fpa = os.path.normpath(os.path.join(filepath, filename))
    if os.path.exists(fpa):
        filepath = fpa
    else:
        filepath = os.path.dirname(__file__)
        fpa = os.path.normpath(os.path.join(filepath, filename))
        if os.path.exists(fpa):
            filepath = fpa

        else:
            filepath = os.sep.join(os.path.dirname(sys_argv[0]).split(os.sep)[:-1])
            fpa = os.path.normpath(os.path.join(filepath, filename))
            if os.path.exists(fpa):
                filepath = fpa
            else:
                filepath = os.sep.join(os.path.dirname(__file__).split(os.sep)[:-1])
                fpa = os.path.normpath(os.path.join(filepath, filename))
                if os.path.exists(fpa):
                    filepath = fpa
                else:
                    filepathpu = os.path.dirname(f)
                    fpa = os.path.join(filepathpu, filename)
                    if os.path.exists(fpa):
                        filepath = fpa
                    else:
                        fpa = os.sep.join(
                            os.path.dirname(filepathpu).split(os.sep)[:-1]
                        )
                        fpa = os.path.normpath(os.path.join(fpa, filename))
                        if os.path.exists(fpa):
                            filepath = fpa
                        else:
                            fpa = which_plus(filename, "one")
                            if fpa:
                                if os.path.exists(fpa):
                                    filepath = fpa
                            else:
                                basedir0 = os.path.basename(__file__)
                                basedir1 = os.path.basename(sys_argv[0])
                                basedir2 = os.path.basename(sys.executable)
                                allba = list(set([basedir0, basedir1, basedir2]))

                                loa = filepath.lower()
                                for fa in get_folder_file_complete_path(
                                    allba, maxsubfolders=-1
                                ):
                                    if fa.file.lower() == loa:
                                        filepath = fa.path
                                        break
                                else:
                                    filepath = filename

    return filepath
