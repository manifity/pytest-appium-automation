import pytest


class TestFirst:

    @pytest.mark.usefixtures
    def test_first(self, appdriver):
        print('First test run')
