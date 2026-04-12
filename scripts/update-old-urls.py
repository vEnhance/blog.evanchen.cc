from pathlib import Path
import json
import sys

CACHE_PATH = Path("~/.cache/blog.evanchen.cc/").expanduser()

with open(CACHE_PATH / "REDIRECTS.json") as f:
    redirect_dict = json.load(f)

for filename in sys.argv[1:]:
    out = ""
    with open(filename) as f:
        for line in f:
            for k, v in redirect_dict.items():
                line = line.replace("blog.evanchen.cc" + k, "blog.evanchen.cc" + v)
            out += line
    with open(filename, "w") as f:
        print(out.strip(), file=f)
