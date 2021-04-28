# get_files_by_regex
Python script to recurse a given directory location and return a list of files whose names match a regex.


## Implemented Functions:
1. ```main()```: Checks the command line arguments for directory and regex, if no command line arguments were passed, uses current directory to list all files.

2. ```get_files_by_regex()```: Takes directory to recurse and regex as arguments. Returns list of files whose name matches the regex in given directory.

## Implemented Unit Tests:

1. ```test_get_all_files()```: Test return all files for a directory if no regex is passed

2. ```test_get_file_by_regex()```: Test return file to match the given regex

3. ```test_get_file_not_valid()```: Test return no file for a directory that does not exist

4. ```test_get_file_random_regex()```: Test return no file for regex not matching

5. ```test_get_file_not_valid_regex()```: Test return no file for invalid regex

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

### Code coverage
Code coverage for the script is at 72%

Code Coverage![image](https://user-images.githubusercontent.com/39092484/116478382-f9174f00-a84b-11eb-8d17-463e6dc729d0.png)

As shown in the above image, the code that is not covered are the one in main() function that checks the command line arguments passed. Unit test are written to run independtly and should not depend on arguments passed. This justifies the lines 47-56 not being covered by the unit tests.

### Execution Time
Exceution timeto return file names for a given directory and regexx is as shown below:

Exceution Time-1![image](https://user-images.githubusercontent.com/39092484/116480047-a2f7db00-a84e-11eb-833e-88e4bcba29e5.png)
Exceution Time-2![image](https://user-images.githubusercontent.com/39092484/116480028-9a9fa000-a84e-11eb-9d02-1d84575fcde9.png)


#### Improve execution time:
* As seen in the above image, providing sub-directories results in faster search.
* Use a dictionary to store filename and it's path. The dictionary can be saved as a pickle file. The next search for the filename will use the dictionary dumped in the pickle file and hence will be faster.


## Authors

* **Sunitha Sampath** - [sunithapriya](https://github.com/sunithapriyadarshini)

