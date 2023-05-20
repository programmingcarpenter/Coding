from pytest import approx
import pytest
from water_flow import water_column_height

def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == approx(7.5)
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
