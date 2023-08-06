import os
import requests
import traceback
import hashlib
import zipfile
from tqdm import tqdm
import json
from . import utils

def compute_file_md5(file):

    cache_md5 = file + ".md5sum"
    if os.path.exists(cache_md5):
        with open(cache_md5, "r") as f:
            return f.read()

    handle = hashlib.md5()
    with open(file, "rb") as f:
        while True:
            b = f.read(1024 * 64)
            if len(b) == 0:
                break
            handle.update(b)
    
    output = handle.hexdigest().upper()
    with open(cache_md5, "w") as f:
        f.write(output)
    return output


def request_text(url):
    data = request_data(url)
    if data is None:
        return None

    text = str(data, encoding="utf-8")
    jdict = json.loads(text)
    if jdict["status"] == "success":
        return jdict["data"]
    
    utils.gprint("Request text failed: ", jdict["message"])
    return None


def request_file(url, file, title):
    
    try:
        chunk_kb_size = 1024
        response   = requests.get(url, stream=True)
        if response.status_code != 200:
            if response.status_code == 404:
                utils.gprint(f"Not found.")
                return False, "NotFound"

            jdict = json.loads(response.content)
            utils.gprint(f"Download failed: {jdict['message']}")
            return False, "Failed"

        content_iter = response.iter_content(chunk_size=chunk_kb_size)
        if "Content-Length" in response.headers:
            content_length = int(response.headers["Content-Length"])
            block_count = int((content_length + chunk_kb_size - 1) / chunk_kb_size)
        else:
            content_length = None
            block_count = None
        
        bar_format = "{l_bar}|{bar}|{n_fmt} KB/{total_fmt} KB {elapsed}<{remaining}"
        pbar = tqdm(content_iter, total=block_count, desc=title, bar_format=bar_format)
        with open(file, "wb") as fout:
            handle = hashlib.md5()
            for ib in pbar:
                fout.write(ib)
                handle.update(ib)

        with open(file + ".md5sum", "w") as f:
            f.write(handle.hexdigest().upper())
        return True, "Updated"
    except Exception as e:
        traceback.print_exc()
    return False, "Failed"


def request_data(url):
    try:
        response   = requests.get(url, stream=True)
        if response.status_code != 200:
            if response.headers["Content-Type"].find("application/json") != -1:
                jdict = json.loads(response.content)
                utils.gprint(f"Request failed: {jdict['message']}")
            else:
                utils.gprint(f"Request failed: {response.content}")
            return None

        return response.content
    except Exception as e:
        traceback.print_exc()
        return None


def require_file_and_check_md5(url, md5url, file, title, update=False, verbose=False):
    try:
        root_dir = os.path.realpath(os.path.dirname(file))
        os.makedirs(root_dir, exist_ok=True)

        if os.path.exists(file) and not update:
            meta = json.load(open(file + ".info", "r"))
            if os.path.getsize(file) == meta["size"]:
                utils.vprint(f"File already download at {file}")
                return True, meta, "Cached"
            else:
                utils.gprint(f"Found a broken package file {file}, I will remove it.")
                os.remove(file)

        if verbose:
            utils.gprint("Send an http request to check the file has been updated...")

        remote_info = request_text(md5url)
        if remote_info is None:
            if verbose:
                utils.gprint(f"Can not request remote info from url: {md5url}")
            return False, None, "Failed"

        if verbose:
            utils.gprint(f"Dump info to: {file}.info")

        json.dump(remote_info, open(file + ".info", "w"), ensure_ascii=True, indent=4)
        if os.path.exists(file):
            local_md5 = compute_file_md5(file)
            remote_md5 = remote_info["md5"]
            if remote_md5 == local_md5:
                # MD5 matched
                if verbose:
                    utils.gprint(f"File already download at {file}, because the MD5 is matched.")
                return True, remote_info, "Cached"

        ok, state = request_file(url, file, title)
        return ok, remote_info, state
    except Exception as e:
        traceback.print_exc()
        return False, None, "Failed"


def extract_zip_to(file, to, verbose=True):
    zfile = zipfile.ZipFile(file)
    members = zfile.namelist()
    if verbose:
        pbar = members
    else:
        pbar = tqdm(members)

    for member in pbar:
        if not verbose:
            pbar.set_description(f"Unzip {member}")

        zfile.extract(member, to)
        if verbose:
            utils.gprint(f"Extract file {os.path.join(to, member)}")
    return members