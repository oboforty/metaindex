import sys

from cliapp.cli import MetaIndexCommandLineInterface


def main():
    app = MetaIndexCommandLineInterface()

    if len(sys.argv) > 1:
        app.run(sys.argv)
    else:
        app.start()


if __name__ == '__main__':
    main()
