# Singlestone Data Engineer Exercise Submission

## Quickstart

### requirements (non-exhaustive)

- `libsnappy-dev` or binary distributed `python-snappy`
- LLVM 7+
  - specifically, when pip installing `pandas`, a dependency build (`setup.py` from `numba`) was failing for me when trying to access llvm_config, so I installed Debian's `llvm-7` and ran `LLVM_CONFIG=$(which llvm-config-7) pipenv install`
  - this may or may not be avoidable with binary distributions more common in something like Conda
- Python 3.5+

### Tooling

I generally use [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html) for dependency/venv management in Python - it has advantages over a `requirements.txt`, but may not be well known/used, thus I generate the requested file.

I've also written a `Makefile`, which encapsulates my workflow. Selection of Make was based on installed/user base and that a native tool would be a good entry point for an abstract audience, rather than something awesome, more easily cross platform, and in the same ecosystem, like [doit](https://blogs.aalto.fi/marijn/2016/02/25/doit-a-python-alternative-to-make/).

### running
for development, have `pipenv` and other system requirements and run from scratch with `make requirements.txt integration` to see the solution run.
alternatively, use `requirements.txt` to install pip packages and then use `python3 -m solution`.

## Problem Statement

The goal of this project is to create a small app using the same techniques you would normally use for a client.
When writing your application there are a few assumptions to keep in mind:

* Single machine will run the application not a cluster of computes.
* The machine will be somewhat limited in resources.
* When working with data no matter the size of the data in the exercise,
  assume it is too large to fit it all into memory.


### Directions:

Write a python application that processes the two data files [students.csv , teachers.parquet]. The application should
use both files to output a report in json listing each student, the teacher the student has and the class ID the student is 
scheduled for. 

Your submission should have everything required such that it could be given to an analyst(ie none developer), and they are able 
setup and run your application using directions provided.

## interpreted/assumed Acceptance Criteria

- runs on single machine
- dataset larger than memory (note: for most effective strategy to fulfil the business logic and this requirement, I settled on the following)
  - parquet approach: producing an index off the parquet data (rather than reading all columns), since we only needed a full name per class id, and teachers-to-students is one-to-many in these datasets. As my first time actually hands-on with parquet and its patterns, there may be a better approach, and I'd love to get feedback from the reviewers on other ways to tackle this. Perhaps the arrow read filters are more straightforward or functional, but I compromised to omit columns rather than rows/rowgroups, and to omit the seemingly larger/complex (and also unfamiliar) arrow.
  - csv approach: iterative chunked reads, with one full csv pass over the course of the runtime
- combine student csv and teacher parquet to generate output
- output format, per student: student, teacher, class id
- pylint score 10

(if this was for a customer, there would be more time spent up front clarifying and characterizing the system, especially nonfunctional, requirements)

## Test Plan ( implicit TD-development plan )

- collaborator tests to understand selected libraries/apis (done)
- csv chunk read helper units (done)
- teacher indexing/lookup helper units (done)
- integration test to assert expected output from proceesing example csv/parquet datasets (done)
