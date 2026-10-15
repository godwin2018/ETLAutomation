import pytest
import pytest_check as check

@pytest.fixture(scope="session")
def greetings():
    print(f"Hello - you are using fixtures - before test...\n")
    yield
    print(f"Bye - You are using fixtures - after test...")


