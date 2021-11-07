In order to implement a suitable solution for this problem we need to have a good understanding of definitions
and our requirements. Some of the assumptions we are going to make:

### Assumptions
- Word Definition: 
  - We assume all the non-digit strings such as propositions are defined as words.
  - All strings containing at least one digit are not considered as words.
- Size of the input file: depending on the size of file we might want to change our solution. If our input
file is big and loading the whole text to the memory is not an option we could go for windowed reading solution
or simply `chunked` data processing and then aggregating chunks results together. But for this task we assume
that whole file can fit in memory at one go.
- Input is a single file of text.
- Output will be only printed on standard output.


### Usage

Our solution is dockerized to make it easy for deployment on different types of infrastructures.
You need docker and docker-compose to run the solution.

```
docker-compose up --build app 
```

Currently input file is specified from `run.sh` script as an argument passed to the script which can be 
modified for another path.

### Tests
To run tests you can simply run 

```
docker-compose up --build test
```

### More?
Depending on the infra choice we can add CI/CD integration and monitoring.
