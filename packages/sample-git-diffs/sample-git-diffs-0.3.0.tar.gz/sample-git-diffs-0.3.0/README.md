# sample-git-diffs

```
Sample git diffs uniformly wrt. number of changes per file. The output is formatted as a .diff file.

optional arguments:
  -h, --help            show this help message and exit
  --n N                 Total number of diffs to be sampled
  --diffstat DIFFSTAT   Custom git diff command for the sampling probabilities
  --diffcommand DIFFCOMMAND
                        Custom git diff command for the actual diff
```

For example, if you want to draw a sample of 25 diffs from the folder data/, you run

```
sample-git-diffs --diffstat "git diff --stat data/" --n 25
```