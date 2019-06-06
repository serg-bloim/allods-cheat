import sys

from aoe2stats import aoe2server
import argparse

from aoe2stats.installer import install

defaultStaticFilesVersion = '0.0.1-rc.2'

def __add_options(parser):
    parser.add_argument('cmd', metavar='CMD', type=str, nargs='?', default='install_run')
    parser.add_argument('--files-version', dest='version', default=defaultStaticFilesVersion)


def run():
    print(sys.argv)
    parser = argparse.ArgumentParser()
    __add_options(parser)
    args = parser.parse_args()
    print(args)
    if args.cmd == 'run':
        aoe2server.startServer()
    elif args.cmd == 'install':
        install(args.version, force=True)
    elif args.cmd == 'install_run':
        install(args.version)
        aoe2server.startServer()

if __name__ == '__main__':
    run()