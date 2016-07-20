##! /usr/bin/env python                             # ------> Shebang

# !!!!!! Note to the user
#    This file provides EXAMPLES of how to do things. Obviously don't import a module or declare variables you have no use for...
#    
#    The  "------->" comments are not to be included in the end file. They're just notes to you as you get started. 
#           Get rid of them once you set up your module (same with the !!!!!!!!!!!!!!!!COMMENTS!!!!!!!!!!!!!!!!!, and this section

__author__     = 'Author Name'                      # ------> Credits
__copyright__  = "CYGNSS - Southwest Research Institute"
__credits__    = ["NA"]
__license__    = "NA"
__version__    = "0.0.1"
__maintainer__ = "Maintainer Name"
__email__      = "my.name@gmail.com"
__status__     = "Dev"

"""
File name: Template.py
Authors:  
Created:  11/3/2014
Modified: 7/24/2015

Description:
    A quick one-line description of this module

    A longer description that goes into more details about how this module works and
    what methods/classes are in it.

Noteworthy Examples:
    # Create a Foo instance
    >>>foo = Foo()
    # Test the Foo instance
    >>>foo.test()

Todos:
    * Make Foo() compatible with python 3.3
    * This one method is clumsily done, rework it

"""

##############################################################################
#                                   Imports
#----------*----------*----------*----------*----------*----------*----------*
###### Standard Modules
import sys                                              # ------> Standard Modules, each imported on their own line
import logging
import os
import logging
from datetime import datetime                           # ------> Some more specialized
import pandas as pd                                     # ------> Explicit naming, avoid namespace collision

##############################################################################
#                             Module-wide Variables
#----------*----------*----------*----------*----------*----------*----------*
# logger         = Utils.getLogger()

##############################################################################
#                                  External Functions
#----------*----------*----------*----------*----------*----------*----------*

def square(x):
    """ Single sentence description: Returns the square of value x
    
    Description: 
        More detailed description of what function does

    Assumptions: 
        If the function assumes things say what that is. May be some high level thing

    Returns:
        The function returns an int or float after squaring it. It could return a tuple, 
        dicitonary, boolean, dataframe, who knows. Maybe it operates on a class instance
        and doesn't return anyhting
    """

    ###### Major sections/divisions for a function have 6 #'s

    #### Semi-major sections/divisons for a function have 2 #'s

    ## Comments prefacing a few lines of code use 2 #'s

    ## Large chunks of expliantion might start with 2 and go to 1 #
    # Wow. These next couple of lines need some preface because they
    # are insanely complicated.

    return x**2 # Quick comments to explain a line go at the end and have 1 #

##############################################################################
#                                  Classes
#----------*----------*----------*----------*----------*----------*----------*
class Foo(object):
    """Here is where the explination and description of a class goes. This class accomplishes a specific task.

    Description:
        Here is more detail on the how it works, and how the task is accomplished
        Run Foo.test() for a verification

    Examples:
        foo = Foo()
        foo.test()
    """

    def __init__(self, theVar):
        """ Initializes this class

        Initialization:
            This describes what happens upon initialization. Lists processes, assumptions, and behavior

        Args:
            theVarNone: A variable that is needed by the class. Can be none.

        Kwargs:

        """
        if theVar is not None:
            self.setTheVar(theVar)

    def setTheVar(self,theVar):
        """This fucntion sets the 'theVar' class variable"""
        self.theVar = theVar
    
    def getTheVar(self):
        """This fucntion gets the 'theVar' class variable"""
        return self.theVar

    def concatThree(self, thingOne, thingTwo="is the best"):
        """It concactenates two things with theVar

        Returns:
            String concactenation foo.theVar, thingsOne, and thingTwo

        Args:
            thingOne: First end of concactenation

        Kwargs:
            thingTwo: Second part of concactenation with default "is the best"

        Examples:
            print(foo.theDemo("Cake ", thingTwo="is the WORST"))
        """
        
        self.theVar =  str(self.theVar) + str(thingOne) + str(thingTwo)

    def isOkay(self):
        """Boolean indicator that this class operates as intended,error free.

        Examples:
            if not foo.isOkay():
                raise Exception("Uh oh! Foo() is broken!)
        """
        try:
            self.test(fullPrintout=False)
            return True
        
        except:
            print(("Automatic %s.test() FAILED" % self.__class__.__name__))
            return False

    def test(self,fullPrintout=True):
        """Test all functionality of this class 

        Kwargs:
            fullPrintout: Boolean indicator that you want to see a printout of each step.

        Examples:
            foo.test()
        """
        ## Test each class and it's functions
        if fullPrintout: print("Auto testing of the Foo() class")
        foo = Foo("Duck") # Also an example of how to use the class

        if fullPrintout: print("Testing the Foo class methods")
        
        ## Testing setTheVar()
        if fullPrintout: print("Testing setTheVar()")
        foo.setTheVar('Cow')    # Set theVar to 'Cow'
        correctAnswer = "Cow"   # Test against known answer

        if not foo.theVar == correctAnswer:
            raise AssertionError("Foo variable theVar was not properly set. Expected [%s], Got [%s]." %(correctAnswer,foo.theVar) )        

        ## Testing getTheVar()
        if fullPrintout: print("Testing getTheVar()"    )
        getTheVarRes = foo.getTheVar()
        
        if not getTheVarRes == correctAnswer:
            raise AssertionError("Foo variable theVar was not properly gotten. Expected [%s], Got [%s]." %(correctAnswer,getTheVarRes) )                

        ## Testing concatThree()
        foo.concatThree(-1,thingTwo='Negative')

        correctAnswer = "Cow-1Negative"
        if not foo.theVar == correctAnswer:
            raise AssertionError("Foo variable theVar was not properly set. Expected [%s], Got [%s]." %(correctAnswer,foo.theVar) )

        return foo # Return the test object if you want play with it in ipython

##############################################################################
#                                 Main
#----------*----------*----------*----------*----------*----------*----------*
def main():
    """This method is meant to self test this module's functionality where appropriate. 

    It is a bug checker/integrity checker to make sure that errors weren't introduced somewhere 
    that could affect higher up functionality"""

    resultsDict     = dict() # dictionary of boolean result returned
    fullPrintout    = False

    ####### Test each class with isOkay
    print("Testing Template module's classes")

    #### Foo Class
    print("Testing Foo class")
    fooInst = Foo(None)
    resultsDict['FooClassResult'] = fooInst.isOkay()
    # fooInst.test() # usually commented out, otherwise reveal testing printouts

    #### Another Class if there was one

    ####### Test the exerior functions not in classes
    #### Testing square() function
    print("Testing square() exterior function")
    result = False
    
    ## Test square() with expected value
    x       = 4
    answer  = 16
    if (square(x) != answer):
        if fullPrintout: print("FAILURE square() failed int test" )
        result = False
    else: 
        if fullPrintout: print("SUCCESS square() passed int test")
        result = True

    resultsDict['squareFuncResult1'] = result # append to results dictionary

    ## Test square() with maybe unexpected zero case
    x       = 0
    answer  = 0
    if square(x) != answer:
        if fullPrintout: print("FAILURE square() failed float test")
        result = False
    else: 
        if fullPrintout: print("SUCCESS square() failed float test")
        result = True

    resultsDict['squareFuncResult2'] = result # append to results dictionary

    #### Would be another Function test

    ###### Return dictionary of test results
    return resultsDict
 
##############################################################################
#                              Runtime Execution
#----------*----------*----------*----------*----------*----------*----------*
if __name__ == "__main__":
    ## Run main function()
    print("Running the Template module")
    results = main()

    ## Return results to overarching tester
    print(results) # Just print(it out here)
