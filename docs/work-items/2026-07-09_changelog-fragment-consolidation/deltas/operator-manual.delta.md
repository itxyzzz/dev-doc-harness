# Operator Manual Delta

Work ID: `2026-07-09_changelog-fragment-consolidation`
Short ID: `changelog-fragment-consolidation`
Status: Implemented
Harness release: `0.5+`
Schema: `schema:delta.operator-manual`

## Delta

Routine harness work now records changelog source entries in the work-item
package instead of editing root `CHANGELOG.md` before every commit.

Operators should expect agents to update:

```text
docs/work-items/<work-id>/changelog/*.md
```

before planning approval commits, implementation commits, amendment commits, or
phase commits. Fragment entries use the same changelog heading and metadata
fields as root changelog entries.

Root `CHANGELOG.md` remains the consolidated publication view. Run:

```bash
python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py
```

at a project-owned checkpoint such as after merging work branches, before
preparing release notes, before product/application release, or whenever the
project's process needs root changelog completeness. Use `--check` when the
checkpoint should only verify that consolidation has already happened.

The Dev Doc Harness distribution release process is separate from downstream
software release processes. This repository's harness maintainer release
branch process consolidates fragments before curating package-local Dev Doc
Harness release notes. Downstream applications, packages, and agentic systems
keep their own release, deployment, and publication processes; they only need
to place the harness consolidation step wherever root changelog completeness is
useful in their process.
