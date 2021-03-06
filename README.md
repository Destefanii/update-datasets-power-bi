# Atualizar datasets do PowerBI utilizando python

<p align="center">
  <img src="/src/airflow+power_bi.png" width="350" title="Airflow com power bi" alt="airflow">
</p>

## Conteudo

- [Oque é ❓](#getting_started)
- [Requisitos ⚠ ](#requisitos)
- [Permissoes Necessarias 🔐](#Permissoes_Necessarias)
- [Permissoes Necessarias Cloud ☁](#Azure)


## Oque é ❓<a name = "getting_started"></a>

Feature responsável por atualizar os datasets do power bi que pode ser usado com airflow, assim que uma base for atualizada pelo airflow logo em seguida o dataset que esteja vinculado a aquele pipeline também será atualizado, assim centralizando a atualização de datasets do powerbi em um único lugar com fácil entendimento de quais bases foram ou não atualizadas.

### Requisitos ⚠<a name = "requisitos"></a>

Client ID, Nome de usuário para conectar no power bi e senha para conectar no power bi.

## Permissoes 🔐<a name = "Permissoes_Necessarias"></a>

Para conseguir utilizar o script sera necessario criar um client ID para o power BI, este cliente ID 
precisa das seguintes permissões 
```
"Read and write all datasets, Read All Workspaces"
```
Link de acesso para criar o client ID: https://dev.powerbi.com/apps selecione as permissões necessárias mencionadas anteriormente, essas permissões devem ser registradas no e-mail que esteja vinculado a cloud da azure do seu projeto.

## Proximos passos utilizando a Azure ☁ <a name = "Azure"></a>

Para conseguir utilizar esse script no seu projeto, na azure sera necessário registar a chave do client ID dentro 
de App Registrations, portanto siga os próximos passos: App Registrations -> Selecione o nome que você escolheu para o client id do power bi -> API Permissions -> Grant admin consent for (Resource group).

Assim que esses passos forem finalizados o script já vai estar com permissão para acessar os datasets e atualizar os mesmos assim que forem solicitados 🚀