import os
import dicom


def browse(directory):
    """
    Browses a directory and returns list of DICOM files and the values of their tags as a dictionary.

    :param directory: directory pth where to search for DICOM files.
    :return: dictionary with DICOM tag values for each DICOM file in directory
    """
    tree = {}
    for fname in os.listdir(directory):
        full_fname = os.path.join(directory, fname)
        if is_dicom_file(full_fname):
            tree[full_fname] = ''
    return tree


def is_dicom_file(fname):
    """
    Returns true if the specified file is a valid DICOM file.

    :param fname: path to file
    :return: True, if file is a valid DICOM file; False, otherwise.
    """
    if not os.path.isfile(fname):
        return False

    try:
        dicom.read_file(fname, stop_before_pixels=True)

    except dicom.errors.InvalidDicomError as e:
        return False

    return True
