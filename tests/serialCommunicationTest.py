import sys
sys.path.append("../")
from packages.serialCom import SerialCom

class TestSerialCom:
    def test_one(self):
        x = SerialCom.findCom()
        assert len(x) == 1

    def test_two(self):
        x = SerialCom.findCom()
        assert "COM3" in x