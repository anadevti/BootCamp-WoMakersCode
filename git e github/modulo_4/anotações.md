# Como atualizar um fork via linha de comando

## Passo a Passo:

1. **Clone seu fork localmente**:
    ```sh
    git clone https://github.com/seu-usuario/seu-fork.git
    cd seu-fork
    ```

2. **Adicione o repositório original como um remoto**:
    ```sh
    git remote add upstream https://github.com/original-usuario/original-repo.git
    ```

3. **Busque as atualizações do repositório original**:
    ```sh
    git fetch upstream
    ```

4. **Atualize seu fork com as mudanças do repositório original**:
    Se você estiver na branch principal (`main` ou `master`), faça o merge das mudanças:
    ```sh
    git checkout main
    git merge upstream/main
    ```

    Se estiver em uma branch diferente ou o repositório original usa uma branch diferente da `main`, ajuste os comandos conforme necessário.

5. **Resolva quaisquer conflitos que possam surgir**:
    Se houver conflitos durante o merge, o Git informará quais arquivos precisam ser resolvidos. Edite esses arquivos para resolver os conflitos, depois adicione-os novamente ao índice:
    ```sh
    git add caminho/para/arquivo-resolvido
    ```

6. **Finalize o merge**:
    Após resolver todos os conflitos e adicionar os arquivos resolvidos, finalize o merge:
    ```sh
    git commit
    ```

7. **Envie as atualizações para seu fork no GitHub**:
    ```sh
    git push origin main
    ```

Seguindo esses passos, você manterá seu fork atualizado com as últimas mudanças do repositório original.
