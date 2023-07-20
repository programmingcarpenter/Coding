import pytest
from chances import substat

def test_substat():
    assert substat(0) == 0

pytest.main(["-v", "--tb=line", "-rN", __file__])