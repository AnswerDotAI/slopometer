Python imports are slow the first time and free after that, within one process. The record of completed imports dies with the process. warmpy keeps a process alive so the record survives. A call made in a new process runs in that old process instead.

One rule governs everything: a warm call and a cold call must behave the same. Same arguments, same stdin and stdout, same working directory, same environment, same exit code, same response to Ctrl-C. The user may notice speed. The user may notice nothing else.

This rule decides the design. The client passes its file descriptors to the server, and the server reads and writes the user's real terminal. The working directory and environment travel with every call, because the server's own copies are stale. If the server is missing or broken, the client runs the function itself, slowly. The server is an optimization. It is never a requirement.

The server is a cache, and doubt means disposal. A socket that does not answer is deleted and a new server starts. A server with the wrong version is replaced, never negotiated with. When two clients start a server at once, one wins and the other connects to the winner. When no server can start, the client runs cold. No warmpy failure may become an error the user sees.

A server's name includes everything that could change an answer: the target function, the interpreter, the package versions. Its life is inferred from use. The first call starts it. Idle time ends it. There are no start or stop commands because the user never needs them.

The user has two obligations. Keep the wrapped module cheap to import, with heavy imports inside the function body. Treat import-time state as fixed, because a function that mutates module state acts differently warm than cold, and warmpy cannot detect that.

warmpy caches imports, never results. It is not a task queue, a service manager, or an RPC framework.

The test for every future decision: can the user tell, except by the clock? If yes, the decision is wrong. If no, take the simpler option.
