<!-- This README template is inspired by othneildrew's Best-README-Template repo avaible at : https://github.com/othneildrew/Best-README-Template/tree/master
-->
[![build](https://github.com/adrienpra/Template_Python/actions/workflows/build.yml/badge.svg?event=push)](https://github.com/adrienpra/Template_Python/actions/workflows/build.yml)    [![license](https://img.shields.io/badge/license-MIT-purple)](https://www.python.org/downloads/release/python-3110/)    [![python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/release/python-3110/)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.python.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png" alt="Python_logo" width="500">
  </a>
</div>

# project_name

<!-- ABOUT THE PROJECT -->
## About The Project

_Here's a blank template to get started. Give a short description of the project._

### Built With

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Poetry](https://python-poetry.org/) (venv)
- [Pytest](https://docs.pytest.org/en/7.4.x/index.html) (tests)
- [Coverage](https://coverage.readthedocs.io/en/7.4.1/) (tests)
- [Sphinx](https://www.sphinx-doc.org/en/master/index.html) (docs)
- [GitHub Actions](https://github.com/features/actions) (ci/cd)

<!-- GETTING STARTED -->
## Getting Started

_This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps._

### Prerequisites

- [miniconda](https://docs.conda.io/projects/miniconda/en/latest/)

### Installation

1. Clone project repo
    ```sh
    $ git clone https://github.com/adrienpra/Template_Python.git
    ```

2. Create virtual environnement named template from .yml 
    ```sh
    $ conda env create -f environment.yml
    ```

3. Install pyhton dependencies and build project wheel
    ```sh
    $ conda activate template
    $ poetry install
    ```
4. Install specific group dependencies
    ```sh
    $ poetry install --only docs,tests,deploy
    ```

### Docs
1. Generate docs
    ```sh
    $ ./docs/make html
    ```

2. Docs' available at `.\docs\_build\html\index.html`

### Tests
1. Run tests
    ```sh
    $ cd ./tests/
    $ pytest --cov
    $ coverage html
    ```
2. Tests' coverage available at `.\tests\htmlcov\index.html`

## Additional informations

<!-- USAGE EXAMPLES -->
### Usage

_Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources._

For more examples, please refer to the documentation.

### Commit messages

[Freecodecamp](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/) tutorial on how to write better commit messages.

<!-- ROADMAP -->
### Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

<!-- LICENSE -->
### License

This project is released under the [MIT License](LICENSE).

<!-- CONTACT -->
### Contact

Your Name - name.surname@mail.com

Project Link: [https://github.com/adrienpra/Template_Python](https://github.com/adrienpra/Template_Python)

<!-- ACKNOWLEDGMENTS -->
### Acknowledgments

 - 
 - 
 - 
