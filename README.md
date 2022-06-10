## Developer guide

Need poetry to for managing dependencies
For installing poetry from `https://python-poetry.org/docs/#installation`

### Steps for setup
1. git clone repo
2. cd to directory Attandance
3. Set python path `poetry env use <python-path>`
4. run the command `poetry install`


### Managing dependencies
#### Add new package
for example `poetry add pandas`

#### Remove package
for example `poetry remove pandas`

#### updating package
for example `poetry update`


### Style and coding guidelines
* Run `black` before commit the code.
    ```
    1. for all file run command in terminal -> "black ."
    2. for specific file run command in terminal -> "black main.py"    
    ```  
* Run `flake8` before commit the code


### Code Profiling
Steps:
  1. Generates .profile 
     `python -m cProfile -o test.profile <*.py>`
  2. Run Snakeviz
     `snakeviz test.profile`


### Running the application
steps:
  1. Initalize Database
      `python .\app\initialiser.py`
  2. Run the server
      `uvicorn app.main:app`
 
