import sys
import os
package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
if package_path not in sys.path:
    sys.path.append(package_path)

from dicomviewer import ConsoleViewer
import argparse


def run_standalone():
    """
    Runs when user launches this file in standalone python mode, i.e. from command line.
    """
    parser = argparse.ArgumentParser(description='Display values of DICOM tags inside a directory')
    parser.add_argument('directory')
    parser.add_argument('tags', nargs='+')

    args = parser.parse_args()

    try:
        viewer = ConsoleViewer(args.directory, args.tags)
        viewer.draw_model()
    except AttributeError as e:
        sys.stderr.write(str(e))

    sys.exit(0)


if __name__ == '__main__':
    run_standalone()
