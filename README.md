# Projeto de cadastro de hotéis para o sprint 01 da pós graduação em Engenharia de software

Este projeto destina-se ao curso de pós-graduação 2023 </br> 
<p>Módulo Backend</p>

<p>
objetivo: Criar uma API que permita fazer as operações básicas de inserção, exclusão, atualização e seleção de dados
</p>

<h3>Requisitos de software</h3>
<ul>
    <li>API com, pelo menos, três rotas (por exemplo, “/cadastrar_produto”, “/buscar_produto” e “/deletar_produto”), sendo que, pelo menos, uma delas deve implementar o método Post (por exemplo, na rota de cadastro).</li>
    <li>Fazer uso de um banco de dados SQLite ou PostgreSQL com, pelo menos, uma tabela (por exemplo, tabela de usuários cadastrados).</li>
    <li>Documentação da API em Swagger.</li>
</ul>

<h3>Instalação</h3>
<p>Premissas </p>
<ul>
    <li>Ter instalado e configurado o Phython. A versão testada neste MVP foi a 3.9</li>
    <li>Seguir as instruções para instalação do comando PIP https://pip.pypa.io/en/stable/installation/ caso não esteja instalado</li>
    <li>Criar um ambiente virtual para executar o código local ou ativar o já existente <i>(source venv39/bin/activate)</i></li>    
    <li>Instalar as dependências contidas no arquivo <strong>requirements.txt</strong> através do comando <i>pip install -r requirements.txt</i></li>
</ul>

<h3>Métodos Suportados</h3>
<ul>
    <li><strong>POST /hotel</strong>: Adiciona um novo hotel</li>
    <li><strong>GET /hotels</strong>: Obter a lista de todos os hotéis cadastrados</li>
    <li><strong>GET /hotel{id}</strong>: Obter um hotel específico pelo id informado</li>
    <li><strong>DELETE /hotel/{id}</strong>: Exclui o hotel pelo id informado</li>    
    <li><strong>PUT /hotel/{id}</strong>: Aletra o hotel identificado pelo id, com as informações passadas no corpo da requisição</li>    
</ul>

<h3>Documentação</h3>
<p>Na pasta __documentation encontra-se a coleção atualizada das rotas deste projeto, para utilizar, basta importar no Postman.</p>
<p>Para acessar a documentação do swagger utilize o caminho <i>/api/docs</i> quando o programa estiver em execução</p>
