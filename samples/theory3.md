Importing a big library takes seconds. Python pays that cost once per process, and a CLI starts a new process for every command, so a CLI pays it on every command. warmpy arranges to pay it once. Your function runs in a background process that has already done its imports. The command you type becomes a small program that starts fast, sends your arguments to the background process, and shows you the output.

One rule governs the whole design. Running through the background process may change nothing except speed. The function gets the same arguments, reads the same stdin, writes to the same terminal, sees the same working directory and the same environment variables, and produces the same exit code. Ctrl-C still stops it.

That rule forces the main choices. The command hands its own stdin, stdout, and stderr to the background process, which unix sockets allow. Printing, piping, and prompts therefore work exactly as if nothing was in between. The command also sends its current directory and environment on every call, because the background process started earlier, possibly in a different directory, and its own copies are out of date. And if the background process is missing or broken, the command imports the library and runs the function itself. Slower, same answer.

Every failure has a fixed recovery, and none of them reaches the user. If the socket file exists but nothing answers, the command deletes the file and starts a fresh background process. If the background process was built from an older version of the package, the command tells it to exit and starts a fresh one; every connection begins with a version check, which is how this is noticed. If two commands run at the same instant, only one can create the socket, and the other connects to the one that did. If no background process can start at all, the command runs the function directly. In all cases the user's command succeeds. The worst outcome warmpy permits is a slow one.

Each combination of function, Python executable, and package version gets its own socket file, because a change to any of those could change what the function does. Nobody manages the background process by hand. The first command starts it, and after ten idle minutes it exits.

The wrapped code has two obligations. Its module must import fast, so `import spacy` goes inside the function body, not at the top of the file; a slow module makes the fast command slow, and warmpy cannot fix that. And the function must not depend on module-level variables it changed during earlier calls. In a new process those changes are gone, in the background process they persist, and warmpy cannot see the difference.

warmpy skips imports and nothing else. Your function itself runs on every call. warmpy is not a task queue, not a service manager, and not an RPC framework.

To judge any future change to warmpy, ask whether a user could notice it other than by timing. If they could, reject it. If they could not, take the simpler option.
