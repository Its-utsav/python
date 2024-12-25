- there is a problem when we install third party packages /module ( using `pip install <package_name>`) user / program executer need to install those all packages / module

- solution is `virtualenv` package
- `pip install virtualenv` it is a python package

- `virtualenv` give virtual Environment means create a virtual computer (new machine that is different from our machine) with basic installation of python (not a pure virtual environment)

- `python -m venv .venv` here `.venv` is folder name
- best way is that open terminal in `gitbash` and run `source .venv/Scripts/activate`
- than we can install any module using `pip install <package_Name>` that is different from our machine everything install on machine
- All module / packages install in virtual environment not on direct host machine
- how to create a list of package -

1.  `pip list > requirement.txt` - with specific version but not too strict
2.  `pip list --format=freeze > requirements.txt` -with specific version but it is strict
3.  `pip freeze > requirements2.txt` - same as above

for download from above file
`pip install -r requirements.txt`

---

Deactivate the current virtual environment
`deactivate`
