import argparse
from argparse import RawTextHelpFormatter

from differ import find_matches


parser = argparse.ArgumentParser(
    description="""
Display diff between two lines.
Example:
    old:    "same_prefix_12533_same_suffix"
    new:    "same_prefix23123_same_suffix"
    result: "same_prefix(_)[23]12(53)3_same_suffix"

"()" contains only in old version
"[]" contains only in new version
""", formatter_class=RawTextHelpFormatter)
parser.add_argument('-o', '--old', help='Old version string', required=True)
parser.add_argument('-n', '--new', help='New version string', required=True)

args = parser.parse_args()

if __name__ == "__main__":
    print ''.join(find_matches(args.old, args.new))
