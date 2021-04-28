# get_files_by_regex
Python script to recurse a given directory location and return a list of files whose names match a regex.


## Implemented Functions:
1. ```main()```: Checks the command line arguments for directory and regex, if no command line arguments were passed, uses current directory to list all files.

2. ```get_files_by_regex()```: Takes directory to recurse and regex as arguments. Returns list of files whose name matches the regex in given directory.

## Implemented Unit Tests:

1. ```test_get_all_files()```: Test return all files for a directory if no regex is passed

2. ```test_get_file_by_regex()```: Test return file to match the given regex

3. ```test_get_file_not_valid()```: Test return no file for a directory that does not exist

4. ```test_get_file_not_valid_regex()```: Test return no file for random regex

## Getting Started
### Prerequisites
```
python
```

### Installing
1. Download the module
```
git clone https://github.com/sunithapriyadarshini/search_files.git
```

### Running
The command line arguments for get_files.py are as follows:  
1.`-d` or `--directory` directory to recurse

2.`-r` or `--regex` regex to match
Note: Pass regex in quotes, alternatively escape characters that are special to bash to get the match 

```
python3 get_files/get_files.py -d . -r '.*.py'
```

### Running Unit Tests
```
python3 -m unittest test/get_files_test.py
```

###Code coverage
Code coverage for the script is at 72%

Code Coverage![image](https://user-images.githubusercontent.com/39092484/116478382-f9174f00-a84b-11eb-8d17-463e6dc729d0.png)

As shown in the above image, the code that is not covered are the one in main() function that checks the command line arguments passed. Unit test are written to run independtly and should not depend on arguments passed. This justifies the lines 47-56 not being covered by the unit tests.



## Authors

* **Sunitha Sampath** - [sunithapriya](https://github.com/sunithapriyadarshini)

