# Começando o OrderFlow (a partir do pendrive)

LP3 — IFSP-SPO · 2026/2. Você recebeu a pasta `tads-lp3`. Siga na ordem.
Faça **uma vez** só, no primeiro dia.

---

## 1. Copie a pasta do pendrive para o seu computador

Copie `tads-lp3` do pendrive para um lugar seu (ex.: `Documentos`).
**Não trabalhe direto no pendrive.**

## 2. Confira o ambiente

Abra a pasta pela IDE (IntelliJ ou Eclipse) como projeto Maven e rode a classe
`Main`, ou use o terminal:

```bash
mvn -q compile
java -cp target/classes br.edu.ifsp.orderflow.Main
```

Se aparecer `Ambiente OK. Java ...`, está tudo certo.

## 3. Apague o histórico do professor (importante)

A pasta pode já conter um histórico Git. Você quer o **seu**, começando do
zero. Dentro da pasta `tads-lp3`:

**Linux/Mac:**
```bash
rm -rf .git
```
**Windows (PowerShell):**
```powershell
Remove-Item -Recurse -Force .git
```

## 4. Inicialize o seu repositório local

```bash
git init -b main
git add .
git commit -m "estrutura inicial do OrderFlow"
```

> Se o `git` reclamar de identidade, rode uma vez:
> ```bash
> git config --global user.name "Seu Nome"
> git config --global user.email "seu-email@exemplo.com"
> ```

Pronto — você já tem controle de versão local. **Isto basta para trabalhar em
aula.** O GitHub (passos abaixo) é para guardar na nuvem e para o professor
acompanhar.

---

## 5. Crie o repositório vazio no GitHub

1. Entre em <https://github.com> e faça login.
2. Clique em **New** (ou no `+` no topo → **New repository**).
3. **Nome:** `tads-lp3`.
4. Deixe **público**.
5. **NÃO** marque "Add a README", "Add .gitignore" nem "license" — o repositório
   tem que nascer **vazio**, senão dá conflito no próximo passo.
6. Clique em **Create repository**.

## 6. Conecte o local ao GitHub e envie

Na página que abriu, o GitHub mostra a URL do seu repositório (algo como
`https://github.com/SEU-USUARIO/tads-lp3.git`). Use-a abaixo:

```bash
git remote add origin https://github.com/SEU-USUARIO/tads-lp3.git
git push -u origin main
```

Atualize a página do GitHub: seus arquivos estão lá.

---

## No dia a dia (toda aula)

Trabalhe normalmente e, ao final de cada encontro, registre:

```bash
git add .
git commit -m "aula-03: dominio, contratos e fluxo sincrono"
git tag aula-03
git push
git push --tags
```

- `commit` grava o estado no seu histórico local.
- `tag` marca o fim da aula (facilita voltar depois).
- `push` (com `--tags`) envia tudo para o GitHub.

**Faça isso toda aula.** Seus commits e tags são o que comprova o
acompanhamento contínuo do projeto (parte da nota).

---

## Deu erro?

- **`git push` pede usuário e senha e a senha não funciona:** o GitHub não
  aceita mais a senha da conta no terminal. Gere um **Personal Access Token**
  (GitHub → Settings → Developer settings → Personal access tokens) e use o
  token no lugar da senha. Alternativa mais simples: instale o **GitHub
  Desktop** e faça login por ele.
- **`error: remote origin already exists`:** você já tinha configurado o
  remote. Troque a URL com:
  ```bash
  git remote set-url origin https://github.com/SEU-USUARIO/tads-lp3.git
  ```
- **`Updates were rejected` / `fetch first` no primeiro push:** o repositório
  do GitHub não nasceu vazio (veio com README/license). Crie outro sem marcar
  nenhuma opção, ou force o envio inicial:
  ```bash
  git push -u origin main --force
  ```
- **`failed to push some refs`:** rode `git pull origin main --rebase` e depois
  `git push`.
