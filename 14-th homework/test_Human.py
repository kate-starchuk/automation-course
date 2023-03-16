from Human import Human
import pytest


def test_grow():
    human = Human("Alice", 20, "female")
    human.grow()
    assert human.age == 21


def test_grow_util_dead():
    human = Human("Bob", 100, "male")
    human.grow()
    with pytest.raises(Exception, match="Bob is already dead..."):
        human.grow()


def test_change_gender():
    human = Human("Charlie", 30, "male")
    human.change_gender("female")
    assert human.gender == "female"


def test_change_gender_same():
    human = Human("David", 40, "male")
    with pytest.raises(Exception, match="David already has gender 'male'"):
        human.change_gender("male")


def test_change_gender_invalid():
    human = Human("Eve", 50, "female")
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender("other")


def test_gender():
    human = Human("Grace", 70, "female")
    assert human.gender == "female"


def test_age():
    human = Human("Frank", 60, "male")
    assert human.age == 60


