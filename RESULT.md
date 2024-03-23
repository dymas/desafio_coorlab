# Resultado - Desáfio CoorLab

## Soluções utilizadas
- Vue.js;
- TypeScript;
- Normalize.css;
- FastAPI.

## Práticas utilizadas
- HTML semântico;
- Mobile-first;
- Design responsivo.

## Desenvolvimento
O desenvolvimento foi iniciado pelo front-end. O Vue.js foi instalado e em seguida foi implementado o componenente LeftSidebar.vue, que representa a barra lateral azul com o logotipo e o link para a calculadora de viagens. Quando o componente é montado, é verificado o tamanho da janela para adaptar o menu e também é adicionado um event listener para caso o usuário redimensione a janela. Depois, foi criado o componente NavBar.vue para implementar a barra superior branca.

O componente principal é o TripCalculator.vue que possui os estilos e funções para o cálculo da viagem. As constantes ``destiny`` e ``chosen_date`` são reativas e aguardam o preenchimento do usuário. A constante ``dialog`` manipula o modal e ``result`` guardará os resultados da pesquisa. O componente antes de ser montado faz requisição GET ao back-end buscando a lista de cidades disponíveis na endpoint "/". Ao preencher a cidade e a data, é feito uma requisição ao endpoint "/city/{city}", onde "{city}" é a cidade escolhida. Caso o usuário não preencha a cidade ou data e tente submeter o formulário, um ``<dialog>`` é exibido pedindo a inserção dos dados.

O CSS é, em sua maior parte, puro. Foi utilizado o Normalize.css para maior consistência entre os navegadores. Foi dada preferência à soluções nativas do HTML5 e CSS3 por questões de desempenho. Um dos exemplos é o menu hamburguer exibido em viewports menores que 1024px, que usa a tag ``<details>``.

Os componentes com ícones SVG foram criados utilizando os ícones distribuídos gratuitamente pelo [LineIcons](https://lineicons.com/free-icons). Alguns ícones estão na pasta public por questões de praticidade.

Todos os componentes são chamados no App.vue.

A API foi criada utilizando o framework [FastAPI](https://fastapi.tiangolo.com/). Todo o código original do back-end está no arquivo main.py. Foram criadas duas endpoints:

- GET ``/``: retorna a lista de cidades disponíves no data.json;
- GET ``/city/{city}``:  retorna uma lista com dois objetos, ambos selecionados de acordo com a cidade enviada como path parameter: o primeiro é o transporte mais rápido e confortável, o segundo é o mais econômico.