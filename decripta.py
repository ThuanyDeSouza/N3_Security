# Decripta
import base64

def decrypt(private_key, message):
  n, d = private_key
  decrypted = []
  for msg in message:
    encodedChunk = pow(int(msg), int(d), int(n))
    decrypted.append(encodedChunk)

  return decrypted

def read_keyfile(keyfile):
  with open(keyfile, 'r') as file:
    lines = []
    for line in file:
      lines.append(line)

  return lines

def int_to_str(n: int) -> str:
  if n == 0:
    string_val = "0"
  else:
    string_val = ""
    while n > 0:
      quot, rem = divmod(n, 256)
      char_num = rem
      string_val += chr(char_num)
      n = quot

  return str(string_val)

def chunk_int_to_base64(int_chunks):
  base64 = ""
  for chunk in int_chunks:
    base64 += int_to_str(chunk)

  return base64

def decrypt_file(keyfile, inputfile, outputfile):
  # Lê o arquivo a ser descriptografado
  with open(inputfile, 'r') as file:
    lines = []
    for line in file:
      lines.append(line)
  # Lê a chave
  private_key = read_keyfile(keyfile)
  # Descriptografa os dados
  decrypted = decrypt(private_key, lines)
  # Converte de inteiro para string
  base64Text = chunk_int_to_base64(decrypted)
  # Converte o base64 para texto
  decoded_bytes = base64.b64decode(base64Text)
  decoded_string = decoded_bytes.decode('utf-8')
  # Escreve o arquivo encriptado
  with open(outputfile, 'w') as file:
    file.write(decoded_string)
  print("Arquivo descriptografado com sucesso!")

if __name__ == '__main__':
  keyfile = input("Qual o arquivo da chave privada? ")
  inputfile = input("Qual o arquivo da mensagem a ser descriptografada? ")
  outputfile = input("Em qual arquivo gerar a mensagem descriptografada? ")

  decrypt_file(keyfile, inputfile, outputfile)