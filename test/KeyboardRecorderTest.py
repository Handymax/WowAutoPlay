
import unittest
import sys
sys.path.append("..")

from keybdAct import press
from KeyboardRecorder import KeyboardRecorder as kybd


class KeyboardRecordTest(unittest.TestCase):
    def testCanTakeARecorder(self):
        _kybd = kybd()
        _kybd.start()
        self.assertEqual(len(_kybd.script), 4)