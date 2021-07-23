import sys

from ufoLib2 import Font


def main(argv):
    for ufopath in argv:
        ufo = Font(ufopath)
        ufo.save(ufopath, overwrite=True)


if __name__ == "__main__":
    main(sys.argv[1:])
