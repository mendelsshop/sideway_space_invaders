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
### [Note]: For macOS prebuilt libraries (for each release) to run them it without getting a code signing error.
### Go to System Preferences -> Security & Privacy -> Privacy -> Developer Tools: and add Terminal (or your prefered shell) to the list of
### app that can run software locally that does not meet the system's security policy.
### Another way to do this is go to System Preferences -> Security & Privacy -> General: at the bottom under Allow apps downloaded from: 
### you should see a popup that asks if you binary x to be allowed to run. (I think te popup only shows if you run it and get the error) screenshot exmaples coming soon