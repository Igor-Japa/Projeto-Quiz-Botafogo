perguntas = {
    'Pergunta 1': {
        'pergunta': 'Em que ano foi o primeiro título de futebol do Botafogo?',
        'respostas': {
            'a': 1942,
            'b': 1907,
            'c': 1910,
            'd': 1894
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quantos títulos de Brasileirão o Botafogo possuí?',
        'respostas': {
            'a': 5,
            'b': 1,
            'c': 3,
            'd': 2,
        },
        'resposta_certa': 'd',
    },
    'Pergunta 3': {
        'pergunta': 'Em que ano foi o primeiro título do Brasileirão do Botafogo?',
        'respostas': {
            'a': 1910,
            'b': 1962,
            'c': 1968,
            'd': 1946,
        },
        'resposta_certa': 'c',
    },
}
acertos = 0
tentativas = 3
for pk, pv in perguntas.items():
    resp = False
    verificacao = True
    while verificacao:
        chance = True
        print(f'{pk}\n {pv["pergunta"]}\n')
        for rk, rv in pv["respostas"].items():
            print(f'{rk}) {rv}')
        resp = input('Qual é a alternativa certa?')
        if resp != 'a' and resp != 'b' and resp != 'c' and resp != 'd':
            verificacao = True
            print('O que foi digitado não é valido!')
        else:
            verificacao = False
            if resp == pv['resposta_certa']:
                print('Parabéns você sabe muito sobre o Glorioso!')
                acertos += 1
            else:
                print('Resposta incorreta!')
                while chance:
                    chance = input('Quer tentar outra alternativa?[S] ou [N]')
                    if chance == 'S' or chance == 's':
                        verificacao = True
                        chance = False
                        tentativas += 1
                    elif chance == 'N' or chance == 'n':
                        chance = False
                    else:
                        print('Digite apenas "S" para sim e "N" para não!')
                        chance = True
print(f'Você acertou {acertos} em {tentativas} chances!\nSua porcentagem de acertos foi {(acertos/tentativas)*100}%!')
