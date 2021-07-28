# Atualizar datasets do PowerBI utilizando python

## Conteudo

- [Oque é](#getting_started)
- [Permissoes Necessarias](#Permissoes_Necessarias)
- [Requisitos](#requisitos)

## Oque é <a name = "getting_started"></a>

Feature responsavel por atualizar os datasets do power bi e pode ser usado com airflow, assim que uma base for atualizada pelo airflow logo em seguida este conjunto de codigo sera ativado e atualizando as bases de dados necessarias.

### Requisitos <a name = "requisitos"></a>

Client ID, Nome de usuario para conectar no power bi e senha para conectar no power bi.

## Permissoes <a name = "Permissoes_Necessarias"></a>

Para conseguir utilizar o script sera necessario criar um client ID para o power BI, este cliente ID \n
precisa das seguintes permissões 
```
"Read and write all datasets, Read All Workspaces"
```
Link de acesso para criar o client ID: https://dev.powerbi.com/apps selecione as permissões necessarias mencionadas anteriormente.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
