[metadata]
name = pre_commit_hooks
version = 0.8.0

[options]
packages = find:
install_requires =
    colorama
python_requires = >=3.6

[options.entry_points]
console_scripts =
    sbt-scalafmt = pre_commit_hooks.scalafmt:main
    sbt-scalafix = pre_commit_hooks.scalafix:main