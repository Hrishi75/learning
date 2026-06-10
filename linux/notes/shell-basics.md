# Shell Basics

The shell is a program that reads commands and runs them. Default on most Linux is **bash**. Each command: `name [options] [arguments]`.

## Navigation

```bash
pwd                 # print working directory (where am I)
ls                  # list files
ls -l               # long format: permissions, owner, size, date
ls -la              # also show hidden files (start with .)
cd /etc             # change to absolute path
cd notes            # change to relative path (from here)
cd ..               # up one level
cd ~                # home directory
cd -                # previous directory
```

## Paths

- **Absolute** — starts at root: `/home/user/file.txt`
- **Relative** — from current dir: `notes/file.txt`
- `.` = current dir, `..` = parent, `~` = your home

## Files & directories

```bash
touch file.txt          # create empty file (or update timestamp)
mkdir mydir             # make directory
mkdir -p a/b/c          # make nested dirs, no error if exist
cp src.txt dst.txt      # copy
cp -r dir1 dir2         # copy directory (recursive)
mv old.txt new.txt      # move OR rename
rm file.txt             # delete file (no trash, permanent)
rm -r mydir             # delete directory + contents
rmdir mydir             # delete empty directory only
```

## Viewing file contents

```bash
cat file.txt            # dump whole file
less file.txt           # scroll page by page (q to quit)
head file.txt           # first 10 lines
head -n 20 file.txt     # first 20 lines
tail file.txt           # last 10 lines
tail -f log.txt         # follow: live-stream new lines (Ctrl+C to stop)
wc -l file.txt          # count lines
```

## Searching

```bash
grep "error" log.txt        # lines containing "error"
grep -i "error" log.txt     # case-insensitive
grep -r "TODO" .            # recursive search in current tree
find . -name "*.md"         # find files by name pattern
find . -type d              # find directories
```

## Pipes & redirection

The power of the shell: chain small tools.

```bash
command > file       # redirect output to file (overwrite)
command >> file      # append to file
command < file       # feed file as input
cmd1 | cmd2          # pipe: output of cmd1 becomes input of cmd2
```

Examples:

```bash
ls -l | grep ".txt"             # list, keep only .txt lines
cat log.txt | grep "error" | wc -l   # count error lines
history | tail -20              # last 20 commands you ran
```

## Help

```bash
man ls          # full manual (q to quit)
ls --help       # quick option summary
which python    # show full path of a command
type cd         # what kind of thing is this command
```

## Handy keys

- `Tab` — autocomplete file/command names
- `Ctrl+C` — kill current command
- `Ctrl+L` — clear screen (same as `clear`)
- `Ctrl+R` — search command history
- `↑` / `↓` — previous/next commands
