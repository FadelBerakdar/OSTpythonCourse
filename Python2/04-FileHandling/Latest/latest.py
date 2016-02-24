import os
import glob
import zipfile


def latest(num=1, path="."):
    # a function which returns a list of the most recently modified file(s)

    files = glob.glob(os.path.join(path, "*"))
    dated_files = [(os.path.getmtime(fn), os.path.abspath(fn))
                   for fn in files]
    dated_files.sort()
    latest_files = [f for (d, f) in dated_files[-num:]]
    latest_files.reverse()
    return latest_files


def zip_latest(fn, num, path):

    files_to_archive = latest(num, path)
    zf = zipfile.ZipFile(fn, "w", zipfile.ZIP_DEFLATED)
    for fn_to_archive in files_to_archive:
        zf.write(fn_to_archive)
    zf.close()