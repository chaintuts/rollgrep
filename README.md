## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* RollGrep counts instances of techniques in a CSV hobby log

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build directory

### Features
* Use regular expressions to count instances of techniques in a hobby log

### Requirements
* Requires Python 3

### Platforms
* Windows
* Linux
* MacOSX

## Usage
____________

### General usage
* Place logfile in the bin directory
* Modify config file with constants for log filename, desired techniques, and CSV header (column) to search under
* Run `rollgrep.py`


