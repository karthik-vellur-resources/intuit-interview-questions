# Contributing

This repository is built entirely by the community of assessors at Intuit. We strongly encourage you to contribute problems/questions, and we have provided these guidelines to keep things organized.

## Content

### Samples

Please see the question samples here before contributing a question of your own.

[Template](Contributing/question_template.md)

[Sample](Contributing/sample.md)

### Tagging

At the end of the template, there is a section for tagging. These tags help other assessors find questions when they are 
conducting interviews. Please ensure that your question is filed appropriately in the correct location and also tag your 
question with relevant tags, which will help make it searchable in github pages. Especially important are the #phonescreen or #onsite 
tags. At least one of those should be included, and both if appropriate.

## How to Contribute

### Process

1. Fork this repository
1. Create a new branch
1. Copy the [template file](Contributing/question_template.md) and populate it with your question.
1. If the question requires referncing external files such as static content, then follow the steps [here](Contributing/external_files.md).
1. Edit the mkdocs.yml file to add the path to your new content.
1. Open a Github Pull Request into this repository's master branch
1. Submit the PR to be review by the appropriate domain [team](https://github.intuit.com/orgs/poolhiring/teams). If you aren't sure which team to tag, you can tag `a4a-superadmin` team to review your PR.
1. Once you have an approval, feel free to squash and merge your commits.


### PR Approvals

This repository is using the CODEOWNERS file which manages who can approve pull requests into specific parts of the repository.
This has been broken down by folders in the docs which map to different domain areas in Software Engineering.
Each domain area is managed by a separate [team](https://github.intuit.com/orgs/poolhiring/teams).

## Structural Changes

### I Would Like to be Added as an Approver

Reach out to the relevant [team](https://github.intuit.com/orgs/poolhiring/teams). Send a note to the members of the 
team, and they can consider you for inclusion.

### What if I Need to Add/Change Domains?

1. Please reach out to the administrators of this repository
1. If this is approved, a new team will be created for you, and you will be made an admin of that team.
1. Open a pull request with the new folder and at least one question. 
1. Make sure there are at least 3 people in the team other than yourself. 
1. With great power comes great responsibility.


## Updating content

* For each question, create/edit markdown files in the [docs](./docs) directory. Follow the naming convention as shown below

Type of Files | Directory to Store them in
------------ | -------------
Backend | [docs/backend](./docs/backend)
Backend -> TPI | [docs/backend/tpi](./docs/backend/tpi)
Backend -> Craft | [docs/backend/craft](./docs/backend/craft)

* If a question has more than one file (for example: test data, images), create a directory for that question.

* Edit [mkdocs.yml](./mkdocs.yml) to update navigation structure to add the questions to the correct navigation structure.

## Running Locally

### Install prereqs

* Install Python3, if not already installed. You can check with `which python3`

Run the following commands from the root of this repository:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Build the docs locally
```
mkdocs build
```

### Run the docs server locally
At the root folder of this repo:

```
mkdocs serve
```
Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Publishing the content

1. Create a PR from your branch
2. This repo is being built and published via this [build job](https://build.intuit.com/pool-hiring/blue/organizations/jenkins/interview-questions/). Your PR build should succeed for a merge approval
3. Once the PR is merged, verify that the deployment job succeeded from master.

## Links

1. [Material theme for mkdocs](https://squidfunk.github.io/mkdocs-material/)
2. [mkdocs help](https://www.mkdocs.org/)
