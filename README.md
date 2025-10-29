# Batalha Naval

    Trabalho desenvolvido na disciplina Optativa de Python, com o objetivo de aplicar conceitos de lógica de programação, uso de cores no terminal e manipulação de matrizes.

## Instalação

Este projeto utiliza apenas o **Python padrão**, sem dependências externas.  
Basta ter o **Python 3.x** instalado no sistema para executar o jogo.

```bash
python batalha_naval.py
```

## Identificação de jogadas

| Símbolo | Significado                      | Cor no Terminal |
| :-----: | :------------------------------- | :-------------- |
|  **A**  | Água não atingida (pré-definida) | Azul forte      |
|  **E**  | Embarcação                       | Cinza           |
|  **O**  | Água atingida (erro de tiro)     | Azul claro      |
|  **X**  | Embarcação atingida (acerto)     | Vermelho        |

## Visualizações
    
### O jogo possui duas formas principais de exibir os tabuleiros:

    • imprime_tabuleiro(tabuleiro)
        Exibe o tabuleiro completo — ideal para testes ou depuração.
        Pode ser usado para visualizar tanto o tabuleiro do jogador quanto o do computador.

    • imprime_visivel(tabuleiro)
        Exibe o tabuleiro parcialmente, ocultando as embarcações inimigas.
        É a visualização padrão durante a partida do jogador.

## Como jogar

### Para iniciar o jogo

#### Na tela inicial, escolha como deseja posicionar seus navios:

        • Manual → você escolhe as posições.

        • Automático → o sistema sorteia posições aleatórias.

### Durante o jogo:

    • O jogador realiza disparos informando as coordenadas desejadas.

    • O computador joga de forma automática e aleatória.

### Para terminar o jogo:

    • O jogo encerra automaticamente quando todos os navios de um dos jogadores são destruídos.

    • Também é possível sair manualmente fechando o terminal ou interrompendo a execução (Ctrl + C).

## Opções oferecidas

### O sistema oferece as seguintes opções ao usuário:

    • Escolher modo de posicionamento dos navios (manual ou aleatório).

    • Visualizar o próprio tabuleiro atualizado a cada rodada.

    • Visualizar o tabuleiro inimigo parcialmente (modo imprime_visivel).

    • Habilitar visualização completa do tabuleiro inimigo (modo imprime_tabuleiro, visualização padrão).

    • Encerrar o jogo ao final de uma vitória, derrota ou manualmente.

## Conclusão

O programa oferece um jogo de Batalha Naval tradicional e funcional, permitindo o usuario escolher se quer colocar manualmente suas embarcações ou automatica.
Há algumas limitações como por exemplo a dificil visualização dos mapas devido ao terminal, em versões futuras poderá ter interface grafica para facilitar interação e visualização

## Autor

    Desenvolvido por [Felipe Silva](https://github.com/Felipe0132)
    Projeto acadêmico - Disciplina: Optativa de Python 
    Curso - Engenharia da Computação

## License

    [MIT](https://choosealicense.com/licenses/mit/)