# ls command in CMD  
This script recreates the functionality of the ls command in Windows' CMD.
You can add colors and extension types. See [termcolor usage](https://pypi.org/project/termcolor/) for options according to your shell.

### Integration steps
- Create venv from requirements.txt with:
 `python -m venv venv && "venv/Scripts/activate.bat" && pip install termcolor`
 
- Run it with: 
`"%directory%/venv/Scripts/python.exe" "%directory%/main.py"` where %directory% should be replaced with full path to repository.
- Make it persistent creating an alias called ls to previous command following this tutorial: https://superuser.com/a/560558