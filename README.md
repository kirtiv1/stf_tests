This repository contains code that shows how to run STF tests against StreamSets Control Hub 3.x

### Pre-requisites
* [Python 3.4+](https://docs.python.org/3/using/index.html) and pip3 installed
* StreamSets Test Framework [installed](https://streamsets.com/documentation/stf/latest/installation.html) 
* [Access to StreamSets Control Hub](https://streamsets.com/documentation/controlhub/latest/help/controlhub/UserGuide/OrganizationSecurity/OrgSecurity_Overview.html#concept_q5z_jkl_wy) with an user account in your  organization 
* At least one [StreamSets Data Collector](https://streamsets.com/products/dataops-platform/data-collector/) instance registered with the above StreamSets Control Hub instance
and has a label = 'stf-3'

1. Set up the following environment variables:

SCH_PASSWORD,

SCH_USERNAME,

SCH_URL,

SCH_SDC_URL - This corresponds to the above StreamSets Data Collector.

2. Clone this branch of repo. Say the path on the system, after the cloning is $PATH/stf_tests

### Run tests
1. Change to a directory where tests exist

```cd $PATH/stf_tests```

2. Run the following command

```
stf --docker-image streamsets/testframework:3.x test -vs \
 --sch-server-url "${SCH_URL}" \
 --sch-username "${SCH_USERNAME}" \
 --sch-password "${SCH_PASSWORD}" \
 --sch-authoring-sdc "${SCH_SDC_URL}" \
 test_simple_entities.py
 ```


