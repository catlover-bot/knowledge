import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

spec = importlib.util.spec_from_file_location(
    "check_diagrams", Path(__file__).resolve().parents[1] / "scripts/check_diagrams.py"
)
checker = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = checker
spec.loader.exec_module(checker)


class DiagramChecks(unittest.TestCase):
    def inspect(self, body="", attrs='viewBox="0 0 640 800"'):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.svg"
            path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" {attrs}><title>図</title><desc>説明</desc>{body}</svg>')
            return checker.inspect_svg(path)

    def test_self_contained_svg(self):
        self.assertEqual(self.inspect('<path fill="url(#gradient)" d="M0,0 L1,1"/>'), [])

    def test_dimensions_required(self):
        self.assertTrue(self.inspect(attrs=""))

    def test_negative_dimensions(self):
        self.assertTrue(self.inspect(attrs='viewBox="0 0 -1 100"'))

    def test_nonfinite_coordinates_and_dimensions(self):
        for value in ('0 0 nan 100', '0 0 inf 100', 'nan 0 100 100', '0 -inf 100 100'):
            with self.subTest(value=value):
                self.assertTrue(self.inspect(attrs=f'viewBox="{value}"'))

    def test_script_rejected(self):
        self.assertTrue(self.inspect('<script>alert(1)</script>'))

    def test_event_handler_rejected(self):
        self.assertTrue(self.inspect('<rect onclick="click()"/>'))

    def test_remote_resource_rejected(self):
        self.assertTrue(self.inspect('<use href="https://example.com/icon.svg"/>'))

    def test_remote_css_rejected(self):
        self.assertTrue(self.inspect('<style>@import "https://example.com/font.css";</style>'))

    def test_title_and_description_required(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.svg"
            path.write_text('<svg viewBox="0 0 640 800"/>')
            self.assertEqual(len(checker.inspect_svg(path)), 2)

    def test_missing_image_and_alt_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text('![](assets/diagrams/missing.svg)')
            count, errors = checker.inspect_embeds(root)
            self.assertEqual(count, 1)
            self.assertEqual(len(errors), 2)

    def test_external_images_not_fetched(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text('![](https://example.com/a.svg)')
            self.assertEqual(checker.inspect_embeds(root), (0, []))

    def test_fenced_image_example_is_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text('```md\n![](assets/diagrams/missing.svg)\n```')
            self.assertEqual(checker.inspect_embeds(root), (0, []))


if __name__ == "__main__":
    unittest.main()
