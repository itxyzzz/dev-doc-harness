# Superpowers Stub Continuity Test Cases

Status: Approved
Work ID: `2026-07-12_superpowers-stub-continuity`

## `TC-001` Absent directory remains absent

Given a repository has no `docs/superpowers` directory and no prior packages there, when Superpowers requests its default output path, then the harness workflow creates no directory or stub and keeps the durable artifact under `docs/work-items/<work-id>/`.

## `TC-002` Empty or newly seeded directory does not qualify

Given `docs/superpowers` is empty or was created during the current work, when compatibility is evaluated, then the workflow treats the continuity gate as unsatisfied and adds no document there.

## `TC-003` Historical packages permit pointers only

Given `docs/superpowers` predates the current work and contains previous documentation packages, when a continuity document is needed, then the new document contains only a title, status, and link to the canonical harness package or artifact.

## `TC-004` Full duplicate remains prohibited

Given the historical-package gate is satisfied, when a proposed file duplicates spec or plan content, then the contract rejects it because compatibility permits only a minimal pointer stub.

## `TC-005` Current repository deletes legacy stubs

Given the operator manually deleted six tracked stubs, when implementation is committed, then all six deletions are present and no `docs/superpowers` file is added or recreated.

## `TC-006` Frozen history remains unchanged

Given historical work-item artifacts truthfully record the former compatibility behavior, when the live contract is strengthened, then those frozen artifacts remain byte-for-byte unchanged.

## Approval

- Status: Approved
- Superseded by: None
