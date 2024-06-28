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
## test_utils.py
Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.

Inside test_memoize, define following class

class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()
Use unittest.mock.patch to mock a_method. Test that when calling a_property twice, the correct result is returned but a_method is only called once using assert_called_once.
## test_client.py
Parameterize and patch as decorators
declare the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.

This method should test that GithubOrgClient.org returns the correct value.

Use @patch as a decorator to make sure get_json is called once with the expected argument but make sure it is not executed.

Use @parameterized.expand as a decorator to parametrize the test with a couple of org examples to pass to GithubOrgClient, in this order:

google
abc
Of course, no external HTTP calls should be made.
## test_client.py
Mocking a property
memoize turns methods into properties. Read up on how to mock a property (see resource).

Implement the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.

Use patch as a context manager to patch GithubOrgClient.org and make it return a known payload.

Test that the result of _public_repos_url is the expected one based on the mocked payload.
## test_client.py
More patching
Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.

Use @patch as a decorator to mock get_json and make it return a payload of your choice.

Use patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

Test that the mocked property and the mocked get_json was called once.
