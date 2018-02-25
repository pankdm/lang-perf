
import json
import os
import subprocess


RESULTS_FILE = "results.txt"

RUN_SCRIPTS = {
    "cpp": "./cpp/run.sh",
    "python": "./python/run.sh",
    "python3": "./python/run_python3.sh",
    "kotlin": "./kotlin/run.sh",
    "kotlin_jit": "./kotlin/run_jit.sh",
    "kotlin_jit_5": "./kotlin/run_jit_5.sh",
    "cython_bfs": "./cython/run.sh",
    "cython_full": "./cython/run_full.sh",
}


def extract_tags(lines):
    result = {}
    for line in lines.split('\n'):
        if "=" in line:
            k, v = line.split("=")
            result[k] = v
    return result


def run_benchmark(name, map_name):
    path = 'txt-maps/{}'.format(map_name)
    script = RUN_SCRIPTS[name]
    stdout = subprocess.check_output([script, path])
    tags = extract_tags(stdout)
    tags['map'] = map_name
    tags['name'] = name
    print(tags)
    return tags


def write_to_file(data):
    f = open(RESULTS_FILE, 'a')
    f.write(json.dumps(data) + '\n')
    f.close()


def get_map_tags(map_name):
    f = open('maps/{}'.format(map_name.replace(".txt", ".json")))
    data = json.load(f)
    return {
        'nodes': len(data['sites']),
        'edges': len(data['rivers']),
    }


def all_benchmarks():
    # clean the file
    f = open(RESULTS_FILE, 'w')
    f.close()

    files = os.listdir('txt-maps/')
    # files = [
    #     'edinburgh-10000.txt',
    #     'icfp-coauthors-pj.txt',
    #     'vancouver.txt',
    #     'oxford-10000.txt',
    # ]
    for f in reversed(files):
        print('')
        map_tags = get_map_tags(f)
        print('{} -> {}'.format(f, map_tags))
        for name in sorted(RUN_SCRIPTS.keys()):
            tags = run_benchmark(name, f)
            tags.update(map_tags)
            write_to_file(tags)


all_benchmarks()
# run_benchmark('kotlin_jit', 'gothenburg-sparse.txt')
