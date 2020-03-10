# This is a dummy tasks.py file for testing
import invoke
from provoke import provoke

@invoke.task
@provoke.depends(file="README.md")
def test(ctx):
    print("I AM RUNNING")
