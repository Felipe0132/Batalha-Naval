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
    
    O jogo possui duas formas principais de exibir os tabuleiros:

    imprime_tabuleiro(tabuleiro)
    Exibe o tabuleiro completo — ideal para testes ou depuração.
    Pode ser usado para visualizar tanto o tabuleiro do jogador quanto o do computador.

    imprime_visivel(tabuleiro)
    Exibe o tabuleiro parcialmente, ocultando as embarcações inimigas.
    É a visualização padrão durante a partida do jogador.

## Como jogar

    -O jogador pode posicionar manualmente seus navios ou optar por uma disposição aleatória.

    -O adversário (computador) realiza jogadas de forma aleatória.

    -A cada rodada:

        -O jogador vê seu próprio tabuleiro atualizado.

        -Pode acompanhar os tiros realizados no tabuleiro inimigo.

    -Também é possível habilitar a visualização completa do tabuleiro do computador, útil para testes e verificação do funcionamento do jogo.

## Autor

    Desenvolvido por [Felipe Silva](https://github.com/Felipe0132)
    Projeto acadêmico - Disciplina: Optativa de Python 
    Curso - Engenharia da Computação

## License

    [MIT](https://choosealicense.com/licenses/mit/)