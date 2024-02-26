# import subprocess
# import sys

# def run_command(command):
#     """
#     Executa um comando no shell e exibe a saída.
#     """
#     try:
#         output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
#         print(output)
#     except subprocess.CalledProcessError as e:
#         print(f"Erro ao executar o comando {command}: {e.output}")

# def main(commit_message):
#     """
#     Executa uma série de comandos para automatizar o processo de commit.
#     """
#     # Constrói o livro com Jupyter Book
#     run_command("jupyter-book build --all .")
    
#     # Adiciona todas as mudanças ao Git
#     run_command("git add ./*")
    
#     # Commita as mudanças com a mensagem fornecida
#     run_command(f'git commit -m "{commit_message}"')
    
#     # Faz push das mudanças
#     run_command("git push")
    
#     # Publica o livro com ghp-import
#     run_command("ghp-import -n -p -f _build/html")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Uso: script.py <mensagem de commit>")
#     else:
#         commit_message = sys.argv[1]
#         main(commit_message)


#!/usr/bin/env python3

import subprocess
import sys

def main():
  # Obtém a mensagem de commit como parâmetro
  if len(sys.argv) < 2:
    print("Erro: Mensagem de commit não informada.")
    print("Uso: python automatizar_commits.py <mensagem_de_commit>")
    return
  mensagem_commit = sys.argv[1]

  # Constrói o livro Jupyter
  subprocess.run(["jupyter-book", "build", "--all", "."])

  # Adiciona todos os arquivos ao Git
  subprocess.run(["git", "add", "./*"])

  # Cria um commit com a mensagem informada
  subprocess.run(["git", "commit", "-m", mensagem_commit])

  # Envia o commit para o repositório remoto
  subprocess.run(["git", "push"])

  # Importa o livro para o GitHub Pages
  subprocess.run(["ghp-import", "-n", "-p", "-f", "_build/html"])

if __name__ == "__main__":
  main()
