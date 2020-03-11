# This is a dummy tasks.py file for testing
import invoke
from provoke import provoke

@invoke.task
@provoke.run_if_exists(path="README.md")
def test(ctx):
    print("I AM RUNNING")


@invoke.task
@provoke.run_if_changed(path="README.md")
def test2(ctx):
    print("I AM RUNNING x2")
