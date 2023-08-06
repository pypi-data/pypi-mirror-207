# pyboil
python package for initializing a python package

## Getting started
for usage information, type
```
pyboil --help

usage: Pyboil [-h] -n NAME -a AUTHOR [-v VERSION] [-d DESCRIPTION] [-e EMAIL] [-u URL]

Initialize a basic python wheel package setup via cli script

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Specifies the name of the package to be initialized.
  -a AUTHOR, --author AUTHOR
                        The author of this package (likely you!).
  -v VERSION, --version VERSION
                        Version of the wheel to be placed in setup.py
  -d DESCRIPTION, --description DESCRIPTION
                        A short description of the package's purpose.
  -e EMAIL, --email EMAIL
                        email address for inquiries regarding the package.
  -u URL, --url URL     Project website link (Github or Pypi).

Get started fast!
```

NAME and AUTHOR are required fields.
VERSION will default to 0.1.0 if not included.
DESCRIPTION will default to "New python package!" if not included.
EMAIL and URL will both default to an empty string ("") if not included.

## Generated tree

for now, this script will generate a specific file structure as shown below
```
{NAME}
  -> __init__.py
build.sh
pyproject.toml
setup.py
```

when you run ./build.sh, it will install the build and twine python module.  The wheel will be built using the 'build' package, and it will be uploaded to Pypi via Twine.  Once you run build.sh, you will eventually be prompted for your Pypi username and password.  Pass this verification and your wheel will be uploaded.  After uploading the wheel, the script deletes all artifacts created locally.

I hope to expand this with more options to include various other build files, such as the MANIFEST.in.  For now, a simple script to quick start projects is all that I needed.