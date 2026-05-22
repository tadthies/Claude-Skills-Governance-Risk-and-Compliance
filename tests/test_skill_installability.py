"""
test_skill_installability.py
============================
Validates that every .skill file in the repository can be installed
by Claude without errors.

Rules enforced (mirrors the Claude skill installer):
  1. The archive must contain at least one entry.
  2. Exactly one SKILL.md must exist inside the archive.
  3. SKILL.md must live exactly ONE directory level deep:
       <skill-name>/SKILL.md   ✅
       skills/<skill-name>/SKILL.md  ❌  (two levels — triggers installer error)
       SKILL.md                ❌  (top-level — no wrapping folder)
  4. All reference files (if any) must sit under the same top-level folder
     as SKILL.md, e.g. <skill-name>/references/*.md
  5. The archive must not contain any path that escapes the top-level folder
     (path-traversal guard: no entry may start with / or contain ..)
  6. SKILL.md must not be empty (> 0 bytes).

Two sets of .skill files are tested:
  - Standalone: the <Name> - Claude Skill/<name>.skill files for direct download
  - Plugin-bundled: plugins/<name>/<name>.skill files shipped with each plugin

Run with:
    pip install pytest
    pytest tests/test_skill_installability.py -v
"""

import zipfile
from pathlib import Path
import pytest

# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"

# Standalone .skill files: live in "<Name> - Claude Skill/" folders
STANDALONE_SKILL_FILES = sorted([
    p for p in REPO_ROOT.rglob("*.skill")
    if "plugins" not in p.parts and ".claude" not in p.parts
])

# Plugin-bundled .skill files: live at plugins/<name>/<name>.skill
PLUGIN_SKILL_FILES = sorted([
    p for p in PLUGINS_DIR.rglob("*.skill")
    if p.parent.name == p.stem  # e.g. plugins/iso27001/iso27001.skill
])

ALL_SKILL_FILES = sorted(set(STANDALONE_SKILL_FILES) | set(PLUGIN_SKILL_FILES))

# ---------------------------------------------------------------------------
# Expected inventory — update when adding a new skill
# ---------------------------------------------------------------------------

# Canonical lowercase kebab-case names for all 28 skills
EXPECTED_SKILL_NAMES = {
    "ccpa",
    "cis-controls",
    "cmmc",
    "csrd",
    "dora",
    "dpdpa",
    "ear",
    "eu-ai-act",
    "fedramp",
    "gdpr-compliance",
    "hipaa-compliance",
    "ism",
    "iso27001",
    "iso27701",
    "iso42001",
    "itar",
    "lgpd",
    "nis2",
    "nist-800-53",
    "nist-ai-rmf",
    "nist-csf",
    "nzism",
    "pci-compliance",
    "section-508",
    "soc2",
    "swift-csp",
    "tsa-compliance",
    "vn-pdpl",
    "wcag",
}

# Standalone filenames as they actually appear on disk (some legacy names differ)
EXPECTED_STANDALONE_FILENAMES = {
    "ccpa.skill",
    "cis-controls.skill",
    "cmmc.skill",
    "csrd.skill",
    "dora.skill",
    "dpdpa.skill",
    "ear.skill",
    "eu-ai-act.skill",
    "fedramp.skill",
    "gdpr-compliance.skill",
    "hipaa-compliance.skill",
    "ism.skill",
    "iso27001.skill",
    "iso27701.skill",
    "ISO-42001.skill",
    "itar.skill",
    "lgpd.skill",
    "nis2.skill",
    "nist-800-53.skill",
    "nist-ai-rmf.skill",
    "NIST Cybersecurity.skill",
    "nzism.skill",
    "PCI-Compliance.skill",
    "vn-pdpl.skill",
    "section-508.skill",
    "soc2.skill",
    "swift-csp.skill",
    "TSA-Compliance.skill",
    "wcag.skill",
}


def pytest_generate_tests(metafunc):
    """Parametrise every test that accepts a skill_path fixture."""
    if "skill_path" in metafunc.fixturenames:
        ids = [
            f"{'plugin' if 'plugins' in p.parts else 'standalone'}::{p.name}"
            for p in ALL_SKILL_FILES
        ]
        metafunc.parametrize("skill_path", ALL_SKILL_FILES, ids=ids)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _entries(skill_path: Path):
    """Return list of (name, file_size) for every entry in the archive."""
    with zipfile.ZipFile(skill_path) as zf:
        return [(info.filename, info.file_size) for info in zf.infolist()]


def _skill_md_entries(entries):
    return [name for name, _ in entries if name.upper().endswith("SKILL.MD")]


# ---------------------------------------------------------------------------
# Archive structure tests (parametrised over all .skill files)
# ---------------------------------------------------------------------------

class TestSkillArchiveStructure:

    def test_is_valid_zip(self, skill_path):
        """File must be a valid ZIP archive."""
        assert zipfile.is_zipfile(skill_path), (
            f"{skill_path.name} is not a valid ZIP file"
        )

    def test_archive_not_empty(self, skill_path):
        """Archive must contain at least one entry."""
        entries = _entries(skill_path)
        assert len(entries) > 0, f"{skill_path.name} is an empty archive"

    def test_exactly_one_skill_md(self, skill_path):
        """There must be exactly one SKILL.md in the archive."""
        entries = _entries(skill_path)
        skill_mds = _skill_md_entries(entries)
        assert len(skill_mds) == 1, (
            f"{skill_path.name}: expected 1 SKILL.md, found {len(skill_mds)}: {skill_mds}"
        )

    def test_skill_md_exactly_one_level_deep(self, skill_path):
        """
        SKILL.md must be exactly one directory level deep.

        Accepted:   <skill-name>/SKILL.md
        Rejected:   SKILL.md                       (top-level, depth 0)
                    skills/<skill-name>/SKILL.md   (two levels, depth 2+)
        """
        entries = _entries(skill_path)
        skill_md_path = _skill_md_entries(entries)[0]
        parts = Path(skill_md_path).parts
        depth = len(parts) - 1

        assert depth == 1, (
            f"{skill_path.name}: SKILL.md must be exactly one directory deep "
            f"(e.g. <skill-name>/SKILL.md), but found it at: {skill_md_path!r} "
            f"(depth={depth}). "
            "This causes the installer error: 'SKILL.md file must be in the "
            "top-level folder, not nested deeper.'"
        )

    def test_no_path_traversal(self, skill_path):
        """No entry may use absolute paths or .. components (security guard)."""
        entries = _entries(skill_path)
        bad = [
            name for name, _ in entries
            if name.startswith("/") or ".." in Path(name).parts
        ]
        assert not bad, (
            f"{skill_path.name}: archive contains unsafe paths: {bad}"
        )

    def test_all_files_under_top_level_folder(self, skill_path):
        """
        Every file entry must live under the same top-level folder as SKILL.md.
        Prevents partially-nested archives where some files escaped the skill folder.
        """
        entries = _entries(skill_path)
        skill_md_path = _skill_md_entries(entries)[0]
        top_folder = Path(skill_md_path).parts[0]

        bad = [
            name for name, _ in entries
            if not name.startswith(top_folder + "/")
            and name != top_folder + "/"
            and name != top_folder
        ]
        assert not bad, (
            f"{skill_path.name}: these entries sit outside the expected top-level "
            f"folder '{top_folder}/': {bad}"
        )

    def test_skill_md_not_empty(self, skill_path):
        """SKILL.md must have content (> 0 bytes)."""
        entries = _entries(skill_path)
        skill_md_name = _skill_md_entries(entries)[0]
        size = next(sz for name, sz in entries if name == skill_md_name)
        assert size > 0, (
            f"{skill_path.name}: SKILL.md exists but is empty (0 bytes)"
        )

    def test_references_under_skill_folder(self, skill_path):
        """
        If a references/ directory exists, all its contents must be under
        <skill-name>/references/, not at a different path.
        """
        entries = _entries(skill_path)
        skill_md_path = _skill_md_entries(entries)[0]
        top_folder = Path(skill_md_path).parts[0]

        ref_entries = [
            name for name, _ in entries
            if "reference" in name.lower() and not name.endswith("/")
        ]
        bad = [
            name for name in ref_entries
            if not name.startswith(f"{top_folder}/references/")
        ]
        assert not bad, (
            f"{skill_path.name}: reference files found outside "
            f"'{top_folder}/references/': {bad}"
        )


# ---------------------------------------------------------------------------
# Standalone folder hygiene tests
# ---------------------------------------------------------------------------

STANDALONE_DIRS = sorted([
    d for d in REPO_ROOT.iterdir()
    if d.is_dir() and d.name.endswith(" - Claude Skill")
])


def test_standalone_dirs_contain_no_unexpected_file_types():
    """
    Every '<Name> - Claude Skill' folder may contain .skill files and README/
    markdown files, but nothing else (e.g. no binaries, scripts, or config files).
    """
    ALLOWED_SUFFIXES = {".skill", ".md", ".txt"}
    violations = {}
    for skill_dir in STANDALONE_DIRS:
        unexpected = [
            f.name for f in skill_dir.iterdir()
            if f.is_file() and f.suffix.lower() not in ALLOWED_SUFFIXES
        ]
        if unexpected:
            violations[skill_dir.name] = unexpected

    assert not violations, (
        "Unexpected file types found in standalone skill folders:\n"
        + "\n".join(f"  {folder}: {files}" for folder, files in violations.items())
    )


def test_standalone_dirs_contain_exactly_one_skill_file():
    """Each '<Name> - Claude Skill' folder must contain exactly one .skill file."""
    violations = {}
    for skill_dir in STANDALONE_DIRS:
        skill_files = [f for f in skill_dir.iterdir() if f.suffix.lower() == ".skill"]
        if len(skill_files) != 1:
            violations[skill_dir.name] = [f.name for f in skill_files]

    assert not violations, (
        "Expected exactly one .skill file per standalone folder:\n"
        + "\n".join(f"  {folder}: {files}" for folder, files in violations.items())
    )


# ---------------------------------------------------------------------------
# Plugin .skill completeness check
# ---------------------------------------------------------------------------

def test_every_plugin_has_bundled_skill_zip():
    """
    Every plugin directory must contain a <plugin-name>.skill ZIP file.
    This is the bundled copy for direct download alongside the plugin source.
    """
    plugin_dirs = sorted([p for p in PLUGINS_DIR.iterdir() if p.is_dir()])
    missing = []
    for plugin_dir in plugin_dirs:
        expected = plugin_dir / f"{plugin_dir.name}.skill"
        if not expected.exists():
            missing.append(f"plugins/{plugin_dir.name}/{plugin_dir.name}.skill")

    assert not missing, (
        "The following plugins are missing their bundled .skill ZIP.\n"
        "Copy the standalone .skill file into the plugin folder to fix:\n"
        + "\n".join(f"  {m}" for m in missing)
    )


# ---------------------------------------------------------------------------
# Inventory sanity checks
# ---------------------------------------------------------------------------

def test_all_expected_standalone_skills_present():
    """
    All 27 expected standalone .skill files must exist.
    When adding a new skill, add its filename to EXPECTED_STANDALONE_FILENAMES.
    """
    found = {p.name for p in STANDALONE_SKILL_FILES}
    missing = EXPECTED_STANDALONE_FILENAMES - found
    assert not missing, (
        f"Expected standalone .skill files not found: {missing}"
    )


def test_no_unexpected_standalone_skills():
    """
    Warn if standalone .skill files appear that are not in the expected set.
    This catches new skills added without updating the test inventory.
    When adding a new skill, update EXPECTED_STANDALONE_FILENAMES above.
    """
    found = {p.name for p in STANDALONE_SKILL_FILES}
    extra = found - EXPECTED_STANDALONE_FILENAMES
    assert not extra, (
        f"Found standalone .skill files not listed in EXPECTED_STANDALONE_FILENAMES — "
        f"add them to the set at the top of this test file: {extra}"
    )


def test_plugin_skill_names_match_canonical():
    """
    Every plugin-bundled .skill file must use the canonical lowercase kebab-case
    name matching its plugin directory name.
    """
    wrong = []
    for skill_file in PLUGIN_SKILL_FILES:
        plugin_name = skill_file.parent.name
        if skill_file.stem != plugin_name:
            wrong.append(
                f"plugins/{plugin_name}/{skill_file.name} "
                f"(expected: {plugin_name}.skill)"
            )
    assert not wrong, (
        "Plugin-bundled .skill files with incorrect names:\n"
        + "\n".join(f"  {w}" for w in wrong)
    )
