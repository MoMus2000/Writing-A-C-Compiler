# Writing-A-C-Compiler

Housekeeping on Mac

- Rosetta 2 enables the execution of `x64` assembly on apple silicon
- Run the command below to launch the x64 shell

```bash
arch -x86_64 zsh
```

## Chapter 1

- To convert C program into assembly

``` bash
gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none return_2.c
```

### Workflow:

- Lex
- Parse
- Emit Assembly
- Use GCC and Clang to assemble and link
