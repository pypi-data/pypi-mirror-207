Thinly scoped and opinionated tool that computes a version number from git tags
and trailers

--------------------------------------------------------------------------------

Python3.8+ CLI that computes a version number `MAJOR.MINOR.PATCH` based on git
tags and commit trailers.

Every project starts at `0.0.0`.
By default, every commit increments the `RELEASE` portion of the version.

In any commit, one may include a trailer of the form::

```
ci-version-bump: {patch,minor,major}
```


The version number will be incremented accordingly.

As an example:

```mermaid
flowchart LR
    v0(fa:fa-tag 0.0.0)
    v1(fa:fa-tag 0.0.1)
    v2(fa:fa-tag 0.0.2)
    v3(fa:fa-tag 0.1.0)
    v4(fa:fa-tag 0.1.1)
    v5(fa:fa-tag 1.0.0)
    v6(fa:fa-tag 1.0.1)

    v0 -->|fa:fa-message patch| v1
    v1 -->|fa:fa-message patch| v2
    v2 -->|fa:fa-message minor| v3
    v3 -->|fa:fa-message patch| v4
    v4 -->|fa:fa-message major| v5
    v5 -->|fa:fa-message patch| v6
```
