# Deeper Insights Test Code Repo
deeper insights test code

This program lets user pass a textfile path as a arguement to the script.
The script then looks for the search term in the last line of the file and looks for that search item in the other lines of the file.

**USER HELP** - Use the help function by running -h as an arguement to the program

**DEVELOPER HELP** - Please refer to comments and doc strings in the di_testcode.py file

The file should be a txt file

**USAGE**
    
    pip install -r requirements.txt

    python di_testcode.py <<path of the file>>

**TEST CASE USAGE**

In order to use the test case set the debug parameter in config.yaml to True and add the path directly in the path parameter of config.yaml

    python test.py  

The whole solution was packaged. Although Clare Walsh suggested i leave as it is. I wanted to package the solution. These are the steps I followed to package it into solution. 

1. create a setup.py with all the requirements in the first directory.
2. added all dependencies to requirements.txt
3. build the package using 

    python setup.py sdist bdist_wheel

4. uploaded the build distribution to Pypi using

    twine upload dist/*



Assumptions:
The search term is always a alphabetical string. It never has any numbers in it.  As described in the problem statement it is a word. It takes special characters like german umlaut, greek alphabets (I have checked with Clare Walsh and she confirmed this)

Or the search_term can be dirty and it would shall need cleaning before using it as search term. ( I have checked with Clare Walsh and she confirmed this)

This program runs on python3 not python2.7 as it no longer has support. 

File is a text file as this is a basic program that checks for text files. (I have checked with Clare Walsh and she confirmed this)

There are no empty lines between the search term and source text. 

Also what happens if there are no search terms in source files? Its just means the program can return a statement to the user saying "No search_term found in the source_text". The drawback being its going to do it everytime 


