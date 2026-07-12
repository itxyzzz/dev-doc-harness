### 2026-07-11_post-release-pr-flow docs: require protected post-release synchronization

Release target: `unreleased`
Package impact: `repository-only`
Release-note: `source-only`

#### Changed

- Required post-release development state to reach protected `master` through a topic-branch pull request, followed by remote ancestry and released-changelog verification before new development branches are created.
