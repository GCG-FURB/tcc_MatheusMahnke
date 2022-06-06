# Reuniões

## 2021-03-11

### Tecnolgia

Drone: antigo ou novo

Título: Arquitetura para Navegação Autônoma Drones

Pensa em modularizar e desenvolver a partes para permitir atingir o objetivo de
transportar um produto de um ponto para outro dentro de uma cidade.

Comentei da dificuldade em usar um espaço maior e público.

TCC Diego Fachinello Correa: <http://dsc.inf.furb.br/tcc/index.php?cd=6&tcc=2041>
TCC João Serodio: <http://dsc.inf.furb.br/arquivos/tccs/monografias/2018_2_joao-paulo-serodio-goncalves_monografia.pdf>

Site de Mapa livre: <https://www.openstreetmap.org/relation/296522#map=17/-26.87195/-49.10744>

Drones:
<https://shop.santoslab.com/portfolio/bebop-pro-3d-modeling/>
<https://support.parrot.com/global/support/products/parrot-bebop-pro-3d-modeling>
<https://www.tecmundo.com.br/analise/52197-analise-drones-parrot-ar-2-0-limited-e-elite-edition-video-.htm>

## 2021-05-03

### Defesa Pré-projeto

[Anotações de defesa do Pré-projeto](./tcc_MatheusMahnke_2021-05-03_PreProjeto_Defesa.md)

----

## 2022-03-07

Mencionou que comprou um Drone. Mas memso assim vai usar o drone do LIFE.  
Falei para conversar com prof. Maurício para fazer emprestimo do Drone.  

Pedi para fazer um esboço de como ficaria a arquitetura.  

## 2022-03-14

Chegou o Drone do orientando.  
Vai esperar um pouco para pegar do LIFE (Maurício vai usar).  

[Arquitetura](./arquitetura.svg "Arquitetura")  

Vai trabalhar:

- entender os comandos do Drone e tentar usar PC para comandar o drone.  
- ligar placa com PC. Ver como processar imagem na placa.  

## 2022-03-21

Estava fora da FURB e desmarquei a reunião:
Oi Matheus Mahnke, estou num compromisso fora da FURB e não vou conseguir chegar a tempo para nossa reunião hoje.  
Não te avisei antes porque estava na esperança de chegar a tempo .. estou em trânsito tentando chegar na FURB.  
Bom, peço que me descreve rapidamente o que conseguisse fazer esta semana, e o que pretendes fazer para próxima semana.  
E me avise se achas que devemos remarcar a nossa reunião ainda para esta semana, ou deixamos para conversar na próxima semana.  

[17:31] Matheus Mahnke  
Na semana passada foquei na engenharia reversa do app pra controlar o drone, consegui controlar por um emulador de android e interceptar as requisições pelo wireshark.Para essa semana vou tentar entender a comunicação que esta em chinês e tentar controlar o drone pelo python.  
[17:32] Matheus Mahnke  
Tenho em mente fazer isso, caso eu tenha muitos contra tempos ai marcamos uma call  

## 2022-04-18  

<https://www.youtube.com/watch?v=8DISRmsO2YQ>

Vai usar o DataSet exemplo .. depois pegar real.  
decidir qual Drone usar (Drone3).  
Vai fazer Deploy do Docker na placa (instalar o novo SO Rasq). --> nuvem de pontos.  
--> Pedi para cuidar com o cronograma.  

## 2022-04-25

- problemas com código de reconhecimento do link para Placa  
- Acho formas de contornoar o problema  
- pedi para acelerar o desenvolvimento  

## 2022-05-09

Aluno(a): Matheus Mahnke
08/05/2022 23:26:44
Horas trabalhadas: 320

- Trocado a lib node-bebop em nodejs para pyparrot em python, visto que a forma de conexão dos comandos com a lib node-bebop só permite execução em uma única thread.  
- Feito teste de carga com o carregador portátil acoplado ao drone.  
- Inicio dos cenários de testes ainda sem utilizar GPS e visão computacional.  

- comandos de voo  
- dados dos sensores
- já está carregando a placa e bateria
    esta semana - NÃO GPS
- NÃO Stream de video
- cv2 -> OpenCV

## 2022-05-23

Relatório quinzenal aluno  
23/05/2022  
Horas trabalhadas: 380  

- Atuando nos cenários de testes enolvendo GPS  
- Troca do gps do drone por um modulo gps externo conectado ao raspberry pi  
- Atuando no streaming de video para o raspberry pi  

## 2022-06-06

Relatório quinzenal _ Horas trabalhadas: 440  

- Instalado MiDaS pytorch no raspberry pi  
- Realizado algoritmo de desvio de obstáculo  
- Realizado testes do MiDaS no raspberry pi  
- Realizado testes com peso no drone  

Problemas com em ter acesso ao streamming de video do Drone e optou em usar uma placa ligada a placa IOT.
No PC funciona, mas na placa IOT está com 15 segundos para cada novo frame.  

A-GPS
    3G
    WIFI
    GPS
Problemas com pegar coordenadas do GPS, passei o tCC do WillliamLopes:  
<http://dsc.inf.furb.br/arquivos/tccs/monografias/2019_2_william-lopes-da-silva_monografia.pdf>  
<https://github.com/GCG-FURB/tcc_WilliamLopesSilva>  
<http://dsc.inf.furb.br/arquivos/tccs/monografias/2020_1_diego-fachinello-correa_monografia.pdf>  
<http://dsc.inf.furb.br/arquivos/tccs/monografias/2018_2_joao-paulo-serodio-goncalves_monografia.pdf>  
