# pyprovoke

A set of useful utilities and checks to run alongside the [Python invoke](http://www.pyinvoke.org/)
tool


### 🚧 IN PROGRESS 🚧

I'm still working on this!


### List of Utilities

There are a few utilities currently being built (the API is subject to change until version 1.0 is
solidified). The main goal was to build dependency checks on tasks such that a task will only run
if certain pre-conditions are met. This will give `invoke` a similar featureset to `Make` in that
it only runs certain tasks if a file doesn't exist or if a file has changed.

* `provoke.run_if_exists`: Only run a task if a file exists
* `provoke.run_if_not_exists`: only run a task if a file doesn't exist
* `provoke.run_if_changed`: only run a task if a file has changed


### The `.invokerc` File

Currently I am storing information that needs to be kept between invoke runs in an `.invokerc` file.
I don't know of any better method to accomplish this yet.
