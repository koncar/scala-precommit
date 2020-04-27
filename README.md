# Scala pre-commit hooks

Pre commit/push hooks for formating and removing unused imports from scala project

### Instalation
First copy `.pre-commit-config.yaml` to your scala  project

Then same from your scala project execute:
```
pip install pre-commit

# and then one of following two commands
# pre push hook
pre-commit install --hook-type pre-push
# pre commit hook
pre-commit install
```

In `plugins.sbt` you should have plugins for `scalafmt` and `scalafix`
```
addSbtPlugin("org.scalameta"  % "sbt-scalafmt"  % "2.3.2")
addSbtPlugin("ch.epfl.scala" % "sbt-scalafix" % "0.9.13")
``` 

also add this to `build.sbt`
```
addCompilerPlugin(scalafixSemanticdb)
scalacOptions ++= List(
  "-Yrangepos",
  "-Ywarn-unused-import"
)
```
