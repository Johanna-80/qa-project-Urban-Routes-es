import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    pytest.main(["-v", "tests/test_urban_routes.py"])