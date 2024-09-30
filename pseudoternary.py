import matplotlib.pyplot as plt 

# Função para codificação Pseudoternary
def pseudoternary_encoding(bit_sequence):
    encoded = []
    last_pulse = -1  # Usamos -1 para o primeiro pulso negativo
    
    for bit in bit_sequence:
        if bit == '1':
            encoded.append(0)  # 1 é representado por ausência de pulso
        else:
            # Alterna entre pulsos +1 e -1 para os 0s
            if last_pulse == 1:
                encoded.append(-1)
                last_pulse = -1
            else:
                encoded.append(1)
                last_pulse = 1
    
    return encoded

# Função para desenhar a sequência original e codificada
def plot_sequences(original_sequence, encoded_sequence, title):
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))

    # Adiciona um ponto extra ao final para o gráfico de degraus
    original_sequence = original_sequence + [original_sequence[-1]]
    encoded_sequence = encoded_sequence + [encoded_sequence[-1]]

    # Plot da sequência original (ajustando para gráfico de degraus)
    ax[0].step(range(len(original_sequence)), original_sequence, where='post', label='Sequência Original', color='blue')
    ax[0].set_title('Sequência Original')
    ax[0].set_ylim(-0.1, 1.1)
    ax[0].set_xlim(0, len(original_sequence)-1)
    ax[0].grid(True)

    # Plot da sequência codificada (mantendo step para codificação)
    ax[1].step(range(len(encoded_sequence)), encoded_sequence, where='post', label='Sequência Codificada (Pseudoternary)', color='orange')
    ax[1].set_title('Sequência Codificada (Pseudoternary)')
    ax[1].set_ylim(-1.1, 1.1)
    ax[1].set_xlim(0, len(encoded_sequence)-1)
    ax[1].grid(True)

    # Títulos e exibição
    plt.suptitle(title)
    plt.show()

# Sequências de bits fornecidas
bit_sequence_1 = "1000000001010011"
bit_sequence_2 = "1110100101000010"

# Converte as sequências de string para listas de inteiros
bit_sequence_1_list = [int(bit) for bit in bit_sequence_1]
bit_sequence_2_list = [int(bit) for bit in bit_sequence_2]

# Codifica as sequências usando Pseudoternary
encoded_sequence_1 = pseudoternary_encoding(bit_sequence_1)
encoded_sequence_2 = pseudoternary_encoding(bit_sequence_2)

# Exibe os gráficos
plot_sequences(bit_sequence_1_list, encoded_sequence_1, 'Codificação Pseudoternary - Sequência 1')
plot_sequences(bit_sequence_2_list, encoded_sequence_2, 'Codificação Pseudoternary - Sequência 2')
