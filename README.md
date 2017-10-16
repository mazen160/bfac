BFAC
----
*Advanced Backup-File Artifacts Testing for Web-Applications*

![BFAC](https://raw.githubusercontent.com/mazen160/public/master/static/images/BFAC-banner.png)

BFAC (Backup File Artifacts Checker) is an automated tool that checks for backup artifacts that may disclose the web-application's source code. The artifacts can also lead to leakage of sensitive information, such as passwords, directory structure, etc.

**The goal of BFAC is to be an *all-in-one tool* for backup-file artifacts black-box testing.**

## Features
* Multithreaded scanning.
* Includes request rate throttling.
* HTTP proxy support.
* Uses multiple algorithms for automatically detecting valid and invalid pages.
* HTTP proxy support
* User agent randomization.
* Batch processing.
* Works both as a command-line tool and Python module.
* Support for Windows, MacOS, and Linux operating systems.
* Reporting: simple, verbose, CSV, JSON.

## Usage

| Description                                                | Command                                                                 |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| Help                                                       | `bfac --help`                                                           |
| Check a single URL.                                        | `bfac --url http://example.com/test.php`                                |
| Check a list of URLs.                                      | `bfac --list testing_list.txt`                                          |
| Single URL with a different level (level 2 for example).   | `bfac --url http://example.com/test.php --level 2`                      |
| Single URL and show the results only.                      | `bfac --no-text --url http://example.com/test.php`                      |
| Limit the test to exposed DVCS tests.                      | `bfac --dvcs-test --url http://example.com/`                            |
| Verify existence of files using Content-Length checks only.| `bfac --detection-technique content_length http://example.com/test.php` |
| Verify existence of files using Status-Code checks only.   | `bfac --detection-technique status_code http://example.com/test.php`    |
| Exclude results with specific status-codes.                | `bfac --exclude-status-codes 301,999 http://example.com/test.php`       |


## Using BFAC as a module
```python
import bfac


testing_level = 5

# Returns a list of BFA patterns for http://example.com/test.php
bfa_urls = bfac.generate_bfa_urls(
    'http://example.com/test.php', testing_level=testing_level)

# Performs BFA testing using BFAC, and returns a list of findings, if any.
# If nothing is identified, it returns an empty list.
bfa_testing_result = bfac.test_url(
    'http://example.com/test.php', testing_level=testing_level)
```


## Requirements
* Python2 or Python3
* requests
* colorama


## Installation [Optional]
`sudo python setup.py install`


## Compatibility
The project currently supports all platforms that run Python.
The project is compatible with both Python 2 and Python 3.


## Frequently Asked Questions
**Q:** How to use BFAC with all levels?

**A:**
BFAC runs with all levels by default. if you would like to decrease the used testing level, you can do it by setting the `--level` flag to a lower value.


**Q:** How do BFAC determines if the file actually exists on the web-server or not?

**A:**
BFAC approach regarding detection differs from regular security tools.

Regular security tools determinate if a file exists on a server by checking the HTTP status code. Since there are system administrators that might spoof HTTP status codes for HTTP requests to fool security tools and bots, BFAC implemented an additional method.

It checks for the general response of an invalid or non-available web resource. Then, it sends requests and compare the response size of the request with the initial base.

* `--detection-technique all` uses both methods for HTTP Status Code checks, and the HTTP Content-Length.
* `--detection-technique status_code`: uses HTTP status code checks only.
* `--detection-technique content_length`: uses HTTP Content-Length checks only.


## Community Contribution
Contribution from the community to the BFAC project is very welcome. If you find a bug, have an idea for a feature, ideas to reconstruct the code to work better, or anything else, feel free to submit an issue or a pull request.


### Using the issue tracker

The issue tracker is the preferred channel for bug reports and features requests.

[![GitHub issues](https://img.shields.io/github/issues/mazen160/bfac.svg?style=flat-square)](https://github.com/mazen160/bfac/issues)


## Legal Disclaimer
This project is made for educational and ethical testing purposes only. Usage of BFAC for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.


## License
The project is currently licensed under GNU GPLv3.0 License.

[![GitHub license](https://img.shields.io/badge/license-GPL-blue.svg?style=flat-square)](https://raw.githubusercontent.com/mazen160/bfac/master/LICENSE.txt)


## Author
*Mazin Ahmed*
* Website: [https://mazinahmed.net](https://mazinahmed.net)
* Email: *mazin AT mazinahmed DOT net*
* Twitter: [https://twitter.com/mazen160](https://twitter.com/mazen160)
* Linkedin: [http://linkedin.com/in/infosecmazinahmed](http://linkedin.com/in/infosecmazinahmed)
