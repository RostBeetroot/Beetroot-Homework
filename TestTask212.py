import os
import pytest
from tempfile import NamedTemporaryFile
from Task21_1 import FileContextManager


# Positive cases

def test_file_context_manager_read():
    content_to_write = "Testing file context manager."
    with NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(content_to_write)

    with FileContextManager(temp_file.name, 'r') as file:
        content = file.read()
        assert content == content_to_write

    os.remove(temp_file.name)


def test_file_context_manager_write():
    content_to_write = "Testing file context manager."
    with FileContextManager("test_file.txt", 'w') as file:
        file.write(content_to_write)

    with open("test_file.txt", 'r') as file:
        content = file.read()
        assert content == content_to_write

    os.remove("test_file.txt")


def test_file_context_manager_append():
    initial_content = "Initial content."
    new_content = " Appended content."
    with NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(initial_content)

    with FileContextManager(temp_file.name, 'a') as file:
        file.write(new_content)

    with open(temp_file.name, 'r') as file:
        content = file.read()
        assert content == initial_content + new_content

    os.remove(temp_file.name)


# Error cases

def test_file_context_manager_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        with FileContextManager("test_file.txt", 'r') as file:
            pass


def test_file_context_manager_runtime_error():
    with pytest.raises(RuntimeError):
        with FileContextManager("test_file.txt", 'w') as file:
            raise RuntimeError("Simulated runtime error")


# Ensure the context manager closes the file even if an exception occurs
def test_file_context_manager_exception_handling():
    with pytest.raises(RuntimeError):
        with FileContextManager("test_file.txt", 'w') as file:
            raise RuntimeError("Simulated runtime error")

    # Check that the file was closed despite the exception
    assert not file.file.closed


# Ensure the counter is correctly incremented and decremented
def test_file_context_manager_counter():
    assert FileContextManager("test_file.txt").counter == 0

    with FileContextManager("test_file.txt", 'r') as file:
        assert FileContextManager("test_file.txt").counter == 1

    assert FileContextManager("test_file.txt").counter == 0
