# Deeper Insights Test Code Repo
deeper insights test code

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

**The whole solution was packaged. Although Clare Walsh suggested i leave as it is. I wanted to package the solution. These are the steps I followed to package it into solution.** 

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

    **for some reason I don't know why this prints the result twice**

> I didn't fix the issue of the solution printing the result twice when run from installed package.When run using the script manually it worKs just fine. I have confirmed with the Clare Walsh and she said it is okay if the solution IS to be executed manually using python script
Example :- python solution.py <file_path>. If you run the code directly without the package command line then it works normally.  

Assumptions:
---------------

The user has python 3 and uses linux or windows OS. (I have checked with Clare Walsh and she confirmed this that I can assume the user environment)

The search term is always an alphabetical string. It never has any numbers in it.  As described in the problem statement it is a word. It takes special characters like german umlaut, greek alphabets, and romance language letters. But from my testing experience it doesnt print that result properly in the terminal.

Or the search_term can be dirty and it shall need cleaning before using it as search term. ( I have checked with Clare Walsh and she confirmed this)

This program runs on python3 not python2.7 as it no longer has support. 

File is a text file as this is a basic program that checks for text files. (I have checked with Clare Walsh and she confirmed this)

There are no empty lines between the search term and source text. 

Files will fit into memory. (I have checked with Clare Walsh and she confirmed this)

Also what happens if there are no search terms in source files? Its just means the program can log an error to the user saying "The search_term doesnt exist in the source_text for the file <path_of_file>". 

Originally I wanted to write this is a docker file. But I wasnt sure if this application would be used in cloud or user has docker installed. I confirmed with Clare Walsh that I can put it in readme saying assume user has docker. But I ultimately decided not to do docker container for this application and instead made a pip package. Although the package has a bug, I am more than willing to learn from people on solving the issue. 

