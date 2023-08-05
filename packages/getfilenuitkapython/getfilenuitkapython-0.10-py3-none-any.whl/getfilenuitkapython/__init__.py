import os
import sys


def get_filepath(filename: str) -> str:
    filepath = os.path.dirname(sys.argv[0])
    fpa = os.path.normpath(os.path.join(filepath, filename))
    if os.path.exists(fpa):
        filepath = fpa
    else:
        filepath = os.path.dirname(__file__)
        fpa = os.path.normpath(os.path.join(filepath, filename))
        if os.path.exists(fpa):
            filepath = fpa

        else:
            filepath = os.sep.join(os.path.dirname(sys.argv[0]).split(os.sep)[:-1])
            fpa = os.path.normpath(os.path.join(filepath, filename))
            if os.path.exists(fpa):
                filepath = fpa
            else:
                filepath = os.sep.join(os.path.dirname(__file__).split(os.sep)[:-1])
                fpa = os.path.normpath(os.path.join(filepath, filename))
                if os.path.exists(fpa):
                    filepath = fpa
                else:
                    fi = sys._getframe(1)
                    dct = fi.f_globals
                    f = dct.get("__file__", "")

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
                            filepath = filename
    return filepath
