import os
import dicom
from collections import OrderedDict


def browse(directory, select_tags=None):
    """
    Browses a directory and returns list of DICOM files and the values of their tags as a dictionary.

    The dictionary uses same tag names as those used by pydicom library (mind the spacing and capital/lower case).

    :param directory: directory pth where to search for DICOM files.
    :param select_tags: list of DICOM tag names that have to be extracted. Tags outside of this list will be ignored.
    :return: dictionary with DICOM tag values for each DICOM file in directory
    """
    tree = OrderedDict()
    for fname in os.listdir(directory):
        full_fname = os.path.join(directory, fname)
        try:
            tree[full_fname] = read_dicom_file(full_fname, tag_filter=select_tags)

        except dicom.errors.InvalidDicomError:
            pass

        except IsADirectoryError:
            pass

    return tree


# def is_dicom_file(fname):
#     """
#     Returns true if the specified file is a valid DICOM file.
#
#     :param fname: path to file
#     :return: True, if file is a valid DICOM file; False, otherwise.
#     """
#     if not os.path.isfile(fname):
#         return False
#
#     try:
#         dicom.read_file(fname, stop_before_pixels=True)
#
#     except dicom.errors.InvalidDicomError as e:
#         return False
#
#     return True


def read_dicom_file(fname, tag_filter=None):
    """
    Reads a DICOM file and returns a dictionary where keys are DICOM tag names and values are the values of those tags.
    Only tags that are present in the DICOM file, will be present in the generated dictionary.

    :param fname: path to file.
    :param tag_filter: list of DICOM tags whose values need to be read.
    :return: dictionary where keys are tag names, values are tag values.
    """
    tags = {}
    disabled_tags = ['Pixel Data']

    df = dicom.read_file(fname)
    for tag in df:
        if tag_filter is not None:
            if tag.name in tag_filter:
                tags[tag.name] = df[tag.tag].value

        else:
            if tag.name not in disabled_tags:
                tags[tag.name] = df[tag.tag].value

    return tags
