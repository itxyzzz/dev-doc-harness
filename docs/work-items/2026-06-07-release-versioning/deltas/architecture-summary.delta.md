# Architecture Summary Delta

Work ID: `2026-06-07-release-versioning`
Phase: Phase 02 release package implementation

## Release Identity

The harness package now carries `.agents/skills/dev-doc-harness/VERSION` with `0.3.0`.

## Release Policy Ownership

`module:release` is the canonical owner for release identity, distributable package boundary, changelog-as-release-source policy, release notes, compatibility, artifact release context, and team adoption flow.

## Compatibility Model

Harness release versions carry compatibility meaning. Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned retrieval and ownership anchors.

## Artifact Release Context

Current work-item templates include `Harness release: <version or unknown>` so new artifacts can record which harness release produced or froze them. Historical artifacts without the field remain pre-stamp artifacts.

## Phase 03 Follow-Up

Phase 03 should add validation for the package-local `VERSION`, release notes, source changelog section, current release-versioning changelog schema, package-boundary guidance, and existing graph checks.
