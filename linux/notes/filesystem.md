# Filesystem

Linux has **one tree**, rooted at `/`. No drive letters (no `C:`). Everything — files, directories, even devices — lives under `/`.

## The standard directory tree (FHS)

```
/            root of everything
├── bin      essential commands (ls, cp, cat) — often symlink to /usr/bin
├── boot     kernel + bootloader files
├── dev      devices as files (disks, terminals): /dev/sda, /dev/null
├── etc      system-wide config files (text). "et cetera"
├── home     user home directories: /home/alice
├── lib      shared libraries for /bin, /sbin
├── media    auto-mounted removable drives (USB, CD)
├── mnt      manual mount points
├── opt      optional / third-party software
├── proc     virtual: live kernel + process info (not real files)
├── root     home dir of the root user (NOT same as /)
├── run      runtime data since boot (PIDs, sockets)
├── sbin     system admin commands (mount, reboot)
├── srv      data served by the system (web, ftp)
├── sys      virtual: hardware/kernel interface
├── tmp      temporary files — wiped on reboot
├── usr      user programs + read-only data (/usr/bin, /usr/local)
└── var      variable data: logs (/var/log), mail, caches, spools
```

Memory hooks:
- **config** → `/etc`
- **logs** → `/var/log`
- **your stuff** → `/home/you`
- **scratch** → `/tmp`
- **installed programs** → `/usr/bin`

## Paths

```bash
/home/alice/notes.txt   # absolute — full path from root
notes.txt               # relative — from current dir
./script.sh             # explicit "in current dir"
../shared/file          # parent dir, then down
~                       # your home (/home/alice)
~bob                    # bob's home (/home/bob)
```

## Inspecting the tree

```bash
ls /                # see top-level dirs
tree                # visual tree (install: sudo apt install tree)
tree -L 2           # limit depth to 2 levels
stat file.txt       # size, owner, permissions, timestamps, inode
file image.png      # what TYPE a file really is (by content, not name)
du -sh dir/         # total size of a directory (human-readable)
du -h --max-depth=1 # size of each subdir
df -h               # disk space free/used per mounted filesystem
```

## Links

Two files can point to the same data.

```bash
ln -s /path/to/target linkname    # symbolic (soft) link — a pointer
ln /path/to/target linkname       # hard link — second name for same data
```

- **Symlink** — like a shortcut. Breaks if target moves/deleted. Can cross filesystems, can link directories. Most common.
- **Hard link** — two directory entries, same inode (data). Survives if original name deleted. Same filesystem only.

```bash
ls -l                # symlinks show as  linkname -> target
readlink linkname    # show what a symlink points to
```

## Mounts

Other disks/partitions attach (mount) onto a directory in the tree.

```bash
mount                       # list everything mounted
lsblk                       # block devices (disks) as a tree
df -h                       # which device backs which path
sudo mount /dev/sdb1 /mnt   # attach disk to /mnt
sudo umount /mnt            # detach
```

A USB at `/dev/sdb1` mounted on `/mnt` means: open `/mnt` → you're reading the USB.

## Hidden files

Names starting with `.` are hidden (config, dotfiles).

```bash
ls -a            # show them
ls -d .*         # only hidden entries
cat ~/.bashrc    # your shell config (a dotfile)
```

## Key ideas

- One tree, root `/`. Disks mount *into* it, not beside it.
- `/etc` config, `/var/log` logs, `/home` you, `/tmp` scratch.
- `/proc` and `/sys` are virtual — kernel data shown as files.
- Symlink = pointer (can break); hard link = same data, two names.
