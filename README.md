# GraphJudge
Judge graphs

```python
    from graph_judge import GraphJudge

    gj = GraphJudge({1, 2, 3, 4})
    gj.add_judge("is_even", lambda x: (x % 2 == 0))
    gj.add_judge("is_one", lambda x: x == 1)

    results = gj.run_chain_and(["is_even", "is_one"])
    evens = results.filter("is_even", True).members()
    one = results.filter("is_one", True).members()
    odd = results.filter("is_even", False).filter("is_one", False).members()

    assert evens == [2, 4]
    assert odd == [3]
    assert one == [1]
```

# USER GUIDE -> \*\*Read-The-Docs!\*\* [LinkToDo]

## DEVELOPMENT - Publishing a new version of this package
- Update the version number in `setup.py` try to use [sem ver](https://semver.org/) as a guide for which number to bump
- Run `build_docs_script.py` to regenerate the autogen docs
- Run `build_package_script.py` to build a new version of the package
- Make sure your `dist/` folder contains only the new version (could fail if not!)
- Run `publish_package.py` to upload the contents to the dist/ folder to pypi
