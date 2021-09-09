![example workflow](https://github.com/joey-kilgore/python-CI/actions/workflows/python-app.yml/badge.svg)
# python-CI
Test repo for how to setup continuous integration with python unit testing

# How to setup Unit Tests and Continuous Integration
I always create my remote repository first and then clone the empty repostiroy because you will need to setup a remote repository eventually, and doing it later means you have to connect your local repo to the remote one. Starting with a new remote repo and cloning it is the simplest starting point.

Create the python script with the function you want to test. This can be as simple or as complex as you want (see [calculator.py](https://github.com/joey-kilgore/python-CI/blob/main/calculator.py) for the function tested in this repo)

Create the test script which needs to do the following  
- ```import unittest```  
- ```import``` the test functions  
- create a class that extends ```unittest.TestCase```  
- write the test case functions that typically lead to some assert call (like ```self.assertEqual(testResult, expectedResult)```)  
see [testCalculator.py](https://github.com/joey-kilgore/python-CI/blob/main/testCalculator.py) for an example of the test script  

To run the test case  
```python -m unittest <testing script>.py```

To add continuous integration with GitHub Actions  
Go to the actions tab and add a "Python Application" action
At the end of the sample script, add the ```python -m unittest <testing script>.py``` command we used to test the script earlier.  
To see the workflow for this repo checkout [python-app.yml](https://github.com/joey-kilgore/python-CI/blob/main/.github/workflows/python-app.yml)
