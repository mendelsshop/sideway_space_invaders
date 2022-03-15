# How to build the rust keyboard library.
## Step 1 - buid requirements:
You need to have the following installed:
* [Rust](https://www.rust-lang.org/tools/install),
* [setuptools_rust](https://pypi.org/project/setuptools-rust/),
* [Python](https://www.python.org/downloads/) 3.6 or later for now.
## Step 2 - build and install the library:
* Make sure that your in the rust/keyboard directory.
* [Option 1]: Run python setup.py build (or however you run python).
* Move the compilied library (in rust/keyboard/build/lib.your-platform-python-version) into the main directory where main.py is.
* [Option 2]: Run python setup.py install (or however you run python).
### [Note]: Pre-built libraries will be avaliable for each new release.
### [Note]: There is probably a better way to do this, but I don't know it.