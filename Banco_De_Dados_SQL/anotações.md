# Comando CREATE:
 - Basicamente cria uma tabela no banco de dados.
    - Sintaxe:
    CREATE TABLE nome_da_tabela (
        nome_da_coluna tipo_da_coluna,
        nome_da_coluna tipo_da_coluna,
        ...
    );

# Comando ALTER:
 - Basicamente altera a estrutura de uma tabela.
    - Sintaxe:
    ALTER TABLE nome_da_tabela
    ADD nome_da_coluna tipo_da_coluna;

# Comando DROP:
    - Basicamente deleta uma tabela do banco de dados.
        - Sintaxe:
        DROP TABLE nome_da_tabela;

# Comando INSERT:
    - Basicamente insere dados em uma tabela.
        - Sintaxe:
        INSERT INTO nome_da_tabela (nome_da_coluna, nome_da_coluna, ...)
        VALUES (valor_da_coluna, valor_da_coluna, ...);

# Comando DELETE:
    - Basicamente deleta dados de uma tabela.
        - Sintaxe:
        DELETE FROM nome_da_tabela
        WHERE condição;

# Comando SELECT:
    - Basicamente seleciona dados de uma tabela.
        - Sintaxe:
        SELECT nome_da_coluna, nome_da_coluna, ...
        FROM nome_da_tabela
        WHERE condição;

# Comando UPDATE:
    - Basicamente atualiza dados de uma tabela.
        - Sintaxe:
        UPDATE nome_da_tabela
        SET nome_da_coluna = valor_da_coluna, nome_da_coluna = valor_da_coluna, ...
        WHERE condição;




# Order By:
    - Basicamente ordena os dados de uma tabela.
        - Sintaxe:
        SELECT nome_da_coluna, nome_da_coluna, ...
        FROM nome_da_tabela
        ORDER BY nome_da_coluna ASC/DESC;

# Joins:
    - Basicamente junta duas ou mais tabelas.
        - Sintaxe:
        SELECT nome_da_tabela.nome_da_coluna, nome_da_tabela.nome_da_coluna, ...
        FROM nome_da_tabela
        JOIN nome_da_tabela ON nome_da_tabela.nome_da_coluna = nome_da_tabela.nome_da_coluna;

    - INNER JOIN:
        - Basicamente junta duas ou mais tabelas com base em uma condição.
            - Sintaxe:
            SELECT nome_da_tabela.nome_da_coluna, nome_da_tabela.nome_da_coluna, ...
            FROM nome_da_tabela
            INNER JOIN nome_da_tabela ON nome_da_tabela.nome_da_coluna = nome_da_tabela.nome_da_coluna;

    - LEFT JOIN:
        - Basicamente trás as informações de tudo que vem da esquerda. preenche todas as infos a esquerda.
            - Sintaxe:
            SELECT nome_da_tabela.nome_da_coluna, nome_da_tabela.nome_da_coluna, ...
            FROM nome_da_tabela
            LEFT JOIN nome_da_tabela ON nome_da_tabela.nome_da_coluna = nome_da_tabela.nome_da_coluna;

    - RIGHT JOIN:
        - Basicamente trás as informações de tudo que vem da direita. preenche todas as infos a direita.
            - Sintaxe:
            SELECT nome_da_tabela.nome_da_coluna, nome_da_tabela.nome_da_coluna, ...
            FROM nome_da_tabela
            RIGHT JOIN nome_da_tabela ON nome_da_tabela.nome_da_coluna = nome_da_tabela.nome_da_coluna;

    - FULL JOIN:
        - Basicamente trás as informações de tudo que vem da esquerda e da direita. (todas as linhas)
            - Sintaxe:
            SELECT nome_da_tabela.nome_da_coluna, nome_da_tabela.nome_da_coluna, ...
            FROM nome_da_tabela
            FULL JOIN nome_da_tabela ON nome_da_tabela.nome_da_coluna = nome_da_tabela.nome_da_coluna;


# Subconsultas:
    - Basicamente é uma consulta dentro de outra consulta.
        - Sintaxe:
        SELECT nome_da_coluna, nome_da_coluna, ...
        FROM nome_da_tabela
        WHERE nome_da_coluna IN (SELECT nome_da_coluna FROM nome_da_tabela WHERE condição);