'''
função: avaliar_notas
entrada: Três notas obtidas por um aluno em provas e a média dos exercícios.
saída: conceito (A, B, C ou D)
Restrição: as notas n1, n2 e n3, assim como a média são valores entre 0,0 e 10,0.
'''



def avaliar_notas(n1, n2, n3, media_exercicios):
    if n1 < 0 or n1 > 10:
        raise ValueError('Valor inválido para n1')
    if n2 < 0 or n2 > 10:
        raise ValueError('Valor inválido para n2')
    if n3 < 0 or n3 > 10:
        raise ValueError('Valor inválido para n3')
    if media_exercicios < 0 or media_exercicios > 10:
        raise ValueError('Valor inválido para media_exercicios')

    media_aproveitamento = (n1 + 2*n2 + 3*n3 + media_exercicios)/7
    if media_aproveitamento >= 9.0:
        return 'A'
    elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
        return 'B'
    elif media_aproveitamento >= 6.0 and media_aproveitamento < 7.5:
        return 'C'
    elif media_aproveitamento < 6.0:
        return 'D' 
    
