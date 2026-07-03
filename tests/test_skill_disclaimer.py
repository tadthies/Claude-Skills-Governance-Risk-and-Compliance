"""
test_skill_disclaimer.py
========================
Every SKILL.md must carry the standard not-legal-advice disclaimer.

Skills are installed standalone (as .skill archives), detached from the
repository README and its disclaimer section — so the disclaimer has to
travel inside each skill.

Run with:
    pytest tests/test_skill_disclaimer.py -v
"""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent

CANONICAL_PHRASE = (
    "not legal advice. Verify current requirements against official sources"
)


def _skill_files():
    return sorted(REPO_ROOT.glob("plugins/*/skills/*/SKILL.md"))


@pytest.mark.parametrize("skill_md", _skill_files(), ids=lambda p: p.parent.name)
def test_disclaimer_present(skill_md: Path):
    assert CANONICAL_PHRASE in skill_md.read_text(), (
        f"{skill_md.parent.name}: standard disclaimer missing. Append:\n"
        "> *This skill provides general compliance information, not legal "
        "advice. Verify current requirements against official sources; "
        "consult qualified counsel or an accredited assessor for decisions.*"
    )
