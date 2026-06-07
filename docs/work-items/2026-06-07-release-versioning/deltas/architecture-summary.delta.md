# Architecture Summary Delta

Work ID: `2026-06-07-release-versioning`
Phase: Phase 03 release hardening

## Release Identity

The harness package now carries `.agents/skills/dev-doc-harness/VERSION` with `0.3.0`.

## Release Policy Ownership

`module:release` is the canonical owner for release identity, distributable package boundary, changelog-as-release-source policy, release notes, compatibility, artifact release context, and team adoption flow.

## Compatibility Model

Harness release versions carry compatibility meaning. Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned retrieval and ownership anchors.

## Artifact Release Context

Current work-item templates include `Harness release: <version or unknown>` so new artifacts can record which harness release produced or froze them. Historical artifacts without the field remain pre-stamp artifacts.

## Validation Hardening

Phase 03 adds validation for package-local release identity, release-note headings and source changelog traceability, current release-versioning changelog metadata, package-boundary guidance, template release context, release routing, and existing graph checks.
