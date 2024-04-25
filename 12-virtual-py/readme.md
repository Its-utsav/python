- there is a problem when we install(using `pip install <package_name>`) some packages or modules in python and send that code to other user but that user not install require module , so our progrma create an issue 
- solution is `virtualenv` package

- `pip install virtualenv` it is a python package 

- `virtualenv` give virtual Environment means create a virtual computer (new machine that is differbat from our machine) wih basic installation of python (not a pure virtual enviroment)

- `python -m venv .venv` here .venv is folder name
- best way is thatopen terminal in gitbash and run `source .venv/Scripts/activate` 
- than we can install any module using `pip install <package_Name>` that is differnt from our machine everything install on machine
- how to create a list of package -
1.  `pip list > requirement.txt` -  with specifc version but not too strict 
2. `pip list --format=freeze > requirements.txt` -with specifc version but it is strict 
3. `pip freeze > requirements2.txt` - same as above 

for download from above file 
`pip install -r requirements.txt`


-----------
Deactivate the current virtual environment
`deactivate`
