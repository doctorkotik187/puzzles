# DK's Puzzles

A repository of programming puzzles/assignments, each solving a specific problem in a chosen    language. Used for learning new languages and interview prep.

## Project Structure

- Each puzzle lives in its own top-level directory (e.g. `fizzbuzz/`)
- Directories are named after the puzzle, not the language used
- Each puzzle is self-contained with its source code in the puzzle directory

## Environment & Tooling

The project uses **[mise](https://mise.jdx.dev/)** for tool/version management (see `mise.toml`).

Available tools:
- **Clojure** (`clj`) — latest
- **Babashka** (`bb`) — latest (Clojure scripting, faster startup than `clj`)
- **Java** (JVM, required for Clojure)

Commands are installed via mise. Invoke with `mise exec -- <cmd>` or ensure mise activates in your shell (`mise activate`).

## Running Clojure Puzzles

```bash
# Run with clojure
clj -M fizzbuzz/fizzbuzz.clj

# Run with babashka (faster startup, good for scripting)
bb fizzbuzz/fizzbuzz.clj
```

## Adding a New Puzzle

1. Create a new top-level directory named after the puzzle
2. Add the source file(s) inside that directory
3. Add a section to `README.md` describing the puzzle

## .gitignore Notes

The repo ignores Clojure-specific artifacts: `/target`, `/classes`, `/checkouts`, `.cpcache`, `.clj-kondo/`, `.lsp/`, `pom.xml`, `.lein-*`, `.nrepl-port`, `.prepl-port`, `.DS_Store`, `.idea`, `*.log`, `tmp/`.
