import tkinter as tk
from tkinter import ttk

def create_encoding_scheme():
    """
    Cria um esquema de codificação onde cada caractere é mapeado para um código binário de 7 bits.
    """
    encoding_scheme = {}
    decoding_scheme = {}
    for i in range(128):
        binary_code = format(i, '07b')  # 7-bit binary representation
        char = chr(i)
        encoding_scheme[char] = binary_code
        decoding_scheme[binary_code] = char
    return encoding_scheme, decoding_scheme

def encode_message(message, encoding_scheme):
    """
    Codifica a mensagem usando o esquema de codificação fornecido.
    """
    encoded_message = ' '.join(encoding_scheme[char] for char in message)
    return encoded_message

def decode_message(encoded_message, decoding_scheme):
    """
    Decodifica a mensagem codificada usando o esquema de decodificação fornecido.
    """
    binary_codes = encoded_message.split(' ')
    decoded_message = ''.join(decoding_scheme[code] for code in binary_codes)
    return decoded_message

def encode_decode_message():
    """
    Função para codificar e decodificar a mensagem e exibir os resultados na GUI.
    """
    user_message = entry_message.get()
    encoded_message = encode_message(user_message, encoding_scheme)
    decoded_message = decode_message(encoded_message, decoding_scheme)
    
    label_encoded_message.config(text="Mensagem Codificada: " + encoded_message)
    label_decoded_message.config(text="Mensagem Decodificada: " + decoded_message)

# Criar esquema de codificação e decodificação
encoding_scheme, decoding_scheme = create_encoding_scheme()

# Criar a janela principal da GUI
root = tk.Tk()
root.title("Codificação e Decodificação de Mensagem")
root.geometry("400x200")  # Definir o tamanho da janela

# Estilo para os widgets
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))  # Definir a fonte para os rótulos

# Criar widgets
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

label_instructions = ttk.Label(frame, text="Digite a mensagem para codificação:")
entry_message = ttk.Entry(frame, width=50)
button_encode_decode = ttk.Button(frame, text="Codificar / Decodificar", command=encode_decode_message)
label_encoded_message = ttk.Label(frame, text="")
label_decoded_message = ttk.Label(frame, text="")

# Layout dos widgets
label_instructions.grid(row=0, column=0, columnspan=2, pady=(0, 10))
entry_message.grid(row=1, column=0, columnspan=2, pady=(0, 10))
button_encode_decode.grid(row=2, column=0, columnspan=2, pady=(0, 10))
label_encoded_message.grid(row=3, column=0, columnspan=2, pady=(0, 5))
label_decoded_message.grid(row=4, column=0, columnspan=2)

# Expandir o frame para preencher a janela
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Iniciar o loop principal da GUI
root.mainloop()
