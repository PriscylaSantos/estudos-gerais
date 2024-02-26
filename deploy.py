
#!/usr/bin/env python3

import subprocess
import sys


def run_command(command):
    """
    Executa um comando no shell e exibe a saída.
    """
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando {command}: {e.output}")
        print('----> Deploy cancelado.')
        raise

def main():
    print('===== SCRIPT INICIADO =====')
    if len(sys.argv) < 2:
        print("Erro: Mensagem de commit não informada.")
        print("Uso: python automatizar_commits.py <mensagem_de_commit>")
        return
    mensagem_commit = sys.argv[1]

    print('1 - Contruindo o livro com Jupyter Book')
    run_command("jupyter-book build --all .")
    
    print('2- Adicionando todas as mudanças ao Git')
    run_command("git add ./*")
    
    print('3 - Commitado as mudanças com a mensagem fornecida')
    run_command(f'git commit -m "{mensagem_commit}"')
    
    print('4 - Fazendo push das mudanças no branch main') 
    run_command("git push")
    
    print('5 - Publicando o livro com ghp-import no branch gh-pages')
    run_command("ghp-import -n -p -f _build/html")

    print('----> Deploy finalizado.')

if __name__ == "__main__":
  main()
  print('===== SCRIPT FINALIZADO =====')
