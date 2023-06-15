>Nota: Este arquivo README foi escrito após a conclusão da Sprint 8. Antes de prosseguir com a descrição dos passos seguidos na Sprint 8, gostaria de expressar minhas sinceras desculpas pela falta de completude e atraso na finalização das tarefas. Infelizmente, devido à minha programação/experiencia limitada, ocorreram algumas dificuldades adicionais durante a sprint.

>Durante o período da sprint, fui acometido por uma gripe que afetou tanto minha capacidade mental quanto física. Isso levou a uma diminuição na minha eficiência e no cumprimento das tarefas dentro do prazo estabelecido, me fazendo falhar na documentação e do readme da tarefa.

>Reconheço a importância de cumprir as metas e prazos estabelecidos e entendo o impacto que minha falta de desempenho pode ter causado. Neste sentido, assumo total responsabilidade pelo meu desempenho abaixo do esperado.

>Novamente, peço desculpas ao monitor Augusto Luiz e comprometo-me a redobrar meus esforços para garantir um desempenho mais eficiente e ORGANIZADO(principalmente) nas próximas sprints.

Agora, gostaria de descrever os passos que foram seguidos na Sprint 8 para a importação de dados do banco IMDB e demais atividades.

### Etapa 1 -  Criando sua conta no TMDB

1. Conta criada e esclarecendo os objetivos da minha pesquisa, na [imagem](Sprint8/secao2/etapa1contaTMDB.jpg) eu ainda estava decidindo entre os três temas que indiquei na imagem, mas acabei ficando com a primeira ideia após todos da squad declararem seus proprios temas para não ter repetições.
2. Execução do teste para ver a conexão da API, a execução em [notebook](Sprint8/secao2/etapa2testedecredebib.ipynb) facilita em ver os resultados da pesquisa.

Extra: ao definir meu objetivo de pesquisa, que é a relação Nota x Duração dos filmes separados por anos e decadas, eu defini um SQL([link](https://github.com/jademarinho/Sprint1/blob/main/Sprint8/secao2/sprint%20do%20movies%20em%20sql.txt)) para rodar minha busca localmente. 
A informação que quero extrair do JSON na proxima etapa seria a localização que o filme foi produzido.

### Etapa 2 - Tarefa 2: Desafio Parte 2 - Ingestão de dados do Twitter e/ou TMBD

Como decidi na etapa anterior, meu objetivo de pesquisa era abrangente a todos os filmes, foi instruido "utilize o CSV carregado na Etapa 1 como fonte de entrada para localização dos IDs do IMDB para depois realizar a pesquisa no TMDB"
Na [Layer](Desafio/Sprint8/2layer.jpg) foi necessario o [Pandas](Desafio/Sprint8/1layer.jpg), mas para isso primeiro se deve ([[autorizar seu IAM]](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint8/config%20IAM.jpg)) para realização da função.

Limitei ainda mais minha pesquisa para não dar resultados excessimos ou nulos, conforme o SQL ([link](https://github.com/jademarinho/Sprint1/blob/main/Sprint8/secao2/sprint%20do%20movies%20em%20sql.txt)) que veio da etapa anterior, rodando localmente [aqui](Desafio/Sprint8/1dataimpresso.ipynb) em notebook, com os devidos resultados, resolvi reduzir ainda mais minha pesquisa para colocar na AWS e subir a quantidade de votos para 1500.

Agora que os encontrei o que quero buscar do JSON, vamos para a parte do [docker e boto3](https://github.com/jademarinho/Sprint1/tree/main/Desafio/Sprint8/Nova%20pasta)

Para gerar os [JSON de 100 em 100](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint8/saidas%20json.jpg), dando um total de 754 filmes, [executei o código com barra de processo tqdm](Desafio/Sprint8/execucaocod.png) e validando o sucesso '200' na response.

Extra: Primeiro eu fiz um [dataframe integrando as informações](Desafio/Sprint8/criandodfcominfodojson.py) que eu queria, que era País de produção do filme, mas não era ainda não era para gerar os JSONs, mas fiquei satisfeita com o resultado.
Extra2: Os [resultados](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint8/nb%20com%20informacoes%20de%20api%20final.ipynb) de todos esses codigos pode ser encontrado nesse notebook com notações md entre os codigos.

[Codigo final do desafio](Desafio/Sprint8/importarjsondeinteresse.py)

### Etapa 3: Exercícios - Geração de massa de dados

Primeira etapa da tarefa era [gerar a lista](Sprint8/secao4/ex4-1.ipynb) de nomes em um data frame.
A partir desses resultados a gente pode continuar a fazer os demais exercicios, que vai usar esse data frame como base para os resultados.
A execução das 10 demais [tarefas](Sprint8/secao4) pode ser visto nessa pasta em formato de notebook com os outputs dos respectivos.

### Etapa 4: Certificado

[link](Certificados/Sprint8/UC-0ab2c968-bd35-4ec5-b505-01fbc18f7035.jpg)
