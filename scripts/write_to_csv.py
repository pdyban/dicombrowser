import sys
import os
package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
if package_path not in sys.path:
    sys.path.append(package_path)
from dicomviewer import CSVViewer
import argparse


def run_standalone():
    """
    Runs when user launches this file in standalone python mode, i.e. from command line.
    """
    parser = argparse.ArgumentParser(description='Writes values of DICOM tags inside a directory to a CSV file')
    parser.add_argument('out', metavar='O')
    parser.add_argument('directory')
    parser.add_argument('tags', nargs='+')

    args = parser.parse_args()

    try:
        with open(args.out, 'w') as f:
            viewer = CSVViewer(f, args.directory, args.tags)
            viewer.draw()

    except AttributeError as e:
        sys.stderr.write(str(e))

    sys.exit(0)


if __name__ == '__main__':
    run_standalone()
