"""玉匮（YUKUI）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from yukui import Yukui


class TestYukui(unittest.TestCase):
    def setUp(self):
        self.op = Yukui()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "yukui")
        self.assertEqual(d["code"], "YUKUI")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_seal_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.seal(None)

    def test_verify_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.verify(None)


if __name__ == "__main__":
    unittest.main()
