import os
import subprocess
import getpass

"""
comando antes de dar deploy:

git init
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git


"""


def run_command(command):
    """Executa um comando no terminal e exibe a saída."""
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"❌ Erro/Aviso: {stderr.strip()}")
        return False
    if stdout:
        print(stdout.strip())
    return True

def main():
    print("🚀 === Script de Deploy Automático - OrderFlow ===")

    # 1. Dados do Usuário
    username = input("Digite seu usuário do GitHub: ").strip()
    email = input("Digite seu e-mail do GitHub: ").strip()
    token = getpass.getpass("Cole seu Personal Access Token (o texto fica invisível): ").strip()

    if not username or not token:
        print("❌ Usuário e Token são obrigatórios.")
        return

    # 2. Configura a identidade do Git
    print("\n⚙️ Configurando identidade local do Git...")
    run_command(f'git config user.name "{username}"')
    run_command(f'git config user.email "{email}"')

    # 3. Identifica a URL do repositório remoto
    remote_proc = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
    if remote_proc.returncode != 0:
        print("❌ Remote 'origin' não foi encontrado. Execute 'git remote add origin URL'.")
        return
    
    raw_url = remote_proc.stdout.strip()
    # Limpa a URL para extrair apenas 'usuario/repositorio'
    repo_path = raw_url.split("github.com/")[-1].replace(".git", "")
    auth_url = f"https://{username}:{token}@github.com/{repo_path}.git"

    # 4. Adiciona arquivos
    print("\n📦 Adicionando arquivos alterados...")
    run_command("git add .")

    # 5. Cria o Commit
    commit_msg = input("\n💬 Digite a mensagem do commit (ex: Aula 03 - Dominio inicial): ").strip()
    if not commit_msg:
        commit_msg = "Atualização diária da aula"

    print(f'\n📝 Criando commit: "{commit_msg}"...')
    run_command(f'git commit -m "{commit_msg}"')

    # 6. Sincroniza e envia para o GitHub
    print("\n🔄 Sincronizando com o repositório remoto...")
    run_command(f'git pull {auth_url} main --allow-unrelated-histories --no-edit')

    print("\n⬆️ Enviando para o GitHub...")
    if run_command(f'git push {auth_url} main'):
        print("\n✅ Sucesso! Código atualizado no GitHub.")
    else:
        print("\n❌ Falha ao enviar para o GitHub. Verifique se criou um novo Token válido.")

# 7. (Opcional) Criar e enviar Tag da aula
    criar_tag = input("\n🏷️ Deseja criar uma tag para esta aula? (ex: aula-03 ou N para pular): ").strip()
    if criar_tag and criar_tag.lower() != 'n':
        run_command(f'git tag {criar_tag}')
        run_command(f'git push {auth_url} {criar_tag}')
        print(f"✅ Tag '{criar_tag}' criada com sucesso!")


if __name__ == "__main__":
    main()