Importing a big library takes seconds. Python pays that cost once per process, and a CLI starts a new process for every command. Each command therefore pays the import cost again. `warmpy` arranges to pay it once. Your function runs in a background process that has already done its imports. `yourcommand` becomes a small program that starts fast, sends your arguments to the background process, and shows you the output.

One rule governs the whole design. Running through the background process may change nothing except speed. Your function gets the same arguments, reads the same stdin, writes to the same terminal, sees the same working directory and environment variables, and produces the same exit code. Ctrl-C still stops it.

That rule forces the main choices. `yourcommand` hands its own stdin, stdout, and stderr to the background process, which unix sockets allow. Printing, piping, and prompts therefore work exactly as if nothing was in between. `yourcommand` also sends its current directory and environment on every call, because the background process started earlier and its own copies are out of date. And if the background process is missing or broken, `yourcommand` imports the library and runs the function itself. Slower, same answer.

Every failure has a fixed recovery, and none of them reaches the user. If the socket file exists but nothing answers, `yourcommand` deletes the file and starts a fresh background process. Every connection begins with a version check. When the check finds a background process built from an older package version, `yourcommand` tells it to exit and starts a fresh one. If two commands run at the same instant, only one can create the socket, and the other connects to the one that did. If no background process can start at all, `yourcommand` runs the function directly. In every case `yourcommand` succeeds. The worst outcome `warmpy` permits is a slow one.

Each combination of function, Python executable, and package version gets its own socket file, because a change to any of those could change what the function does. Nobody manages the background process by hand. The first call to `yourcommand` starts it, and after thirty idle minutes it exits.

The wrapped code has two obligations:

- Its module must import fast, and `import spacy` therefore goes inside the function body, not at the top of the file. A slow module makes the fast command slow, and `warmpy` cannot fix that.
- Your function must not depend on module-level variables it changed during earlier calls. A new process loses those changes. The background process keeps them. `warmpy` cannot see the difference.

`warmpy` skips imports and nothing else. Your function itself runs on every call.

To judge any future change to `warmpy`, ask whether a user could notice it other than by timing. If they could, reject it. If they could not, take the simpler option.
