# Permissions

Every file/directory has an **owner**, a **group**, and permission bits controlling who can do what. This is how Linux enforces multi-user security.

## Reading `ls -l`

```
-rwxr-xr--  1  alice  devs  4096  Jun 10 12:00  script.sh
│└┬┘└┬┘└┬┘     └─┬─┘  └┬─┘
│ │  │  │        │     └── group owner
│ │  │  │        └──────── user owner
│ │  │  └── others: r--  (read only)
│ │  └───── group:  r-x  (read + execute)
│ └──────── owner:  rwx  (read + write + execute)
└────────── type: - file, d dir, l symlink
```

Three permission sets, three audiences:
- **owner (u)** — the user who owns it
- **group (g)** — members of the file's group
- **others (o)** — everyone else

Three permissions each:
- **r** read — view file / list directory
- **w** write — modify file / add+delete files in directory
- **x** execute — run file as program / *enter* (cd into) directory

> Directory `x` is required to enter it. Without it, `r` only lets you see names, not use them.

## Octal (numeric) notation

Each permission is a bit. Add them per audience:

```
r = 4
w = 2
x = 1
```

| Octal | Bits | Meaning        |
|-------|------|----------------|
| 7     | rwx  | read+write+exec|
| 6     | rw-  | read+write     |
| 5     | r-x  | read+exec      |
| 4     | r--  | read only      |
| 0     | ---  | nothing        |

Three digits = owner, group, others:

```
755 = rwxr-xr-x   common for scripts/programs + directories
644 = rw-r--r--   common for normal files
600 = rw-------   private file (only owner)
700 = rwx------   private directory
```

## chmod — change permissions

```bash
chmod 755 script.sh        # octal: set exact bits
chmod 644 notes.txt

chmod +x script.sh         # symbolic: add execute (all audiences)
chmod u+x script.sh        # add execute for owner only
chmod g-w file             # remove write from group
chmod o=r file             # set others to exactly read
chmod a+r file             # a = all (u+g+o)
chmod -R 755 mydir/        # recursive: dir + everything inside
```

Symbolic parts: `who` (`u g o a`) + `op` (`+ - =`) + `perm` (`r w x`).

## chown — change owner/group

```bash
sudo chown alice file              # change owner to alice
sudo chown alice:devs file         # owner alice, group devs
sudo chown :devs file              # change group only
sudo chgrp devs file               # change group (alt command)
sudo chown -R alice:devs mydir/    # recursive
```

Changing owner usually needs `sudo`.

## sudo — run as root

```bash
sudo command            # run one command as root (superuser)
sudo -i                 # open a root shell
whoami                  # which user am I
id                      # my user id, group ids, groups
```

`root` (uid 0) bypasses all permission checks. Use `sudo` sparingly.

## Users & groups (where they live)

```bash
cat /etc/passwd     # user accounts (name, uid, home, shell)
cat /etc/group      # groups and members
groups alice        # which groups alice belongs to

sudo adduser bob              # create user
sudo usermod -aG devs bob     # add bob to group devs (-a append, -G group)
```

## Special bits (brief)

```bash
chmod u+s file      # setuid: run as file's OWNER (e.g. /usr/bin/passwd)
chmod g+s dir       # setgid: new files inherit dir's group
chmod +t dir        # sticky bit: only owner can delete own files (/tmp uses this)
```

Shows as `s`/`t` in place of `x`: `-rwsr-xr-x`.

## Mental model

- Permissions = **who** (owner/group/others) × **what** (r/w/x).
- Octal: r=4 w=2 x=1, add per audience → `755`, `644`.
- `chmod` changes permissions, `chown` changes ownership.
- Directory needs `x` to enter, `w` to add/delete files inside.
- `root`/`sudo` ignores all of it — handle with care.
