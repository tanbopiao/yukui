"""玉匮（YUKUI）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_seal_verify(self):
        h = self.op.seal({"正本": True})
        self.assertTrue(self.op.verify(h))
        self.assertFalse(self.op.verify("伪纹"))


if __name__ == "__main__":
    unittest.main()
