## Testing QGIS Scripts

[![LICENSE](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/pernlofgren/qgis-plugin-testing/blob/master/LICENSE)

This repo has been set up as a resource for automated testing of QGIS plugins.


### Unittest



### Local Testing

Test script can be run from your QGIS Python Consule, by calling `run_tests()`


### Travis Continuous Integration

Thanks to [Boundless QGIS Testing Environment](https://boundlessgeo.com/2016/07/qgis-continuous-integration-testing-environment-for-python-plugins/), testing inside a real QGIS session via a docker container is now possible!


The `.travis.yml` file in this repo customizes the steps for the testing environment and tells Travis what to do. All the steps are well documented in the Travis CI documentation, and all thats needed to trigger a new build is to add .travis.yml, commit and push to the remote repo. In this example, builds only get triggered on commits on master branch.


### Resources

- [Travis CI](https://docs.travis-ci.com/)
- [Boundless](https://github.com/boundlessgeo/qgis-testing-environment-docker)
- [Unittest docs](https://docs.python.org/2/library/unittest.html)
- [Script Assistant Plugin](https://github.com/linz/qgis-scriptassistant-plugin)

#### Other Resource Repositories

- [qgis-script-testing](https://github.com/pernlofgren/qgis-script-testing)

### Things to note

- The .travis.yml file is read from the root of the repository
- Travis only runs builds on the commits you push after you’ve enabled the repository in Travis CI.
