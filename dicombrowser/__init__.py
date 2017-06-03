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
    if not os.path.exists(directory):
        raise AttributeError("Directory does not exist.")

    for fname in os.listdir(directory):
        full_fname = os.path.join(directory, fname)
        try:
            tree[full_fname] = read_dicom_file(full_fname, tag_filter=select_tags)

        except dicom.errors.InvalidDicomError:
            pass

        except IsADirectoryError:
            pass

    return tree


def read_dicom_file(fname, tag_filter=None):
    """
    Reads a DICOM file and returns a dictionary where keys are DICOM tag names and values are the values of those tags.
    Only tags that are present in the DICOM file, will be present in the generated dictionary.

    :param fname: path to file.
    :param tag_filter: list of DICOM tags whose values need to be read.
    :return: dictionary where keys are tag names, values are tag values.
    """
    tags = {}
    disabled_tags = ['Pixel Data']  # disable for speed improvement and debugging, TODO: enable in final release

    # check if the DICOM tag names are supported by pydicom
    supported_dicom_tag_names = [item[2] for item in dicom._dicom_dict.DicomDictionary.values()]
    if tag_filter is not None:
        for tag_name in tag_filter:
            if tag_name not in supported_dicom_tag_names:
                raise AttributeError("%s is not a valid DICOM tag name. " \
                                     "Please consult pydicom dictionary for a list of valid names." % tag_name)

    df = dicom.read_file(fname)
    for tag in df:
        if tag_filter is not None:
            if tag.name in tag_filter:
                tags[tag.name] = str(df[tag.tag].value)

        else:
            if tag.name not in disabled_tags:
                tags[tag.name] = str(df[tag.tag].value)

    return tags
