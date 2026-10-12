#!/usr/bin/env python3

print("\033[0;37m                                    \033[0;92m▀\033[0;92;42m▓██\033[0;92m▀\033[0;37m                                   \033[0m")
print("\033[0;37m                                     \033[0;92;42m▒█\033[0;92m▌\033[0;37m                                    \033[0m")
print("\033[0;37m \033[0;92m▄▄■▀\033[0;92;42m▓\033[0;92m▄▄\033[0;37m   \033[0;92m▄■\033[0;37m  \033[0;92m▐█▄■███\033[0;37m \033[0;92m▀▀■▄\033[0;37m      \033[0;92m▄\033[0;37m \033[0;92m■\033[0;37m \033[0;92;42m░\033[0;92m█▌\033[0;37m   \033[0;92m▄▄▀▀▄▄\033[0;37m    \033[0;92m▄▄\033[0;37m      \033[0;92m▄\033[0;37m   \033[0;92m███\033[0;37m \033[0;92m▀▀■▄\033[0;37m   \033[0m")
print("\033[0;92m▐▓\033[0;92;42m█\033[0;37m  \033[0;92m▀█▄▌\033[0;37m \033[0;92;42m▓█\033[0;92m█\033[0;37m   \033[0;92;42m█\033[0;92m█▌\033[0;92;42m▓\033[0;92m██▌\033[0;37m   \033[0;92m▐█▄\033[0;37m \033[0;92m▄█▀\033[0;37m     \033[0;92m█▌\033[0;37m  \033[0;92;42m▓█\033[0;92m▀\033[0;37m   \033[0;92;42m█\033[0;92m█\033[0;37m  \033[0;92m█▀\033[0;92;42m▓\033[0;37m      \033[0;92m▐██▄\033[0;92;42m▓\033[0;92m██▌\033[0;37m   \033[0;92m▐█▄\033[0;37m \033[0m")
print("\033[0;37m  \033[0;92m▀▀■\033[0;90m■▄▄\033[0;37m \033[0;92;42m▒\033[0;92m▀\033[0;92;42m█\033[0;92m▌\033[0;37m   \033[0;92m▐▀▌\033[0;90m▄\033[0;92m▀█\033[0;37m     \033[0;92;42m▓\033[0;92m▀\033[0;37m \033[0;90m▄\033[0;92m▀\033[0;37m     \033[0;90m█▄\033[0;92m▀\033[0;37m \033[0;92;42m▒\033[0;92m▀\033[0;92;42m█\033[0;92m▌\033[0;37m   \033[0;92m▐▀▌▀\033[0;90m▄\033[0;90;47m█\033[0;90m▌\033[0;37m   \033[0;90m■\033[0;37m  \033[0;90m▄\033[0;92m▀\033[0;92;42m▒\033[0;92m▀\033[0;90m▄\033[0;92m▀█\033[0;37m     \033[0;92;42m▓\033[0;92m▀\033[0;37m \033[0m")
print("\033[0;90m▄█▄\033[0;37m   \033[0;90m▐█▌▄\033[0;90;47m▓\033[0;90m▄▀\033[0;37m   \033[0;90m▄▓▀▐\033[0;90;47m▓\033[0;90m▄▌\033[0;37m    \033[0;90m▄▓▌▀█▌\033[0;37m   \033[0;90m▐██\033[0;90;47m▓\033[0;37m \033[0;90m▄\033[0;90;47m▓\033[0;90m▄▀\033[0;37m   \033[0;90m▄▓▀▐\033[0;90;47m█\033[0;90m█▓\033[0;37m  \033[0;90m▄█\033[0;37m  \033[0;90;47m█\033[0;90m█▄▌▐\033[0;90;47m▓\033[0;90m▄▌\033[0;37m    \033[0;90m▄▓▌\033[0m")
print("\033[0;90m▀██▓▄■▀▀\033[0;37m  \033[0;90m▀\033[0;90;47m▓\033[0;90m██▄■\033[0;37m   \033[0;90m▐█▓▌\033[0;37m   \033[0;90m▄█▀\033[0;37m   \033[0;90m▀■▄▄\033[0;37m \033[0;90m▓██▄\033[0;37m \033[0;90m▀\033[0;90;47m▓\033[0;90m██▄■\033[0;37m    \033[0;90m▀██▄■▀\033[0;37m \033[0;90m■▄██▓▀▐█▓▌\033[0;37m   \033[0;90m▄█▀\033[0;37m \033[0m")
print("\033[0;37m                        \033[0;90m■▀\033[0;37m                                            \033[0;90m■▀\033[0;37m    \033[0m")

import argparse
import hashlib
import os
import sys
import datetime
import pwd
import grp
import fcntl
import array
import math
from collections import Counter
from pathlib import Path

# i hate windows
if os.name == "nt":
    print("[-] Error: This only works on Posix-like systems. And Windows sucks anyways.")
    print("I regret nothing.")
    sys.exit(1)

# Magic Signatures Map
MAGIC_SIGNATURES = {
    b'\x7fELF': ("ELF Executable (Linux Binary)", True),
    b'\x89PNG\r\n\x1a\n': ("PNG Image File", False),
    b'\xff\xd8\xff': ("JPEG Image File", False),
    b'%PDF': ("PDF Document", False),
    b'PK\x03\x04': ("ZIP Archive / Modern Office Doc (Docx/Xlsx)", False),
    b'MZ': ("Windows Executable (EXE/DLL) - Suspicious on Linux", True),
    b'#!': ("Executable Script (Shebang Line)", True)
}

FOOTER_SIGNATURES = {
    "PNG Image File": b'\x49\x45\x4e\x44\xae\x42\x60\x82',
    "JPEG Image File": b'\xff\xd9',
    "PDF Document": b'%%EOF'
}

def snatch_sha256(file_path):
    try:
        hasher = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return "Could not read file"

def detect_real_file_type(file_path):
    try:
        with open(file_path, "rb") as f:
            header = f.read(8)
        for signature, (file_type, strict_zero) in MAGIC_SIGNATURES.items():
            if header.startswith(signature):
                return file_type
        return "Unknown Data / Plain Text"
    except Exception:
        return "Could not read magic bytes"
# i genuinely HATED MAKING THIS.
# Is it necessary? A lot of sources say so.
# but GOD dude this made me tweak. I am fine with doing basic math, which this is, but wow.
# Interestingly enough, it apparently works well, i gave it a meterpreter msfvenom file and entropy...
# it hit about a 6 i believe. When encoded, an 8.
def calculate_entropy(file_path):
    try:
        byte_counts = Counter()
        total_bytes = 0
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                byte_counts.update(chunk)
                total_bytes += len(chunk)
        if total_bytes == 0:
            return 0.0
        entropy = 0.0
        for count in byte_counts.values():
            probability = count / total_bytes
            entropy -= probability * math.log2(probability)
        return round(entropy, 4)
    except Exception:
        return "Could not calculate"
# google was my best friend here, for finding the masks
def get_linux_flags(file_path):
    EXT2_IOC_GETFLAGS = 0x80046601
    FLAG_MASKS = {
        0x00000010: "Immutable (i) - File cannot be modified/deleted",
        0x00000020: "Append-only (a) - Can only open for writing at the end",
        0x00000004: "Compressed (c)",
        0x00000800: "No-Dump (d) - Ignored by backup utilities",
        0x00008000: "Extents utilized (e)"
    }
    try:
        fd = os.open(file_path, os.O_RDONLY)
        buf = array.array('i', [0])
        fcntl.ioctl(fd, EXT2_IOC_GETFLAGS, buf, True)
        os.close(fd)
        flags_raw = buf[0]
        active_flags = []
        for mask, desc in FLAG_MASKS.items():
            if flags_raw & mask:
                active_flags.append(desc)
        return active_flags if active_flags else ["None (Standard File)"]
    except Exception:
        return ["Unavailable (Unsupported or non-ext4 filesystem)"]
# yay a simple one that works without being spaghetti.
# Python was meant to be human readable btw
def get_extended_attributes(file_path):
    try:
        if hasattr(os, "listxattr"):
            attrs = os.listxattr(file_path)
            xattrs = {}
            for attr in attrs:
                try:
                    val = os.getxattr(file_path, attr)
                    xattrs[attr] = val.decode('utf-8', errors='replace')
                except Exception:
                    xattrs[attr] = "<Binary/Unreadable Data>"
            return xattrs if xattrs else {"None": "No extended attributes found"}
    except Exception:
        pass
    return {"Error": "Extended attributes not supported on this mount/OS"}
# OH MY GODDDDDDDDDD THIS ACTUALLY WAS HORRIFIC TO MAKE.
# I DON'T THINK I CAN EXPLAIN WHY I DECIDED THIS WAS NECESSARY.
# IT IS USEFUL, YES, BUT I DID NOT EXPECT IT TO TURN TO *THIS*
# I originally left like 15 comments, but I removed it for clarity (seems backward, but trust me.)
# It works, though...
# I regret nothing.
def carve_raw_device(dev_path, output_dir):
    if os.getuid() != 0:
        print("[-] Run it as root for carving.")
        return
    print(f"[!] Sweeping data stream: {dev_path}")

    CHUNK_SIZE = 4194304
    MAX_FILE_SIZE = 52428800

    try:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        global_offset = 0
        leftover_bytes = b''

        with open(dev_path, "rb") as dev:
            while True:
                raw_chunk = dev.read(CHUNK_SIZE)
                is_final_pass = not raw_chunk

                buffer = leftover_bytes + raw_chunk
                if not buffer:
                    break

                for head_bytes, (name, strict_zero) in MAGIC_SIGNATURES.items():
                    start_pos = buffer.find(head_bytes)
                    while start_pos != -1:
                        absolute_match_offset = global_offset - len(leftover_bytes) + start_pos

                        if strict_zero and absolute_match_offset != 0:
                            start_pos = buffer.find(head_bytes, start_pos + 1)
                            continue

                        foot_bytes = FOOTER_SIGNATURES.get(name, b'')
                        carved_data = b''
                        bytes_to_skip = len(head_bytes)  #step forward if carving fails

                        if foot_bytes:
                            end_pos = buffer.find(foot_bytes, start_pos)
                            if end_pos != -1:
                                carved_data = buffer[start_pos:end_pos + len(foot_bytes)]
                                bytes_to_skip = (end_pos + len(foot_bytes)) - start_pos
                            elif len(buffer) - start_pos > MAX_FILE_SIZE:
                                carved_data = buffer[start_pos:start_pos + MAX_FILE_SIZE]
                                bytes_to_skip = MAX_FILE_SIZE
                        else:

                            fallback_size = 1048576 if name == "Executable" else 51200
                            if len(buffer) - start_pos > fallback_size:
                                carved_data = buffer[start_pos:start_pos + fallback_size]
                                bytes_to_skip = fallback_size
                            else:
                                carved_data = buffer[start_pos:]
                                bytes_to_skip = len(buffer) - start_pos

                        if carved_data:
                            ext = ".png" if "PNG" in name else ".jpg" if "JPEG" in name else ".pdf" if "PDF" in name else ".zip" if "ZIP" in name else ".elf" if "Executable" in name else ".bin"
                            out_file = Path(output_dir) / f"carved_{absolute_match_offset}{ext}"
                            with open(out_file, "wb") as f:
                                f.write(carved_data)
                            print(f" [+] Extracted valid target signature [{name}] at offset {absolute_match_offset} -> {out_file}")

                        # Had to fix here because the spamming bug.
                        # Thank god for wildcards, sudo rm -f *.bin saved me after the bug
                        start_pos = buffer.find(head_bytes, start_pos + bytes_to_skip)

                global_offset += len(raw_chunk)
                leftover_bytes = buffer[-MAX_FILE_SIZE:] if len(buffer) > MAX_FILE_SIZE else buffer

                if is_final_pass:
                    break

    except Exception as e:
        print(f"[-] Carver runtime execution aborted: {e}")


# wow i cannot even begin to explain how easy this was compared to what i thought it would be after making...
# that thing up there...
def dump_proc_mem(pid, output_dir):
    if os.getuid() != 0:
        print("[-] Root privileges (sudo) required to parse raw process memory maps.")
        return
    print(f"[!] Hooking virtual allocations of PID: {pid}")
    try:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        maps_path = f"/proc/{pid}/maps"
        mem_path = f"/proc/{pid}/mem"

        if not os.path.exists(maps_path):
            print(f"[-] Process {pid} does not exist.")
            return

        with open(maps_path, "r") as maps, open(mem_path, "rb", 0) as mem:
            for line in maps:
                parts = line.split()
                if len(parts) < 2:
                    continue
                addr_range = parts[0]
                perms = parts[1]

                if perms.startswith("r") and not parts[-1].startswith("[vvar]"):
                    start, end = [int(x, 16) for x in addr_range.split("-")]
                    try:
                        mem.seek(start)
                        buf = mem.read(end - start)
                        if buf and buf != b'\x00' * len(buf):
                            label = "".join(c for c in parts[-1] if c.isalnum() or c in "._-") if len(parts) > 5 else "anonymous"
                            out_file = Path(output_dir) / f"pid_{pid}_{hex(start)}_{label}.dmp"
                            with open(out_file, "wb") as f:
                                f.write(buf)
                            print(f" [+] Dumped segment {hex(start)}-{hex(end)} ({label})")
                    except Exception:
                        pass
    except Exception as e:
        print(f"[-] Memory dump aborted: {e}")

def dump_live_triage_artifacts():
    print("\n==============================================")
    print("      LIVE OS TRIAGE FOOTPRINT REPORT         ")
    print("==============================================")
    # The indentation looks like PHEN-228's torso
    print("\n[*] Auditing Available Profile Shell Histories:")
    try:
        for user_info in pwd.getpwall():
            home_dir = Path(user_info.pw_dir)
            username = user_info.pw_name
            target_histories = [home_dir / ".bash_history", home_dir / ".zsh_history"]

            for hist_path in target_histories:
                if hist_path.is_file():
                    print(f"  [+] History identified for User [{username}] -> {hist_path.name}")
                    try:
                        with open(hist_path, "r", encoding="utf-8", errors="replace") as h_file:
                            lines = h_file.readlines()[-20:]
                            print(f"    --- Last {len(lines)} Shell Commands ---")
                            for line in lines:
                                print(f"      > {line.strip()}")
                    except Exception as err:
                        print(f"    [-] Read Failure: {err}")
    except Exception as e:
        print(f"  [-] Profile mapping aborted: {e}")

    print("\n[*] Auditing Active System Cron/Task Persistence Frameworks:")
    cron_paths = ["/etc/crontab", "/etc/cron.d", "/var/spool/cron/crontabs"]
    for c_path in cron_paths:
        target = Path(c_path)
        if target.is_file():
            print(f"  [!] System Cron Configuration Found: {target}")
            try:
                with open(target, "r", encoding="utf-8", errors="replace") as f:
                    for line in f:
                        if line.strip() and not line.strip().startswith("#"):
                            print(f"    [Active Task] {line.strip()}")
            except Exception as e:
                print(f"    [-] Read Failure: {e}")
        elif target.is_dir():
            print(f"  [!] Monitoring Directory Matrix: {target}")
            for root, _, files in os.walk(target):
                for file in files:
                    full_cron = Path(root) / file
                    try:
                        with open(full_cron, "r", encoding="utf-8", errors="replace") as f:
                            for line in f:
                                if line.strip() and not line.strip().startswith("#"):
                                    print(f"    [{file}] {line.strip()}")
                    except Exception:
                        pass
    print("==============================================\n")

def dissect(fullpath, show_advanced):
    sha256hash = snatch_sha256(fullpath)
    extension = fullpath.suffix.lower() if fullpath.suffix else "None"
    real_type = detect_real_file_type(fullpath)
    entropy_val = calculate_entropy(fullpath)

    print("\n=== File Dissection Report ===")
    print(f"File Path:     {fullpath}")
    print(f"Extension:     {extension}")
    print(f"True Identity: {real_type}")
    print(f"SHA-256:       {sha256hash}")
    print(f"Data Entropy:  {entropy_val} / 8.0")

    if show_advanced:
        try:
            advanced_stats = fullpath.stat()
            modified_time = datetime.datetime.fromtimestamp(advanced_stats.st_mtime)
            fs_flags = get_linux_flags(fullpath)
            xattrs = get_extended_attributes(fullpath)

            print("\n--- Advanced Filesystem Stats ---")
            print(f"Permissions:   {oct(advanced_stats.st_mode & 0o777)}")
            print(f"Owner User:    {pwd.getpwuid(advanced_stats.st_uid).pw_name} (UID: {advanced_stats.st_uid})")
            print(f"Owner Group:   {grp.getgrgid(advanced_stats.st_gid).gr_name} (GID: {advanced_stats.st_gid})")
            print(f"Last Modified: {modified_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Inode Number:  {advanced_stats.st_ino}")

            print("\n--- Low-Level Kernel / FS Attributes (chattr) ---")
            for flag in fs_flags:
                print(f" [!] {flag}")

            print("\n--- Hidden Extended Attributes (xattr) ---")
            for key, value in xattrs.items():
                print(f" [+] {key}: {value}")
        except Exception as e:
            print(f"\nCould not access advanced metadata: {e}")
    print("==============================")
def resurrect_deleted_executables(output_dir):
    # Horrible to write, no other words.
    # In short, this is literally a Paladin using Lay On Hands.
    # Wrote this while very tired, so left a ton of comments.
    print("\n==============================================")
    print("    GHOST PROCESS HUNT & FILE RESURRECTION    ")
    print("==============================================")
    if os.getuid() != 0:
        print("[-] Root privileges (sudo) required to seize process descriptors.")
        return

    try:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        # Loop through every PID
        for pid_dir in os.listdir("/proc"):
            if pid_dir.isdigit():
                exe_symlink = Path("/proc") / pid_dir / "exe"
                try:
                    if exe_symlink.is_symlink():
                        real_target_path = os.readlink(exe_symlink)

                        # The Linux kernel adds (deleted)
                        if " (deleted)" in real_target_path:
                            print(f" Process [{pid_dir}] is executing from a deleted binary. Most likely malware")
                            print(f"     > Original Path: {real_target_path}")

                            # cmdline for more context
                            cmd_path = Path("/proc") / pid_dir / "cmdline"
                            if cmd_path.is_file():
                                with open(cmd_path, "r") as f:
                                    cmdline = f.read().replace('\x00', ' ').strip()
                                    print(f"     > Spawn Command:  {cmdline}")

                            # cast Lay On Hands and hope for NAT 20
                            recovered_file = Path(output_dir) / f"resurrected_pid_{pid_dir}_deleted.bin"
                            with open(exe_symlink, "rb") as source, open(recovered_file, "wb") as dest:
                                dest.write(source.read())
                            print(f"     Pulled deleted binary out of the void, rolled a 20 -> {recovered_file}")
                except Exception:
                    # usually sockets or threads
                    pass
    except Exception as e:
        print(f"[-] Execution link hunt aborted: {e}")
    print("==============================================\n")

def main():
    parser = argparse.ArgumentParser(description="Deep Forensic File and Directory Dissector")
    parser.add_argument("target", nargs="?", default=None, help="File/directory path or block device destination.")
    parser.add_argument("-a", "--advanced", action="store_true", help="Show deep, low-level filesystem stats.")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively crawl directories if target is a folder.")
    parser.add_argument("-c", "--carve", action="store_true", help="Carve raw block targets for deleted evidence clusters.")
    parser.add_argument("-m", "--memdump", type=int, metavar="PID", help="Dump absolute virtual runtime memory segments of a process.")
    parser.add_argument("-t", "--triage", action="store_true", help="Scrape active system artifacts (Cron infrastructure & Profile History footprints).")
    parser.add_argument("-o", "--output", default="forensic_output", help="Directory destination for carved assets or memory segments.")

    args = parser.parse_args()

    if args.triage:
        dump_live_triage_artifacts()
        # I cast Lay On Hands!
        resurrect_deleted_executables(args.output)
        if not args.target:
            sys.exit(0)

    if args.memdump:
        dump_proc_mem(args.memdump, args.output)
        sys.exit(0)

    if not args.target:
        print("Error: Target path parameter or execution flag required.")
        sys.exit(1)

    if args.carve:
        carve_raw_device(args.target, args.output)
        sys.exit(0)

    target_path = Path(args.target)
    if not target_path.exists():
        print(f"Error: '{args.target}' does not exist.")
        sys.exit(1)



    if target_path.is_file():
        dissect(target_path, args.advanced)
    elif target_path.is_dir():
        if args.recursive:
            print(f"Initiating recursive crawl on directory: {target_path.resolve()}")
            for root, _, files in os.walk(target_path):
                for file in files:
                    current_file_path = Path(root) / file
                    if current_file_path.is_file():
                        dissect(current_file_path, args.advanced)
        else:
            print(f"Error: '{args.target}' is a directory. Use -r or --recursive to parse it.")
            sys.exit(1)

if __name__ == '__main__':
    main()
