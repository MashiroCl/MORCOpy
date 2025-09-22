import pathlib
from pathlib import Path

def extract_local(repo_path, repo_url):
    command = f"python3 command.py -r {repo_path} -u {repo_url} -m extract"
    print(command)


def run(repo_name, iteration, platform, output_num):
    command = f"nohup python3 command.py -m search_{platform} -n {repo_name} -i {iteration} -p {platform} -d {output_num} >command_log/{repo_name}{output_num}.out 2>&1 &"
    # command = f"python3 command.py -m search_{platform} -n {repo_name} -i {iteration} -p {platform} -d {output_num}"
    return command


def upload(repo_name, platform):
    command = "No proper platform"
    if platform == "titan":
        command = f"scp -r /Users/leichen/data/MORCoRA/{repo_name}/MORCoRE/csv " \
                  f"chenlei@titan:/home/salab/chenlei/MORCoRA/dataset/{repo_name}/csv"
    elif platform == "thor":
        command = f"scp -r /Users/leichen/data/MORCoRA/{repo_name}/MORCoRE/csv " \
                  f"chenlei@thor:/home/salab/chenlei/project/MORCoRA/dataset/{repo_name}/csv"
    print(command)


def upload_expertise_table(repo_name, platform):
    command = "No proper platform"
    if platform == "titan":
        command = f"scp /Users/leichen/experiement_result/MORCoRA/infos/{repo_name}/csv/expertise_table.csv " \
                  f"chenlei@titan:/home/salab/chenlei/MORCoRA/dataset/{repo_name}/csv/expertise_table.csv"
    elif platform == "thor":
        command = f"scp /Users/leichen/experiement_result/MORCoRA/infos/{repo_name}/csv/expertise_table.csv " \
                  f"chenlei@thor:/home/salab/chenlei/project/MORCoRA/dataset/{repo_name}/csv/"
    print(command)

def download_csv(repo_name):
    p = pathlib.Path(f"/Users/leichen/experiement_result/MORCoRA/infos/{repo_name}")
    p.mkdir(parents=True)
    command = f"scp -r chenlei@titan:/home/salab/chenlei/MORCoRA/dataset/{repo_name}/csv " \
              f"/Users/leichen/experiement_result/MORCoRA/infos/{repo_name}/csv"
    print(command)


def download(repo_name, platform):
    command = "No proper platform"
    if platform == "titan":
        for i in range(1, 6):
            p = Path(f"/Users/leichen/experiement_result/MORCoRA/{repo_name}/titan/1/output{i}")
            p.mkdir(parents=True, exist_ok=True)
            command = f"scp -r chenlei@titan:/home/salab/chenlei/MORCoRA/dataset/{repo_name}/output{i}/{repo_name}/\* " \
                      f"/Users/leichen/experiement_result/MORCoRA/{repo_name}/titan/1/output{i}/"
            print(command)
    elif platform == "thor":
        for i in range(1,6):
            p = Path(f"/Users/leichen/experiement_result/MORCoRA/{repo_name}/thor/1/output{i}")
            p.mkdir(parents=True, exist_ok=True)
            command = f"scp -r chenlei@thor:/home/salab/chenlei/project/MORCoRA/dataset/{repo_name}/output{i}/{repo_name}/\* " \
                      f"/Users/leichen/experiement_result/MORCoRA/{repo_name}/thor/1/output{i}"
            # command = f"scp -r chenlei@thor:/home/salab/chenlei/project/MORCoRA/dataset/{repo_name}/output{i}/{repo_name}/VAR.NsgaiiRE " \
            #           f"/Users/leichen/experiement_result/MORCoRA/{repo_name}/thor/1/output{i}"
            print(command)


def make_dirs(repo_name):
    command = f"mkdir {repo_name}"
    print(command)


if __name__ == "__main__":
    data_base_root = "/Users/leichen/data/MORCoRA/"
    repo_info = {
        "auto": (data_base_root + "auto", "https://github.com/square/dagger", 22500),
        "mockito": (data_base_root + "mockito", "https://github.com/mockito/mockito", 51300),
        "retrofit": (data_base_root + "retrofit", "https://github.com/square/retrofit", 116500),
        "lottie-android": (data_base_root + "lottie-android", "https://github.com/airbnb/lottie-android", 29000),
        "glide": (data_base_root + "glide", "https://github.com/bumptech/glide", 142800),
        "disruptor": (data_base_root + "disruptor", "https://github.com/LMAX-Exchange/disruptor", 44000)
    }

    # extract abs & workload_expertise local
    # for each in repo_info.keys():
    #     extract_local(repo_info[each][0], repo_info[each][1])

    # upload
    # platform = "titan"
    # platform = "thor"
    # for repo in repo_info.keys():
            # upload(repo, platform)
            # upload_expertise_table(repo, platform)
        # make_dirs(repo)

    # run
    # platform = "thor"
    # platform = "titan"
    # for repo in repo_info.keys():
    #     for output_num in range(1, 6):
    #         print(run(repo, repo_info[repo][2], platform, output_num))


    # download
    # platform = "titan"
    platform  = "thor"
    # for repo in ["auto", "lottie-android", "disruptor", "mockito", "retrofit", "glide"]:
    for repo in ["glide"]:
        download(repo, platform)



    # for repo in repo_info.keys():
    #     download_csv(repo)