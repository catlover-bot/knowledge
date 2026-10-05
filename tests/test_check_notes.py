import importlib.util
from pathlib import Path
import unittest


spec = importlib.util.spec_from_file_location(
    "check_notes", Path(__file__).resolve().parents[1] / "scripts/check_notes.py"
)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class NoteChecks(unittest.TestCase):
    def check_body(self, body):
        return checker.inspect(f"<details><summary>題名</summary>\n{body}\n</details>")

    def test_markdown_link_only(self):
        self.assertEqual(len(self.check_body("- [参考](https://example.com)")[0]), 1)

    def test_raw_link_only(self):
        self.assertEqual(len(self.check_body("https://example.com")[0]), 1)

    def test_html_image_and_label_only(self):
        self.assertEqual(len(self.check_body('J-STAGE\n<img src="https://example.com/a.png">')[0]), 1)

    def test_reference_link_only(self):
        self.assertEqual(len(self.check_body("[参考][source]\n[source]: https://example.com")[0]), 1)

    def test_substantive_note(self):
        findings, _, entries = self.check_body("- [参考](https://example.com)\n状態をノード間で伝搬する。")
        self.assertEqual(findings, [])
        self.assertEqual(entries, 1)

    def test_pending_source_is_counted(self):
        findings, pending, _ = self.check_body("本文未確認。2026-10-05に取得を試みたが、本文を取得できなかった。")
        self.assertEqual(findings, [])
        self.assertEqual(pending, 1)

    def test_fenced_template_is_ignored(self):
        self.assertEqual(checker.inspect("```md\n<details><summary>例</summary></details>\n```"), ([], 0, 0))

    def test_code_only_research_record_is_content(self):
        findings, _, entries = self.check_body("```python\nprint(1 + 1)\n```")
        self.assertEqual(findings, [])
        self.assertEqual(entries, 1)

    def test_empty_code_block_is_not_content(self):
        self.assertEqual(len(self.check_body("```python\n\n```")[0]), 1)

    def test_pending_title_is_counted(self):
        result = checker.inspect("<details><summary>本文未確認</summary>本文の取得に失敗した。</details>")
        self.assertEqual(result[1], 1)

    def test_index_links_are_ignored(self):
        self.assertEqual(checker.inspect("# 一覧\n[1月](202601.md)"), ([], 0, 0))

    def test_comment_does_not_count_as_prose(self):
        self.assertEqual(len(self.check_body("<!-- 後で書く -->\n[参考](https://example.com)")[0]), 1)


if __name__ == "__main__":
    unittest.main()
