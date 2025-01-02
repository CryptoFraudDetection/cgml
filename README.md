# 🪙 **cgml**  

Welcome to the **cgml** repository, created for the `Fraud-Detection using Graphs` challenge! 🚀  

- 📖 Read the full blog post about this project [here](https://fuet.ch/cryptofrauddetection/).  
- 📚 Explore the MkDocs documentation [here](https://cryptofrauddetection.github.io/cgml/).  

## ⚙️ **Installing `uv`**  

`uv` is a universal runtime tool that simplifies running and managing Python applications with cross-platform compatibility.  

### 🐧 macOS/Linux  
Run the following command in your terminal:  
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```  

### 🖥️ Windows  
Run this command in PowerShell:  
```powershell
powershell -ExecutionPolicy ByPass -Command "irm https://astral.sh/uv/install.ps1 | iex"
```  

## 🌱 **Setting Up the Environment**  

To set up your development environment, create a virtual environment and install all dependencies:  
```bash
make install
```  

> **Notes:**  
> - Ensure `make` is installed on your system.  
> - Windows users can install `make` via tools like **`choco`** or **`winget`**.  

## 📝 **MkDocs Documentation**  

Start the MkDocs server locally with:  
```bash
make docs-serve
```

## 🛠️ **Further Instructions**  

1. Duplicate the `.env-example` file as `.env` and fill in the required environment variables 🔑.  
2. Load the environment variables:  
   ```bash
   source .env
   ```  
3. You're ready to start! 🎉  

## 📂 **Project Structure**  

```plaintext
├── .github/workflows         <- GitHub Actions workflows.  
├── data       
│   ├── processed             <- Final datasets ready for modeling.  
│   └── raw                   <- Original, immutable data.  
│       
├── docs                      <- Project documentation.  
├── notebooks                 <- Jupyter or Quarto Markdown notebooks.  
│                                Naming: `00-description.qmd`.  
│        
├── reports                   <- Generated outputs: HTML, PDF, diagrams, etc.  
├── src/CryptoFraudDetection  <- Core source code for the project.  
├── tests                     <- Unit tests.  
├── .env-example              <- Sample environment variables.  
├── .gitignore                <- Files ignored by git.  
├── LICENSE                   <- MIT License.  
├── Makefile                  <- Commands like `make install` and `make test`.  
├── mkdocs.yaml               <- MkDocs configuration.  
├── pyproject.toml            <- Build configuration.  
├── README.md                 <- This README file.  
├── ruff.toml                 <- Ruff configuration.  
└── uv.lock                   <- Dependency lock file.  
```  

## 📜 **License**  

This project is licensed under the **MIT License**.  