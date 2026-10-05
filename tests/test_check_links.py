import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from urllib.parse import quote


spec = importlib.util.spec_from_file_location(
    "check_links", Path(__file__).resolve().parents[1] / "scripts/check_links.py"
)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class LinkChecks(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def check(self, text, name="README.md"):
        return checker.check_paths([self.write(name, text)])

    def test_regular_relative_link_and_heading(self):
        self.write("articles/note.md", "# A Useful Note\n")
        result = self.check('[note](../articles/note.md#a-useful-note "Read this")', "topics/index.md")
        self.assertEqual(result.issues, [])
        self.assertEqual(result.links, 1)

    def test_encoded_japanese_path_and_explicit_anchor(self):
        path = "資料/日本語 メモ.md"
        anchor = "基本の概念"
        self.write(path, f'<a id="{anchor}"></a>\n')
        result = self.check(f"[note]({quote(path)}#{quote(anchor)})")
        self.assertEqual(result.issues, [])
        self.assertEqual(result.links, 1)

    def test_japanese_heading_slug(self):
        result = self.check("# 日本語の見出し（入門）\n[戻る](#日本語の見出し入門)")
        self.assertEqual(result.issues, [])

    def test_missing_file_with_fragment(self):
        result = self.check("Intro\n[missing](absent.md#detail)")
        self.assertEqual(len(result.issues), 1)
        self.assertEqual(result.issues[0].line, 2)
        self.assertIn("missing Markdown target", result.issues[0].message)

    def test_missing_anchor(self):
        self.write("note.md", '<a id="present"></a>\n')
        result = self.check("[missing](note.md#absent)")
        self.assertEqual(len(result.issues), 1)
        self.assertIn("missing anchor 'absent'", result.issues[0].message)

    def test_explicit_anchor_variants_and_entities(self):
        result = self.check("<A class='target' ID='one&amp;two'></A>\n<a id=plain></a>\n"
                            "[one](#one%26two) [two](#plain)")
        self.assertEqual(result.issues, [])

    def test_duplicate_explicit_anchor(self):
        result = self.check('<a id="same"></a>\n<a id="same"></a>\n')
        self.assertEqual(len(result.issues), 1)
        self.assertEqual(result.issues[0].line, 2)
        self.assertIn("duplicate explicit anchor", result.issues[0].message)

    def test_duplicate_explicit_target_anchor_reported_once(self):
        self.write("note.md", '<a id="same"></a>\n<a id="same"></a>\n')
        result = self.check("[one](note.md#same) [two](note.md#same)")
        self.assertEqual(len(result.issues), 1)
        self.assertEqual(result.issues[0].path.name, "note.md")

    def test_duplicate_headings_use_suffixes(self):
        result = self.check("# Title\n# Title\n# Title\n"
                            "[one](#title) [two](#title-1) [three](#title-2)")
        self.assertEqual(result.issues, [])

    def test_duplicate_heading_suffix_collisions(self):
        result = self.check("# Title\n# Title-1\n# Title\n# Title-1\n"
                            "[one](#title-2) [two](#title-1-1)")
        self.assertEqual(result.issues, [])

    def test_setext_and_formatted_heading(self):
        result = self.check("**Useful** `Code` &amp; _Notes_\n===\n"
                            "[heading](#useful-code--notes)\n"
                            "## hello_world ###\n[underscores](#hello_world)")
        self.assertEqual(result.issues, [])

    def test_fenced_examples_ignored_and_lines_preserved(self):
        result = self.check("````md\n[bad](missing.md)\n```\n<a id='repeat'></a>\n"
                            "<a id='repeat'></a>\n# Hidden\n````\n"
                            "~~~\n[bad](other.md)\n~~~\n[real](absent.md)")
        self.assertEqual(result.links, 1)
        self.assertEqual(len(result.issues), 1)
        self.assertEqual(result.issues[0].line, 11)

    def test_fenced_and_inline_anchors_are_not_real(self):
        result = self.check("```html\n<a id='example'></a>\n# Hidden\n```\n"
                            "`<a id='inline'></a>`\n[one](#example) [two](#hidden) [three](#inline)")
        self.assertEqual(len(result.issues), 3)

    def test_inline_code_and_comments_ignored(self):
        result = self.check("`[bad](missing.md)` ``[bad](other.md)``\n"
                            "<!-- [bad](missing.md) <a id='comment'></a> -->")
        self.assertEqual(result.issues, [])
        self.assertEqual(result.links, 0)

    def test_odd_backslashes_escape_opening_bracket(self):
        for count in (1, 3, 5):
            with self.subTest(backslashes=count):
                result = self.check("\\" * count + "[not a link](missing.md)")
                self.assertEqual(result.issues, [])
                self.assertEqual(result.links, 0)

    def test_even_backslashes_preserve_link(self):
        for count in (0, 2, 4):
            with self.subTest(backslashes=count):
                result = self.check("\\" * count + "[real link](missing.md)")
                self.assertEqual(len(result.issues), 1)
                self.assertEqual(result.links, 1)

    def test_escaped_exclamation_does_not_escape_link_bracket(self):
        result = self.check(r"\![real link](missing.md) !\[not a link](other.md)")
        self.assertEqual(result.links, 1)
        self.assertEqual(len(result.issues), 1)
        self.assertIn("missing.md", result.issues[0].message)

    def test_external_scheme_query_and_asset_links_ignored(self):
        result = self.check("[one](https://example.com/missing.md#absent)\n"
                            "[two](//example.com/missing.md) [three](mailto:hello@example.com)\n"
                            "[four](custom:missing.md) [five](missing.md?raw=1#x)\n"
                            "[six](missing.md?) ![image](missing.png) [empty]()")
        self.assertEqual(result.issues, [])
        self.assertEqual(result.links, 0)

    def test_balanced_parentheses_and_angle_destinations(self):
        self.write("note (v1).md", "# Intro\n")
        result = self.check('[one](note%20(v1).md#intro) [two](<note (v1).md#intro>)')
        self.assertEqual(result.issues, [])
        self.assertEqual(result.links, 2)

    def test_escaped_parentheses(self):
        self.write("note(v1).md", "# Intro\n")
        result = self.check(r"[one](note\(v1\).md#intro)")
        self.assertEqual(result.issues, [])

    def test_reference_definition_destinations(self):
        self.write("note.md", "# Intro\n")
        result = self.check('[read][source]\n[source]: note.md#intro "Title"\n[absent]: absent.md')
        self.assertEqual(result.links, 2)
        self.assertEqual(len(result.issues), 1)
        self.assertEqual(result.issues[0].line, 3)

    def test_target_links_are_not_recursively_checked(self):
        self.write("journals/old.md", "# Intro\n[historical](absent.md)")
        result = self.check("[old](journals/old.md#intro)")
        self.assertEqual(result.issues, [])
        expanded = checker.check_paths([self.root])
        self.assertEqual(len(expanded.issues), 1)
        self.assertIn("absent.md", expanded.issues[0].message)

    def test_default_scope_is_navigation_only(self):
        for name in checker.DEFAULT_FILES:
            self.write(name, "# Index\n")
        self.write("topics/new.md", "# Topic\n")
        self.write("topics/nested/new.md", "# Topic\n")
        self.write("journals/2024/old.md", "[historical](absent.md)")
        sources = checker.default_sources(self.root)
        self.assertEqual(len(sources), 7)
        self.assertEqual(checker.check_paths(sources).issues, [])

    def test_missing_source_is_an_error(self):
        result = checker.check_paths([self.root / "missing.md"])
        self.assertEqual(len(result.issues), 1)
        self.assertIn("cannot read Markdown file", result.issues[0].message)

    def test_root_relative_link_reports_unsupported(self):
        result = self.check("[root](/README.md)")
        self.assertEqual(len(result.issues), 1)
        self.assertIn("unsupported root-relative", result.issues[0].message)

    def test_main_exit_status(self):
        valid = self.write("good.md", "# Good\n[good](#good)")
        invalid = self.write("bad.md", "[missing](absent.md)")
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(checker.main([str(valid)]), 0)
            self.assertEqual(checker.main([str(invalid)]), 1)
        self.assertIn("Checked 1 source files / 1 local Markdown links / 0 errors", output.getvalue())


if __name__ == "__main__":
    unittest.main()
