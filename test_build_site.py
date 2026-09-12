import tempfile
import unittest
from pathlib import Path

from build_site import build


class BuildSiteTests(unittest.TestCase):
    def test_build_creates_hello_world_page(self):
        with tempfile.TemporaryDirectory() as directory:
            output = build(directory)
            html = Path(output).read_text(encoding="utf-8")

        self.assertEqual(output.name, "index.html")
        self.assertIn("Hello, World.", html)
        self.assertIn("Python-powered", html)
        self.assertIn("GitHub Pages", html)


if __name__ == "__main__":
    unittest.main()
