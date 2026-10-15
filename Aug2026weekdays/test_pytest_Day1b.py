from tabnanny import check

import pytest
import pytest_check as check
#import pytest_


# write fixtures at session level
name= "Godwin"
name2 = 'Chika'
name3 = 'Zane'
name4 = 'Ziv'



def test_welcome_message_10(greetings):
    print("Welcome " + name +" to Python training")


def test_welcome_message_11(greetings):
    print(f"{name}, you are welcome to python training!!!")


def test_welcome_message_12(greetings):
    print(f"{name2}, Python training is getting interesting!!!")


def test_welcome_message_13(greetings):
    print(f"{name3}, you are welcome to python training!!!")


def test_welcome_message_14(greetings):
    print(f"{name4}, Python training is getting interesting!!!")
