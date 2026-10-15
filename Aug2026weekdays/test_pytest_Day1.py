from tabnanny import check

import pytest
import pytest_check as check
#import pytest_


'''

def test_compare_file_1():
    assert 1==1, "Numbers Not Equal from Test 1"

def compare_file_2():
    assert 1 == 1, "Numbers NOt Equal from Test 2"



# hard assertion

def test_compare_file_hardAssert():
    assert 1==1, "Numbers NOt Equal test 3"
    assert 1 == 2, "Numbers NOt Equal test 4"
    assert 3 == 3, "Numbers NOt Equal test 5"



# soft assertion

def test_compare_file_soft_assert():
    check.equal (1,1, "Numbers NOt Equal test 6")
    check.is_true(3,2, "Numbers NOt Equal test 7")
    check.equal(2,1, "Numbers NOT Equal test 8")
    check.equal( 3, 3, "Numbers NOt Equal test 9")
    check.is_true(3,4, "Numbers NOT Equal test 10")


# without fixtures
name= "Godwin"

def test_welcome_message_1():
    print(f'\n Hello {name}!')
    print("Welcome " + name +" to Python training")
    print(f'Bye {name}!')



def test_welcome_message_2():
    print(f"\n Hello {name}")
    print("you are welcome")
    print("bye")




# write fixtures at test case level of function level
name= "Godwin"
name2 = 'Chika'
name3 = 'Zane'
name4 = 'Zi'
@pytest.fixture(scope="function")
def greetings():
    print(f"Hello {name} - you are using fixtures - before test...\n")
    yield
    print(f"Bye {name} - You are using fixtures - after test...")


def test_welcome_message_3(greetings):
    print("Welcome " + name +" to Python training")


def test_welcome_message_4(greetings):
    print(f"{name}, you are welcome to python training!!!")



# write fixtures at file level of module level
name= "Godwin"
name2 = 'Chika'
name3 = 'Zane'
name4 = 'Zi'
@pytest.fixture(scope="module")
def greetings():
    print(f"Hello {name} - you are using fixtures - before test...\n")
    yield
    print(f"Bye {name} - You are using fixtures - after test...")


def test_welcome_message_5(greetings):
    print("Welcome " + name +" to Python training")


def test_welcome_message_6(greetings):
    print(f"{name}, you are welcome to python training!!!")


'''




# write fixtures at file level of session level
name= "Godwin"

def test_welcome_message_7(greetings):
    print("Welcome " + name +" to Python training")


def test_welcome_message_8(greetings):
    print(f"{name}, you are welcome to python training!!!")

def test_welcome_message_9(greetings):
    print(f"{name}, Python training is getting interesting!!!")
