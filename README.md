# 🏗️ Ethos Builder

This repository is the central compilation and packaging factory for the **Ethos** programming language and the **Forge** package manager. 

The core `ethos-lang` and `forge` repositories are strictly dedicated to source code. **Ethos Builder** is responsible for pulling that raw Python source, compiling it into standalone bare-metal executables using Nuitka, and wrapping those binaries into user-friendly, production-ready OS installers.

### ⚙️ The Build Pipeline
1. **Source Retrieval:** Fetches the latest stable source code from `ethos-lang` and `forge`.
2. **Binary Compilation:** Uses isolated Python virtual environments and Nuitka (`--standalone --onefile`) to compile the source into native Linux, Windows, and macOS executables.
3. **OS Packaging:** Wraps the raw binaries into system-specific installers and pushes them to our distribution channels.

### 📦 Distribution Channels

**Linux Native Repositories:**
* **Ubuntu/Debian (PPA):** Automated `.deb` builds published to a Personal Package Archive for `apt` integration.
* **Fedora/RHEL (COPR):** Official `.rpm` packages distributed via Fedora COPR.
* **Arch Linux (AUR):** `PKGBUILD` scripts maintained for the Arch User Repository (`ethos-bin` and `ethos-git`).

**Standalone OS Installers:**
* **Windows (`.msi` / `.exe`):** Configures the installation wizard, sets the global system `PATH`, and registers the `.ethos` file extension.
* **macOS (`.pkg`):** Packages Apple Silicon and Intel binaries into standard signed Apple installers.

### 🚀 Future Roadmap
* **Android (Termux):** Native compilation and environment configuration for running Ethos and Forge directly within the Termux mobile terminal.

### 🛠️ Installer Responsibilities
Regardless of the operating system, all builder scripts guarantee the following environment state upon installation:
1. The `ethos` and `forge` binaries are globally accessible via the system `PATH`.
2. The `.ethos` file extension is natively associated with the Ethos execution engine, allowing scripts to run via `ethos script.ethos`.
3. The `~/.ethos/traits` directory is provisioned (acting as the `sys.path` root for Python-based Soft Traits), alongside the nested `~/.ethos/traits/hard_traits` directory for compiled C/C++ binaries.
