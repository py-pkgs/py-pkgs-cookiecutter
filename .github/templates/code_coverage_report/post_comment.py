#%%

import subprocess
import argparse
import requests
import json
import logging

import markdown
from interrogate import __version__

logger = logging.getLogger("code_coverage_reporter")
handler = logging.StreamHandler()
format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def main(path_to_src: str, endpoint: str, token: str):
    out = subprocess.check_output(
        ["interrogate", "-v", path_to_src]
    )
    out_spl = out.decode('utf-8').split('\n')
    out_spl[-2] = out_spl[-2].replace('-', '').strip().replace("RESULT:", "**RESULT**:")
    del out_spl[-4]
    out_spl = "\n".join(out_spl[2:])
    table = markdown.markdown(out_spl, extensions=["markdown.extensions.tables"])
    msg = f"""<h3>Docstring coverage</h3>  
    Report generated with <a href="https://interrogate.readthedocs.io/en/latest/">interrogate</a>=={__version__}<br/>
    {table}"""
    body={"body": msg}
    r = requests.post(
        url=endpoint,
        headers={
            'Authorization': f'token {token}'
        },
        data=json.dumps(body)
    )
    r.raise_for_status()
    

if __name__=="__main__":
    parser=argparse.ArgumentParser(
        prog="CodeCoverageReporter",
        description="Use this in GH actions to post the results of interrogate code coverage <https://github.com/econchick/interrogate> to a PR as a comment"
    )
    parser.add_argument('path_to_src', type=str)
    parser.add_argument('github_repository', type=str)
    parser.add_argument('pr_number', type=str)
    parser.add_argument('token', type=str)
    args=parser.parse_args()
    endpoint=f'https://api.github.com/repos/{args.github_repository}/issues/{args.pr_number}/comments'
    main(args.path_to_src, endpoint, args.token)
