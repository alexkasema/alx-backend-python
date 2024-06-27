# Unittests and Integration Tests
## Unit Testing:
Unit Testing is a type of software testing where individual software components are tested. Unit Testing of the software product is carried out during the development of an application. An individual component may be either an individual function or a procedure. Unit Testing is typically performed by the developer. It is a testing method using which every independent module are tested to determine if there is any issue by the developer himself.

## Integration Testing:
Integration testing is the process of testing the interface between two software units or modules. Its focus is on determining the correctness of the interface. Integration testing aims to expose faults in the interaction between integrated units. Once all the modules have been unit tested, integration testing is performed. 
## test_utils.py
Parameterize a unit test
Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual that the function returns the expected result.
## test_utils.py
Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):

nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
Also make sure that the exception message is as expected.
## test_utils.py
Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.

We don’t want to make any actual external HTTP calls. Use unittest.mock.patch to patch requests.get. Make sure it returns a Mock object with a json method that returns test_payload which you parametrize alongside the test_url that you will pass to get_json with the following inputs:

test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
Test that the mocked get method was called exactly once (per input) with test_url as argument.

Test that the output of get_json is equal to test_payload.
