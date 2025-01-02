# cgml

Repository for the cgml challenge.

## Installing `uv`

`uv` is a universal runtime tool for running and managing Python applications. It ensures a streamlined setup and cross-platform compatibility.

### macOS/Linux  
Run the following command in your terminal:  
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows  
Execute the following in PowerShell:  
```powershell
powershell -ExecutionPolicy ByPass -Command "irm https://astral.sh/uv/install.ps1 | iex"
```

## Setting Up the Environment

Run the command below to create a virtual environment and install all required dependencies:  
```bash
make install
```

Notes:
- Ensure you have **`make`** installed on your system for the setup command.  
- For Windows users, you may need to install `make` using tools like **`choco`** or **`winget`**.  

## MkDocs
Run the command below to start the MkDocs server:  
```bash
make docs-serve
```

## Further instructions

1. Copy the `.env-example` file to `.env` and fill in the necessary environment variables 🔑
2. Load the environment variables using the `source .env` command 🔄
3. You're ready to start working ☕️

## Structure

```
├── .github/workflows         <- Github actions workflows.
├── data       
│   ├── processed             <- The final, canonical data sets for modeling.
│   └── raw                   <- The original, immutable data dump.
│       
├── docs                      <- Documentation for the project.
├── notebooks                 <- Jupyter or Quarto Markdown Notebooks.
│                                Naming convention is a number (for ordering) and a short `-`
│                                delimited description, e.g. `00-example.qmd`.
│        
├── reports                   <- Generated analysis as HTML, PDF, LaTeX, diagrams, etc.
├── src/CryptoFraudDetection  <- Source code package for use in this project.
├── tests                     <- Unit tests for the project.$
├── .env-example              <- Example environment variables.
├── .gitignore                <- Files to be ignored by git.
├── LICENSE                   <- MIT License.
├── Makefile                  <- Makefile with commands like `make install` or `make test`.
├── mkdocs.yaml               <- MkDocs configuration file.
├── pyproject.toml            <- Package build configuration.
├── README.md                 <- The top-level README for developers using this project.
├── ruff.toml                 <- Ruff configuration file.
└── uv.lock

```