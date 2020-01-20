# Unit_Test_ML-DL-AI

## Unit Test for ML & DL

***What is Unit Testing?***

Unit Testing is the first level of software testing where the smallest testable parts of a software are tested. This is used to validate that each unit of the software performs as designed.
The unittest test framework is python’s xUnit style framework.

***Method:***

White Box Testing method is used for Unit testing.

***OOP concepts supported by unittest framework:***

***. test fixture:***

A test fixture is used as a baseline for running tests to ensure that there is a fixed environment in which tests are run so that results are repeatable.

Examples :

creating temporary databases.
starting a server process.

***. test case:***

A test case is a set of conditions which is used to determine whether a system under test works correctly.

***. test suite:***

Test suite is a collection of testcases that are used to test a software program to show that it has some specified set of behaviours by executing the aggregated tests together.

***. test runner:***

A test runner is a component which set up the execution of tests and provides the outcome to the user.

***Basic Test Structure :***

unittest defines tests by the following two ways :

- Manage test “fixtures” using code.
- test itself.

***Running Tests***

if __name__ == '__main__':

   unittest.main()


***Outcomes Possible :***

There are three types of possible test outcomes :

- OK – This means that all the tests are passed.

- FAIL – This means that the test did not pass and an AssertionError exception is raised.

- ERROR – This means that the test raises an exception other than AssertionError.

```Basic terms used in the code :```

***assertEqual()***

This statement is used to check if the result obtained is equal to the expected result.

***assertTrue() / assertFalse() –***

This statement is used to verify if a given statement is true or false.

***assertRaises() –***

This statement is used to raise a specific exception.

Description of tests :

***test_strings_a***

This test is used to test the property of string in which a character say ‘a’ multiplied by a number say ‘x’ gives the output as x times ‘a’. The assertEqual() statement returns true in this case if the result matches the given output.

***test_upper***

This test is used to check if the given string is converted to uppercase or not. The assertEqual() statement returns true if the string returned is in uppercase.

***test_isupper***

This test is used to test the property of string which returns TRUE if the string is in uppercase else returns False. The assertTrue() / assertFalse() statement is used for this verification.

***test_strip***

This test is used to check if all chars passed in the function have been stripped from the string. The assertEqual() statement returns true if the string is stripped and matches the given output.

***test_split***

This test is used to check the split function of the string which splits the string through the argument passed in the function and returns the result as list. The assertEqual() statement returns true in this case if the result matches the given output.

***unittest.main()*** provides a command-line interface to the test script.On running the above script from the command line, following output is produced :

.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
