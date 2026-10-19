# Publishing

Package: `plainq-sdk` (import `plainq`). Repository: `marsolab/plainq-python-sdk`.

1. In your PyPI account, add a pending trusted publisher for project `plainq-sdk`,
   GitHub owner `marsolab`, repository `plainq-python-sdk`, workflow `publish.yml`,
   environment `pypi`. For an existing project, add a trusted publisher in its settings.
   See https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/ .
2. Update `pyproject.toml` and `uv.lock`, pass CI, commit, and push `vX.Y.Z`.
3. Run **Publish PyPI** against that tag. The workflow reruns CI, verifies the tag
   and version, builds wheel/source distributions, then publishes using GitHub OIDC.
   No long-lived registry token is required.
4. Verify `pip index versions plainq-sdk` and install the published version in
   a clean environment.

A GitHub release and built distributions are separate from PyPI publication.
Manual fallback after configuring credentials locally: `uv build && uv publish`.
Never commit credentials or paste tokens into chat.
