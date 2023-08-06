import argparse

parser = argparse.ArgumentParser(
                    prog='Pyboil',
                    description='Initialize a basic python wheel package setup via cli script',
                    epilog='Get started fast!')

parser.add_argument(
    '-n', '--name', 
    dest="NAME",
    help="Specifies the name of the package to be initialized.",
    required=True
)

parser.add_argument(
    '-a', '--author',
    dest="AUTHOR",
    help="The author of this package (likely you!).",
    required=True
)

parser.add_argument(
    '-v', '--version',
    dest="VERSION",
    help="Version of the wheel to be placed in setup.py",
    default="0.1.0"
)

parser.add_argument(
    '-d', '--description',
    dest="DESCRIPTION",
    help="A short description of the package's purpose.",
    default="New python package!"
)

parser.add_argument(
    '-e', '--email',
    dest="EMAIL",
    help="email address for inquiries regarding the package.",
    default=""
)

parser.add_argument(
    '-u', '--url',
    dest="URL",
    help="Project website link (Github or Pypi).",
    default=""
)