import pytest

from .animals import Cat, Duck, Lion, create_exceptional_leopard


def test_foo():
    pass


@pytest.fixture()
def leopard():
    ...  # setup
    yield None
    create_exceptional_leopard()  # teardown


class TestCats:
    def test_cats_are_cute(self):
        cat = Cat()
        assert cat.is_cute

    def test_lions_are_cats(self):
        lion = Lion()
        assert issubclass(type(lion), Cat)

    # def test_cats_like_water_fail(self):
    #     cat = Cat()
    #     print("cats dont like water? wtf?")
    #     if not cat.likes_water:
    #         # raise ValueError("cats like water, this is a bug")
    #         pytest.fail("cats like water, this is a bug")
    #     # assert cat.likes_water

    # def test_leopard_is_normal_error(self, leopard):
    #     assert leopard is None

    def test_all_cats_are_cute(self):
        # Given, When, Then
        # Given some cats
        cats = [Cat(), Lion()]

        # When we check if they are cute
        is_cute_list = [cat.is_cute for cat in cats]

        # Then they should all be cute
        assert all(is_cute_list)


def test_quack_volume():
    # Arrange
    daffy = Duck()
    quack_volumes = {10: "quack", 40: "Quack", 70: "QUACK", 100: "QUAAAACK!", -5: "..."}

    # Act
    results = {volume: daffy.quack(volume) for volume in quack_volumes.keys()}

    # Assert
    assert results == quack_volumes, "The quack sounds are incorrect."
