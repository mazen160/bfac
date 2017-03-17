BFAC
---
*Advanced Backup-File Artifacts Testing for Web-Applications*

![BFAC](https://www.dropbox.com/s/laiho8j7nazg60e/BFAC-banner.png?dl=1)

BFAC (Backup File Artifacts Checker) is an automated tool that checks for backup artifacts that may disclose the web-application's source code. The artifacts can also lead to leakage of sensitive information, such as passwords, directory structure, etc.

**The goal of BFAC is to be an *all-in-one tool* for backup-file artifacts black-box testing.**

## Usage

| Description                                               | Command                                                                     |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| Help                                                      | `bfac --help`                                                               |
| Check a single URL                                        | `bfac --url http://example.com/test.php`                                    |
| Check a list of URLs                                      | `bfac --list testing_list.txt`                                              |
| Single URL with a different level (level 2 for example)   | `bfac --url http://example.com/test.php --level 2`                          |
| Single URL while specifying values for valid status codes | `bfac --url http://example.com/test.php --valid-status-codes 200,302`       |
| Single URL and showing only the results                   | `bfac --no-text --url http://example.com/test.php`                          |
| Limit the test to exposed DVCS tests                      | `bfac --dvcs-test --url http://example.com/`                                |
| Verify existence of files using Content-Length checks only| `bfac --verify-file-availability content_length http://example.com/test.php`|
| Verify existence of files using Status-Code checks only   | `bfac --verify-file-availability status_code http://example.com/test.php`   |
| Exclude results with specific status-codes                | `bfac --exclude-status-codes 301,999 http://example.com/test.php`           |

## Using BFAC as a module
```
import bfac

testing_level = 4
BFA_URLS = bfac.Generate_BFA_URLs('http://example.com/test.php', testing_level=testing_level)  # Returns a list of BFA patterns for http://example.com/test.php

BFA_Testing_Result = bfac.Test_URL('http://example.com/test.php', testing_level=testing_level)  # Performs BFA testing using BFAC, and returns a list of findings, if any. If nothing is identified, it returns an empty list.

```

## Requirements
* Python2 or Python3
* requests

## Installation [Optional]
`sudo python setup.py install`

## Compatibility
The project currently supports all platforms that run Python.
The project is compatible with both Python 2 and Python 3.

## Community Contribution
Contribution from the community to the BFAC project is very welcome. If you find a bug, have an idea for a feature, ideas to reconstruct the code to work better, or anything else, feel free to submit an issue or a pull request.

### Using the issue tracker 💡

The issue tracker is the preferred channel for bug reports and features requests. 

[![GitHub issues](https://img.shields.io/github/issues/mazen160/bfac.svg?style=flat-square)](https://github.com/mazen160/bfac/issues)


## Legal Disclaimer
This project is made for educational and ethical testing purposes only. Usage of BFAC for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## License
The project is currently licensed under GNU GPLv3.0 License.

## Author
*Mazin Ahmed*
* Website: [https://mazinahmed.net](https://mazinahmed.net)
* Email: *mazin AT mazinahmed DOT net*
* Twitter: [https://twitter.com/mazen160](https://twitter.com/mazen160)
* Linkedin: [http://linkedin.com/in/infosecmazinahmed](http://linkedin.com/in/infosecmazinahmed)

