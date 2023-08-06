# argus-api

`argus-api` is the python API client library for the Argus API.

Complete documentation for this project can be found at: [argus-api documentation](https://argus-api.dev-docs.mnemonic.no)

This repository is maintained by the [tooling team](https://wiki.mnemonic.no/display/DEV/Tooling+Team)


## prerequisites

 - a python `3.6` (or higher) interpreter (**warning :** python `3.6` support will be discontinued soon)

for development:

 - [poetry](https://python-poetry.org/) `1.3` or higher
 - A user in the [argus test system](https://osl-argusdev-portal1.mnemonic.no/)
  - An API key with the relevant permissions

## processes

### requesting changes

To request a change in this repository, create an
[ARGUSUSER ticket in JIRA](https://jira.mnemonic.no/secure/CreateIssue.jspa?pid=11342&issuetype=4),
using the label `tooling` and component `tools/argus-api`.

See [existing JIRA tickets for this project](https://jira.mnemonic.no/issues/?jql=project%20in%20(ARGUSUSER%2C%20ARGUS)%20and%20component%20%3D%20%22tools%2Fargus-api%22%20%20and%20status%20not%20in%20(Done%2C%20Deployed%2C%20Rejected%2C%20Closed))

### contributing

- Re-generation of the package must follow the procedure described in the
  [argus-api-generator documentation](http://argus-api-generator.dev-docs.mnemonic.no/)
- All changes must be submitted as a PR towards the
  [argus-api repository in gitlab](https://gitlab.mnemonic.no/development/tooling/argus-api)
- All commits must be tagged with the correct JIRA ticket and use the
  [conventional commits](https://www.conventionalcommits.org) format
- All changes must be reflected in the project documentation
- All PRs be built successfully before merging.
- All changes must be reviewed and approved by one of the maintainers.
- Non-trivial changes SHOULD be reviewed by two individuals. This is not enforced,
  and is up to the author to decide.
- Any emergency changes MUST be documented properly in the associated JIRA ticket.


## build and deployment

### build process

The package and documentation are built in gitlab on each merge to the `master` branch:

 - the package is built with poetry
 - the documentation is built with sphinx

### deployment process

Deployment occurs on each merge to the `master` branch and after the build:

 - the package is uploaded to pypi with poetry
 - the documentation is uploaded twice:
   - to `osl-devdocs1.mnemonic.no` for internal documentation
   - to `osl-docweb1.mnemonic.no` for public documentation 
