import sys

from defcon import Font


def main(argv):
    for ufopath in argv:
        ufo = Font(ufopath)
        ufo.save(ufopath)


if __name__ == "__main__":
    main(sys.argv[1:])
