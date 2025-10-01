# MORCoRA

MORCoRA is search-based refactoring tool for recommending refactoring operations towards a target repository snapshot.

It based on multi-objective evolutionary algorithm (MOEA), the refactorings recommended achieve 3 objectives:
1. Improving code quality
2. Preserving semantic coherence
3. Preserving high review availability


## Requirement
python 3.8 and later

## Build
1. **Clone this repository and install dependencies**

```
$ git clone https://github.com/MashiroCl/MORCOpy
$ cd MORCOpy
$ pip install -r requirements.txt
```
note: you can find jmetalpy [here](https://github.com/jMetal/jMetalPy), download the [jmetal 1.5.7 package](https://github.com/jMetal/jMetalPy/releases/tag/v1.5.7), and use pip to install it.


2. **Creating a personal access token**

MORCoRA uses the GitHub API, it needs the personal access token to extract pull requests.

For how to get personal access token, please refer to [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

3. **Set the token as a environment variable**

After you get the token, set it as an environment variable, and named the variable as **MORCORE**

For MacOS:
```
$ echo "export MORCORE=<personal-access-token>" >> ~/.bash_profile
$ source ~/.bash_profile
```

For Linux:
```
export MORCORE=<personal-access-token>
```


## Run
1. Extract abstract representation and call graph for the target repository snapshot.

Required: <repo_path>: cloned repository path <repo_url>: GitHub url for the repository

```
$ python3 command.py -r <repo_path> -u <repo_url> -m extract
```

The extracted data are stored in `<repo_path>/MORCoRE/`

2. Fill in `config.txt` with the parent directory of the target repository, e.g. `<repo_path>=/A/B/C/repo_name`, fill the `config.txt` with `/A/B/C/`

3. Search refactoring sequences
```
$ python3 command.py -n <repo_name> -i <max_evaluation_number> -p customize -m search_customize
```


## Publications
The following article include the details of MORCoRA.

Lei Chen, Shinpei Hayashi. [MORCoRA: Multi-Objective Refactoring Recommendation Considering Review Availability](https://www.worldscientific.com/doi/10.1142/S0218194024500438).International Journal of Software Engineering and Knowledge Engineering, vol. 34, no. 12, pp. 1919-1947. dec, 2024. 

📖 [Read on arXiv](https://arxiv.org/abs/2408.06568)

```
@article{
  title={An Empirical Study on the Impact of Change Granularity in Refactoring Detection},
  journal={Journal of Systems and Software},
  volume = {231},
  pages = {112608},
  year = {2026},
  issn = {0164-1212},
  author = {Lei Chen and Shinpei Hayashi},
}
```
