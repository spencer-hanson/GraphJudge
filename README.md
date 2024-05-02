# GraphJudge
Judge graphs


# USER GUIDE -> \*\*Read-The-Docs!\*\* [LinkToDo]

## DEVELOPMENT - Publishing a new version of this package
- Update the version number in `setup.py` try to use [sem ver](https://semver.org/) as a guide for which number to bump
- Run `build_docs_script.py` to regenerate the autogen docs
- Run `build_package_script.py` to build a new version of the package
- Make sure your `dist/` folder contains only the new version (could fail if not!)
- Run `publish_package.py` to upload the contents to the dist/ folder to pypi
