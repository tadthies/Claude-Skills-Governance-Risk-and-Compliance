"""
test_eval_consistency.py
========================
Validates that per-skill evaluation stats are consistent across all three
locations where they are published:

  1. grc-skills-eval-results.html  — canonical evaluation page (ground truth)
  2. index.html                     — #evaluation tab Per-Skill Results table
  3. README.md                      — #skill-evaluation markdown table

Rules enforced:

  • Every skill in the eval page summary table must appear in index.html and README.md
  • with-skill %, baseline %, and delta % must match exactly across all three files
  • Delta must equal (with% − base%) ± 1 tolerance for rounding
  • Accordion headers in grc-skills-eval-results.html must match the summary table

Background: these three files have diverged in the past when a skill's eval was
re-run (improving results) and only one or two of the three locations was updated.
This test ensures any future update propagates consistently to all locations.

Run with:
    pytest tests/test_eval_consistency.py -v
"""

import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT  = Path(__file__).parent.parent
EVAL_PAGE  = REPO_ROOT / "grc-skills-eval-results.html"
INDEX_HTML = REPO_ROOT / "index.html"
README     = REPO_ROOT / "README.md"

EXPECTED_SKILL_COUNT = 30   # update this constant when a new skill is added


# ---------------------------------------------------------------------------
# Name normalisation
# ---------------------------------------------------------------------------

def _normalize_name(raw: str) -> str:
    """
    Produce a canonical, case-insensitive key for cross-file skill matching.

    Handles:
      • HTML tags  (<img …>, <strong>, etc.)
      • Flag / emoji characters (non-ASCII code points)
      • Bracketed regional / regulatory suffixes ([EU], [US], [Brazil], …)
      • Trailing whitespace from stripping the above
    """
    # 1. Strip HTML tags (img alt text stays inside the tag and is removed too)
    name = re.sub(r"<[^>]+>", "", raw)
    # 2. Remove [bracketed] qualifiers
    name = re.sub(r"\[.*?\]", "", name)
    # 3. Drop all non-ASCII characters (removes emoji, flag sequences, etc.)
    name = "".join(c for c in name if ord(c) < 128)
    # 4. Normalise whitespace
    name = re.sub(r"\s+", " ", name).strip()
    return name.lower()


def _parse_pct(raw: str) -> int:
    """'±0%' / '+4%' / '-4%' / '4%' / '0%'  →  integer."""
    return int(re.sub(r"[+\-±%\s]", "", raw))


# ---------------------------------------------------------------------------
# File parsers
# ---------------------------------------------------------------------------

def _parse_eval_page_summary(content: str) -> dict[str, tuple[int, int, int]]:
    """
    Parse the Per-Skill summary table in grc-skills-eval-results.html.

    Returns {canonical_name: (with_pct, base_pct, delta_pct)}.
    This is the ground truth; all other files are compared against it.
    """
    pattern = re.compile(
        r'class="skill-link">([^<]+)</a></td>\s*'
        r'<td[^>]*>(\d+)%</td>\s*'   # with-skill %
        r'<td[^>]*>(\d+)%</td>\s*'   # baseline %
        r'<td[^>]*>([+\-±]?\d+)%</td>',  # delta %
        re.DOTALL,
    )
    return {
        _normalize_name(m.group(1)): (
            int(m.group(2)),
            int(m.group(3)),
            _parse_pct(m.group(4)),
        )
        for m in pattern.finditer(content)
    }


def _parse_eval_page_accordions(content: str) -> dict[str, tuple[int, int, int]]:
    """
    Parse the accordion toggle-header stats in grc-skills-eval-results.html.

    These should mirror the summary table. Divergence indicates an incomplete
    update (e.g. the accordion header was manually edited but the summary row
    was not, or vice-versa).

    Returns {canonical_name: (with_pct, base_pct, delta_pct)}.
    """
    pattern = re.compile(
        r'<span class="skill-toggle-name">([^<]+)</span>\s*'
        r'<span class="skill-toggle-stats">(\d+)% with skill\s*·\s*(\d+)% baseline\s*·\s*'
        r'<span[^>]*>([+\-±]?\d+)%</span></span>',
        re.DOTALL,
    )
    return {
        _normalize_name(m.group(1)): (
            int(m.group(2)),
            int(m.group(3)),
            _parse_pct(m.group(4)),
        )
        for m in pattern.finditer(content)
    }


def _parse_index_html(content: str) -> dict[str, tuple[int, int, int]]:
    """
    Parse the Per-Skill Results table in the #evaluation section of index.html.

    Each row looks like:
      <tr><td …>N</td><td …>[emoji/img] SKILL NAME [TAG]</td><td>5</td>
          <td><strong>WW%</strong></td><td>BB%</td><td>DD%</td>…</tr>

    Returns {canonical_name: (with_pct, base_pct, delta_pct)}.
    """
    pattern = re.compile(
        r"<tr><td[^>]*>\d+</td>"
        r"<td[^>]*>(.*?)</td>"           # skill name cell (may contain img/emoji)
        r"<td>5</td>"                    # eval count — distinguishes this table
        r"<td><strong>(\d+)%</strong></td>"  # with-skill %
        r"<td>(\d+)%</td>"              # baseline %
        r"<td>([+\-±]?\d+)%</td>",      # delta %
        re.DOTALL,
    )
    return {
        _normalize_name(m.group(1)): (
            int(m.group(2)),
            int(m.group(3)),
            _parse_pct(m.group(4)),
        )
        for m in pattern.finditer(content)
    }


def _parse_readme(content: str) -> dict[str, tuple[int, int, int]]:
    """
    Parse the skill evaluation markdown table in README.md.

    Each row looks like:
      | SKILL NAME [TAG] | 5 | **WW%** | BB% | +DD% | … |

    Note: zero-delta skills may appear as "0%" (no sign), not "+0%".
    The delta sign is therefore optional in the pattern.

    Returns {canonical_name: (with_pct, base_pct, delta_pct)}.
    """
    pattern = re.compile(
        r"^\| ([^|]+?) \| 5 \| \*\*(\d+)%\*\* \| (\d+)% \| ([+\-±]?\d+)% \|",
        re.MULTILINE,
    )
    return {
        _normalize_name(m.group(1)): (
            int(m.group(2)),
            int(m.group(3)),
            _parse_pct(m.group(4)),
        )
        for m in pattern.finditer(content)
    }


# ---------------------------------------------------------------------------
# Lookup helper
# ---------------------------------------------------------------------------

def _best_match(key: str, lookup: dict) -> str | None:
    """
    Exact match only.

    We intentionally avoid substring fallbacks here (e.g. "ism" ⊂ "nzism")
    because skill names normalise cleanly and a substring match would silently
    hide missing entries or, worse, cross-match two different skills.
    """
    return key if key in lookup else None


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def eval_data() -> dict:
    eval_content  = EVAL_PAGE.read_text(encoding="utf-8")
    index_content = INDEX_HTML.read_text(encoding="utf-8")
    readme_content = README.read_text(encoding="utf-8")
    return {
        "eval_summary":    _parse_eval_page_summary(eval_content),
        "eval_accordions": _parse_eval_page_accordions(eval_content),
        "index":           _parse_index_html(index_content),
        "readme":          _parse_readme(readme_content),
    }


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestEvalConsistency:
    """Cross-file consistency of per-skill evaluation statistics."""

    # -- Row counts --------------------------------------------------------

    def test_eval_page_skill_count(self, eval_data):
        """Eval page summary table must have exactly EXPECTED_SKILL_COUNT rows."""
        n = len(eval_data["eval_summary"])
        assert n == EXPECTED_SKILL_COUNT, (
            f"Expected {EXPECTED_SKILL_COUNT} skills in grc-skills-eval-results.html "
            f"summary table, found {n}.\n"
            f"If you added a skill, increment EXPECTED_SKILL_COUNT in this file."
        )

    def test_index_html_skill_count(self, eval_data):
        """index.html Per-Skill Results table must have exactly EXPECTED_SKILL_COUNT rows."""
        n = len(eval_data["index"])
        assert n == EXPECTED_SKILL_COUNT, (
            f"Expected {EXPECTED_SKILL_COUNT} skills in index.html, found {n}.\n"
            f"Skills found: {sorted(eval_data['index'])}"
        )

    def test_readme_skill_count(self, eval_data):
        """README.md skill evaluation table must have exactly EXPECTED_SKILL_COUNT rows."""
        n = len(eval_data["readme"])
        assert n == EXPECTED_SKILL_COUNT, (
            f"Expected {EXPECTED_SKILL_COUNT} skills in README.md, found {n}.\n"
            f"Skills found: {sorted(eval_data['readme'])}"
        )

    # -- Cross-file stat consistency ----------------------------------------

    def test_eval_page_vs_index_html(self, eval_data):
        """
        Every skill's (with%, base%, delta%) in grc-skills-eval-results.html
        must match the corresponding row in index.html.

        Common failure: a skill is re-evaluated and the eval page is updated
        but index.html is not (or vice-versa).
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["eval_summary"].items()):
            match = _best_match(name, eval_data["index"])
            if match is None:
                errors.append(f"  '{name}' not found in index.html Per-Skill table")
                continue
            iw, ib, id_ = eval_data["index"][match]
            if (w, b, d) != (iw, ib, id_):
                errors.append(
                    f"  {name!r}:\n"
                    f"    eval page : {w}% with-skill / {b}% baseline / {d:+}% delta\n"
                    f"    index.html: {iw}% with-skill / {ib}% baseline / {id_:+}% delta"
                )
        assert not errors, (
            "Mismatches between grc-skills-eval-results.html and index.html:\n"
            + "\n".join(errors)
        )

    def test_eval_page_vs_readme(self, eval_data):
        """
        Every skill's (with%, base%, delta%) in grc-skills-eval-results.html
        must match the corresponding row in README.md.

        Common failure: a skill re-run improves results; the eval page and
        index.html are updated but README.md is forgotten.
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["eval_summary"].items()):
            match = _best_match(name, eval_data["readme"])
            if match is None:
                errors.append(f"  '{name}' not found in README.md skill evaluation table")
                continue
            rw, rb, rd = eval_data["readme"][match]
            if (w, b, d) != (rw, rb, rd):
                errors.append(
                    f"  {name!r}:\n"
                    f"    eval page: {w}% with-skill / {b}% baseline / {d:+}% delta\n"
                    f"    README.md: {rw}% with-skill / {rb}% baseline / {rd:+}% delta"
                )
        assert not errors, (
            "Mismatches between grc-skills-eval-results.html and README.md:\n"
            + "\n".join(errors)
        )

    # -- Internal consistency within grc-skills-eval-results.html -----------

    def test_accordion_headers_match_summary_table(self, eval_data):
        """
        For every skill that has an accordion toggle header in
        grc-skills-eval-results.html, the header stats must match
        the summary table for that skill.

        Skills added to the summary table without a corresponding accordion
        section (currently: WCAG, NZISM, VN-PDPL, EU CRA) are skipped —
        they lack accordions because they were added in a later batch that
        didn't include detailed accordion sections. They are listed as a
        non-failing informational note.

        The test FAILS only when an accordion header is present but shows
        different values from the summary table (the bug pattern we've seen:
        an accordion is manually edited for a re-run but the summary row
        is not updated, or vice-versa).
        """
        errors = []
        no_accordion = []
        for name, (w, b, d) in sorted(eval_data["eval_summary"].items()):
            match = _best_match(name, eval_data["eval_accordions"])
            if match is None:
                no_accordion.append(name)
                continue
            aw, ab, ad = eval_data["eval_accordions"][match]
            if (w, b, d) != (aw, ab, ad):
                errors.append(
                    f"  {name!r}:\n"
                    f"    summary table : {w}% with-skill / {b}% baseline / {d:+}% delta\n"
                    f"    accordion hdr : {aw}% with-skill / {ab}% baseline / {ad:+}% delta"
                )
        # Informational: list skills with no accordion section (non-blocking)
        if no_accordion:
            print(
                f"\n[INFO] {len(no_accordion)} skill(s) have no accordion section "
                f"in grc-skills-eval-results.html: {no_accordion}"
            )
        assert not errors, (
            "Accordion headers don't match summary table in grc-skills-eval-results.html:\n"
            + "\n".join(errors)
        )

    # -- Arithmetic sanity (delta = with% − base%) --------------------------

    def test_delta_arithmetic_eval_page(self, eval_data):
        """
        Delta must equal (with% − base%) in grc-skills-eval-results.html.
        Tolerance of ±1 accounts for legitimate percentage rounding.
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["eval_summary"].items()):
            expected = w - b
            if abs(expected - d) > 1:
                errors.append(
                    f"  {name!r}: {w}% − {b}% = {expected:+}% but delta shows {d:+}%"
                )
        assert not errors, (
            "Delta arithmetic errors in grc-skills-eval-results.html:\n"
            + "\n".join(errors)
        )

    def test_delta_arithmetic_index_html(self, eval_data):
        """
        Delta must equal (with% − base%) in index.html.
        Tolerance of ±1 accounts for legitimate percentage rounding.
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["index"].items()):
            expected = w - b
            if abs(expected - d) > 1:
                errors.append(
                    f"  {name!r}: {w}% − {b}% = {expected:+}% but delta shows {d:+}%"
                )
        assert not errors, (
            "Delta arithmetic errors in index.html:\n"
            + "\n".join(errors)
        )

    def test_delta_arithmetic_readme(self, eval_data):
        """
        Delta must equal (with% − base%) in README.md.
        Tolerance of ±1 accounts for legitimate percentage rounding.
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["readme"].items()):
            expected = w - b
            if abs(expected - d) > 1:
                errors.append(
                    f"  {name!r}: {w}% − {b}% = {expected:+}% but delta shows {d:+}%"
                )
        assert not errors, (
            "Delta arithmetic errors in README.md:\n"
            + "\n".join(errors)
        )

    # -- With-skill % ≥ baseline % (a skill should never hurt) ---------------

    def test_with_skill_not_worse_than_baseline(self, eval_data):
        """
        With-skill score must be ≥ baseline for every skill in all three files.
        A negative delta would mean the skill is actively making things worse,
        which warrants immediate investigation.
        """
        errors = []
        for source, data in [
            ("grc-skills-eval-results.html", eval_data["eval_summary"]),
            ("index.html",                   eval_data["index"]),
            ("README.md",                    eval_data["readme"]),
        ]:
            for name, (w, b, _d) in sorted(data.items()):
                if w < b:
                    errors.append(f"  [{source}] {name!r}: {w}% with-skill < {b}% baseline")
        assert not errors, (
            "Skills where with-skill score is LOWER than baseline:\n"
            + "\n".join(errors)
        )
