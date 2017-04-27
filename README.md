# PC_Testing_and_CI ![IA](https://img.shields.io/badge/IA-Programmers Club-brightgreen.svg)

Some introductory things in automated ways to improve your code, and to make your
The idea is to introduce them and you can try use them if you think they will be helpful to you.
The examples are mostly for python but the ideas are more general.

##### Contents
- Linting
- Testing
- Web Services integration

To follow the examples in this document clone the repo, cd into the directory and run: ```pip install -r requirements.txt```

# Linting
*A process of running a program that will analyse code for potential errors.*. Essentially spell-check for your code.

- **Style**: Indentation, spaces, comments, doc-strings, variable names.
- **Correctness**: `x is None` rather than `x == None`,
- **Complexity**: Counts nested if-else statements.
- Unused variables
- Finds TODO's
- Type checking (mypy)

If you code is of a consistent style then it easier to read, understand and edit. For yourself and others.

Many are standalone software but there are many plugins available for your IDE or text editor.

For example [flake8](http://flake8.pycqa.org/en/latest/) is a good python linter, following the PEP8 style guide with error and complexity checks.

You can run it in this directory to get a list of errors in examples.py
```
flake8
```

- You can check your latex documents with  [chktex](http://www.nongnu.org/chktex/). (Who hasn't misplaced a $ or [] before.)

- Or bash scripts with [shellcheck](https://www.shellcheck.net/)


Should be able to find plugins for the text editor you use, and programming language you need. I find having the plugins very useful as I see the errors appear as I am writing the code and don't need to manually rerun the linter.

Can turn off specific errors if you don't want them included.
E.g.
- operator spacing
- comment style
- Unused variables
- Found TODO's

See the documentation for error codes, and/or how to disable them.

Maybe overwhelming on large code at first so you can start by disabling all and re-enable a few at a time.

[mypy](http://mypy-lang.org/) is a static type checker which uses the type-hinting from [PEP484](https://www.python.org/dev/peps/pep-0484/).
```
mypy examples.py --ignore-missing-imports
```
`--ignore-missing-imports` is to ignore the complaints about mypy not understanding `numpy` **yet**.


*I have heard automated linter checks for collaborative projects can help coders self-esteem. Its less personal if the tool tells you to tidy up your code before it can be added than if a person does it.*

## CI Testing
From wikipedia ...
>Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the software is improved to pass the new tests, only

Not quite suitable for research but we can make use of some of the concepts/tools.

> In software testing, test automation is the use of special software (separate from the software being tested) to control the execution of tests and the comparison of actual outcomes with predicted outcomes.

Different types of testing, with differing/overlapping names. E.g. unit tests, integration test, system test, end-user tests, quality assurance tests...

Here I focus on unit-tests and property-based testing.

####[Unit-tests](http://softwaretestingfundamentals.com/unit-testing/):
- Test the functionality of one single unit of code. E.g. one function per test.
- Can have more then one check in a given test.
- Should be Small and fast. You will them running them
- Should not just be a duplication of the code.


For python:
- [Unittest](https://docs.python.org/2/library/unittest.html) - built in test framework. Tests written as **Classes**.
- [nose](https://nose.readthedocs.io/en/latest/testing.html)
- [pytest](pytest.org)
  - Scans directory for `test[s]/` `test_*.py` or `*_test.py` files.
  - Runs functions that begin with `test_` or end with `_test`.
  - Can run Unittest and nose test cases.


Some test examples are in test_examples.py.
These run if you type in this directory:
```
pytest
```

pytest does magic things with python's `assert` function which makes it easy to use.
If the `assert` fails it prints a breakdown of why it failed.


Some useful features of pytest shown in the examples are:
- @pytest.mark.xfail(), @pytest.mark.xpass()
    - Allows you to mark tests that are known to be failing, will always fail, or sometimes fail.
    - Still allow test suite to "pass" successfully.
- @pytest.raises(ERROR)
 - Test that "ERROR" was raised.
- @pytest.mark.parametrize()
 - Run same test with different parameters.
 - Removes duplication of code.

See the [pytest documentation](https://docs.pytest.org/en/latest/contents.html#toc) for much more...


[Pytest Fixtures](https://docs.pytest.org/en/latest/fixture.html):
> The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute.

Ability to pass result of long process into many tests.
 - e.g. database access, web-request, load file.
 - Reduces test run-time and code duplication.


#### [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) - Property based testing.
Often in science there is not an exact value to test. `assert x == 42` We can however test the properties of the values we expect.
Type, length, shape, attributes etc.

Good examples are reversible processes:
-  Encryption / Decryption
-  Coordinate transformation

Hypothesis is a tool allowing you to test the properties of you code.
It generates data to pass into test cases, following defined **strategies**.

Some **strategies** are.
- int, float, bool
- list, tuple, sample_from

You can also refine the strategies, such as setting min/max size values, inclusion of infinity etc.

It throws in unique cases trying to find corner cases you have not though of to test. e.g. *inf*, *Nan* or an empty list.

- Tries 200 (default) different combinations.
- Remembers failed test cases, to test again.

The new release has support for `numpy` although I have not used it yet.

#### Coverage
How much run able code was actually ran during the tests? Tells you percentage of coverage and which lines were not run.

```
pytest --cov=. --cov-report term-missing

```
It is only helpful metric if you have **useful tests**.

Should aim to always increase coverage when adding new functionality.
Large project possibly won't accept new features unless they have the associated test.

Of course this metric is not vital to the success of your project, but others are more likely to contribute to a well tested and covered project.

Requires the [coverage](https://coverage.readthedocs.io/en/coverage-4.3.4/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) packages.

## Web Services
There are many web-services available that you can link to your github projects.
- Public repo's use these for free while private repo's need to pay.

When ever you push your code to github it will trigger these services to run, and email you any changed result.

#### Code Review:
Services that perform automated code review checks on your code. I find they complement linting, and each other.
The links here are to my [spectrum_overload](https://github.com/jason-neal/spectrum_overload) project on each of these sites.

Examples:
- [Code Climate](https://codeclimate.com/github/jason-neal/spectrum_overload)
- [Quantified code](https://www.quantifiedcode.com/app/project/gh:jason-neal:spectrum_overload) [![Code Issues](https://www.quantifiedcode.com/api/v1/project/b98ac59838124f07838fd514af29b183/badge.svg)](https://www.quantifiedcode.com/app/project/b98ac59838124f07838fd514af29b183)
  - Can submit pull requests on your repo to make suggested changes. e.g. [this PR](https://github.com/jason-neal/spectrum_overload/pull/8)


#### Continuous Integration Testing: [![Build Status](https://travis-ci.org/jason-neal/PC_Testing_and_CI.svg?branch=master)](https://travis-ci.org/jason-neal/PC_Testing_and_CI)
Services that run your tests.
  - Clone repo and install
  - run tests e.g. pytest
  - after success - do something?
  - Email changed build result.

[Travis CI](https://travis-ci.org/jason-neal/spectrum_overload) but many others with different flavors (windows, phone apps).
  - configure with .travs.yml file in project root dir

#### Coverage: [![Coverage Status](https://coveralls.io/repos/github/jason-neal/PC_Testing_and_CI/badge.svg)](https://coveralls.io/github/jason-neal/PC_Testing_and_CI)
- [coveralls.io](https://coveralls.io/github/jason-neal/spectrum_overload)
- Displays code coverage statistics, and missing lines.
- Comments coverage change on [PR's](https://github.com/jason-neal/spectrum_overload/pull/19)

#### Documentation:
> [Sphinx](http://www.sphinx-doc.org/en/stable/) is a tool that makes it easy to create intelligent and beautiful documentation

- [Auto-documentation](http://www.sphinx-doc.org/en/stable/ext/autodoc.html#module-sphinx.ext.autodoc) from module/class/function doc strings.

[Read The Docs](https://readthedocs.org/) has become popular place to host the documentation of software.

- Builds the html documentation from your github repo and hosts it.

### Pypi
Make your software available from a package manager. Make easy for others to install.
e.g. `pip install ...`
- Easier than you think...
- [How to submit a package to PyPi](http://peterdowns.com/posts/first-time-with-pypi.html)

#### Badges:
Little tokens to display on your documentation, website.
Gives a quick look at the status of your project.
  - tests passing
  - well covered
  - latest version
  - etc.

You can make your own badges at [shields.io/](https://shields.io/). ![IA](https://img.shields.io/badge/IA-Programmers Club-brightgreen.svg)

Much like Pokémon, gotta catch 'em all!

### Advanced for dev teams / large projects:
- [pre-commit Hooks](https://github.com/pre-commit/pre-commit-hooks)
    - Lint check, run tests have to pass before commits or pushes.
- [Fail tests if linting doesn't pass](https://jeffknupp.com/blog/2016/12/09/how-python-linters-will-save-your-large-python-project/)
- Daily test builds?


### Links
- [pytest](https://docs.pytest.org/en/latest/)
- [coverage](https://coverage.readthedocs.io/en/coverage-4.3.4/)
- [Code Coverage-- General](https://wiki.python.org/moin/CodeCoverage)
- [Test and Code Podcast](http://pythontesting.net/test-podcast/)
- [Package Bling](http://tjelvarolsson.com/blog/five-steps-to-add-the-bling-factor-to-your-python-package/)
- [practical software testing tips](http://www.softwaretestinghelp.com/practical-software-testing-tips-to-test-any-application/)
