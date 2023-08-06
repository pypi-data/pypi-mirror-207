# String Matcher Code Repo

This program lets user pass a textfile path as a arguement to the script.
The script then looks for the search term in the last line of the file and looks for that search item in the other lines of the file. 

Clone this repo first 

**USER HELP** - Use the help function by running -h as an arguement to the program

**DEVELOPER HELP** - Please refer to comments and doc strings in the di_testcode.py file

The file should be a txt file

**USAGE**
    
    pip install -r requirements.txt

    python di_testcode.py <<path of the file>>

**TEST CASE USAGE**

In order to use the test case set the debug parameter in config.yaml to True and add the path directly in the path parameter of config.yaml

    python test.py  

> Please keep in mind to change the test parameter in the config.yaml to False while actually running the app. Its only meant to be True when you are running test cases.


1. create a setup.py with all the requirements in the first directory.
2. added all dependencies to requirements.txt
3. build the package using 

        python setup.py sdist bdist_wheel

4. uploaded the build distribution to Pypi using

        twine upload dist/*

5. This is available on https://pypi.org/project/solution-harsha/ To install this use this command

        pip install solution-harsha

6. To install this package run this command 

        pip install solution_harsha

7. After installing run this command with path to the text file and get result. 

        stringapp_di <<path_of_the_file>>

> I didn't fix the issue of the solution printing the result twice when run from installed package.When run using the script manually it worKs just fine. 
Example :- python solution.py <file_path>. If you run the code directly without the package command line then it works normally
