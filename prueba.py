import subprocess

# Lista de extensiones a instalar
extensions = [
    "bradlc.vscode-tailwindcss",
    "christian-kohler.npm-intellisense",
    "codeium.codeium",
    "dbaeumer.vscode-eslint",
    "donjayamanne.githistory",
    "eamodio.gitlens",
    "equinusocio.vsc-material-theme",
    "equinusocio.vsc-material-theme-icons",
    "esbenp.prettier-vscode",
    "firefox-devtools.vscode-firefox-debug",
    "github.copilot",
    "github.copilot-chat",
    "humao.rest-client",
    "jeff-hykin.better-dockerfile-syntax",
    "mhutchie.git-graph",
    "ms-azuretools.vscode-docker",
    "ms-python.autopep8",
    "ms-python.debugpy",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-vscode-remote.remote-containers",
    "pkief.material-icon-theme",
    "quicktype.quicktype",
    "ritwickdey.liveserver",
    "sdras.vue-vscode-snippets",
    "tal7aouy.rainbow-bracket",
    "uctakeoff.vscode-counter",
    "vue.volar",
    "xabikos.javascriptsnippets",
]

def install_extensions():
    failed_extensions = []  # Para registrar extensiones que no se instalaron

    for extension in extensions:
        try:
            # Ejecuta el comando para instalar la extensión
            print(f"Instalando extensión: {extension}...")
            subprocess.run(["code", "--install-extension", extension], check=True)
            print(f"Extensión instalada: {extension}")
        except subprocess.CalledProcessError as e:
            print(f"Error al instalar la extensión {extension}: {e}")
            failed_extensions.append(extension)

    # Reporte final
    if failed_extensions:
        print("\nLas siguientes extensiones no se pudieron instalar:")
        for ext in failed_extensions:
            print(f"- {ext}")
        print("\nIntenta instalarlas manualmente o verifica si existen en el marketplace.")

if __name__ == "__main__":
    install_extensions()
