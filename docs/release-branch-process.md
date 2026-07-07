# Release Branch Process

Use this runbook when an operator asks an agent in chat to create the next minor release branch for the dev-doc-harness repository.

The agent performs the steps. The operator should not need to run the commands manually unless a preflight fails or the release is not the normal next minor release.

This runbook is repository process documentation. Release notes created by this process belong in the distributable package under `.agents/skills/dev-doc-harness/docs/releases/`, not under root `docs/`.

## Default Release Shape

The default flow cuts the next minor release:

| Name | Meaning | Example after latest remote branch `release/0.4` |
|---|---|---|
| Latest release version | Version from the newest remote `release/<major>.<minor>` branch, with patch `.0` implied | `0.4.0` |
| Current version | Release version being cut, equal to the latest release version plus one minor version and patch reset to `0` | `0.5.0` |
| Release branch | Branch name for the current version, without trailing patch zero | `release/0.5` |
| Release notes | Package-local Markdown file for the current version | `.agents/skills/dev-doc-harness/docs/releases/0.5.0.md` |
| Development marker | Version marker after the release branch is cut | `0.5+` |

If the operator wants a patch, major, prerelease, or nonstandard release, stop and ask for explicit version instructions before editing files.

## Preflight

1. Confirm the current branch is `master`.

   ```powershell
   $currentBranch = git branch --show-current
   if ($currentBranch -ne "master") {
     Write-Error "Release branch creation must start from master. Current branch: $currentBranch"
     exit 1
   }
   ```

   If the current branch is not `master`, exit before making changes and report the branch mismatch to the operator.

2. Confirm the worktree is clean enough for release edits.

   ```powershell
   git status --short
   ```

   If unrelated changes are present, stop and ask the operator how to proceed.

3. Refresh remote branch information and identify the newest remote release branch.

   ```powershell
   git fetch --prune origin
   git ls-remote --heads origin "refs/heads/release/*"
   ```

   Use only branch names matching `release/<major>.<minor>`, such as `release/0.4`. Ignore local-only release branches when deriving the latest release version.

4. Derive the versions.

   - Set the latest release version from the newest remote release branch. For `release/0.4`, the latest release version is `0.4.0`.
   - Set the current version by incrementing the minor version and resetting patch to zero. For latest release version `0.4.0`, the current version is `0.5.0`.
   - Set the release branch name by dropping the trailing `.0` from the current version. For current version `0.5.0`, use `release/0.5`.
   - Set the post-release development marker to `<major>.<minor>+` for the released minor. For current version `0.5.0`, use `0.5+`.

## Prepare The Release On Master

1. Update `.agents/skills/dev-doc-harness/VERSION` to exactly the current version.

2. Update `CHANGELOG.md`.

   - Rename the top `## Unreleased` group to the release group for the current version.
   - Use the current changelog heading style, such as `## Release 0.5`, while keeping entry metadata release targets as exact versions such as `0.5.0`.
   - Do not add the next empty `Unreleased` group yet. That happens after the release branch is created and `master` is checked out again.

3. Create package-local release notes at:

   ```text
   .agents/skills/dev-doc-harness/docs/releases/<current-version>.md
   ```

   For example:

   ```text
   .agents/skills/dev-doc-harness/docs/releases/0.5.0.md
   ```

4. Curate the release notes from the changelog entries for the current version.

   Use the current release-note structure from the latest package-local release note. At minimum, include:

   - A title naming `Dev Doc Harness <current-version>`.
   - A `Release` section with a short summary of the release outcome.
   - A `Package Contents` section that preserves the distributable package boundary.
   - `Added`, `Changed`, `Removed`, or other Keep a Changelog sections as applicable to the curated changelog entries.
   - `Compatibility`, `Team Adoption`, and `Rollback` sections when the current release-note style includes them.
   - A `Source Changelog Entries` section listing the exact changelog entry headings used as source material.

   The release notes should summarize delivered release-facing changes once. Planning-only entries may appear in `Source Changelog Entries` for traceability when they support the delivered change, but they should not become duplicate feature bullets.

5. Review the release-prep diff.

   ```powershell
   git diff -- .agents/skills/dev-doc-harness/VERSION CHANGELOG.md .agents/skills/dev-doc-harness/docs/releases
   ```

6. Commit the release-prep changes on `master`.

   ```powershell
   git add .agents/skills/dev-doc-harness/VERSION CHANGELOG.md .agents/skills/dev-doc-harness/docs/releases/<current-version>.md
   git commit -m "release: prepare <current-version>"
   ```

## Create And Push The Release Branch

1. Create the release branch from the release-prep commit.

   ```powershell
   git checkout -b release/<major>.<minor>
   ```

   For current version `0.5.0`, this is:

   ```powershell
   git checkout -b release/0.5
   ```

2. Push the release branch to the remote repository.

   ```powershell
   git push -u origin release/<major>.<minor>
   ```

3. Confirm the remote branch exists.

   ```powershell
   git ls-remote --heads origin "refs/heads/release/<major>.<minor>"
   ```

## Reset Master For The Next Development Cycle

1. Check out `master`.

   ```powershell
   git checkout master
   ```

2. Add a new empty `Unreleased` group at the top of `CHANGELOG.md`, above the release group just created.

   Use the existing changelog metadata style for future entries, but do not invent a placeholder entry. The empty section should be just:

   ```md
   ## Unreleased

   ## Release <major>.<minor>
   ```

3. Update `.agents/skills/dev-doc-harness/VERSION` to the development marker.

   For current version `0.5.0`, write:

   ```text
   0.5+
   ```

4. Review the post-release reset diff.

   ```powershell
   git diff -- .agents/skills/dev-doc-harness/VERSION CHANGELOG.md
   ```

5. Commit the post-release reset on `master`.

   ```powershell
   git add .agents/skills/dev-doc-harness/VERSION CHANGELOG.md
   git commit -m "chore: start <major>.<minor>+ development"
   ```

6. Stop and report the outcome.

   Include:

   - The current version.
   - The release-prep commit hash.
   - The pushed release branch name.
   - The post-release reset commit hash on `master`.
   - Whether `master` has been pushed.

   Do not push `master` unless the operator explicitly asks for that separate action.

## Failure Handling

- If the current branch is not `master`, exit before edits.
- If no remote `release/<major>.<minor>` branch exists, stop and ask the operator for the starting release version.
- If a release branch for the current version already exists locally or remotely, stop and ask whether to inspect, reuse, or abandon that branch.
- If release notes cannot be curated cleanly from the changelog, stop and report the ambiguous entries instead of guessing.
- If any commit or push fails, stop on the current branch and report `git status --short --branch` plus the failing command.
