from main_test import MainTest


class TestMainClassTest:

    def test_get_local_number(self):
        assert MainTest.get_local_number() == 14, "Число != 14"

    def test_get_class_number(self):
        assert MainTest.get_class_number() > 45, "Число < 45"
