from invoke import task

@task
def test(ctx):
    "Run pytests"
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    "Run tests with coverage"
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    "Generate coverage report"
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    "Run pylint"
    ctx.run("pylint src", pty=True)