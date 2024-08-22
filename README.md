# API Test Project

This project is designed for testing APIs using Python, `requests`, and `pytest`. It includes a structured setup with `pipenv` for dependency management and centralized fixtures through `conftest.py`.

## Folder Structure

The project is organized as follows:

```plaintext
api-test-project/
├── src/
│   ├── __init__.py             # Initialize the src package
│   └── api_client.py           # API client implementation
├── tests/
│   ├── __init__.py             # Initialize the tests package
│   ├── conftest.py             # Centralized pytest fixtures
│   └── test_api.py             # Test cases for the API client
├── .gitignore                  # Git ignore file to exclude unnecessary files from version control
├── Pipfile                     # Pipenv file specifying project dependencies
├── Pipfile.lock                # Pipenv lock file to ensure deterministic builds
└── README.md                   # Project documentation (this file)
```

## Setup

### Prerequisites
- Python 3.11
- pipenv for managing dependencies

### Installation
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies using pipenv:
    ```bash
    pipenv install
    ```

### Running Tests
To run the tests, execute the following command:
```bash
pipenv run pytest
```

### Test Cases included in this repository
The following table summarizes the test cases included in this project:

| Test Case     | Description   | Expected Result |
| ------------- | ------------- | -------------   |
| GET /facts returns 200  | Verifies the /facts endpoint returns status code 200 OK  | reponse's status code is 200 OK |
| GET /facts returns a non-empty list | Verifies the /facts endpoint returns a JSON list of objects  | response body is instance of List and the size is greater than 0 |
| GET /facts returns the correct data  | It verifies the data the API is returning is correct  | The response parsed as JSON is compared against the expected JSON and they should be equal |
| POST /facts returns 401 Unauthorized  | Verifies that sending a POST to /facts without being authenticated, returns 401  | The response status code is equals to 401 |
| /GET /non-existing-endpoint returns 404  | Verifies that the API server handles correctly unexpected requests to non-existing resources  | The response status code is equals to 404 Not Found |
| GET /users returns 401 | It verifies that sending a reuqest to GET /users returns 401 as it requires authentication as per documentation  | The response status code equals 401 |
