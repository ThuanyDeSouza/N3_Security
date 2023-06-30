# Encripta
import base64

def encrypt(public_key, message):
  n, e = public_key
  encrypted = []
  for msg in message:
    encodedChunk = pow(msg, int(e), int(n))
    encrypted.append(encodedChunk)

  return encrypted

def read_keyfile(keyfile):
  with open(keyfile, 'r') as file:
    lines = []
    for line in file:
      lines.append(line)

    return lines

def base64_to_int_chunk(base64_string, n):
  chunks = [base64_string[i:i+n] for i in range(0, len(base64_string), n)]
  converted = []
  result = 0
  for chunk in chunks:
    for c in reversed(chunk):
      result = result * 256
      result += ord(c)
    converted.append(result)
    result = 0

  return converted

def block_size(n: int) -> int:
  bsize = 0
  temp = n - 1

  while temp > 1:
    temp = int(temp / 2)
    bsize += 1

  return int(bsize/8)

def encrypt_file(keyfile, inputfile, outputfile):
  # Lê o arquivo a ser encriptado
  with open(inputfile, 'r') as file:
      data = file.read()
  # Converte o texto para base64
  data = base64.b64encode(data.encode()).decode()
  # Lê a chave
  public_key = read_keyfile(keyfile)
  # Retorna blocksize de acordo com n
  bs = block_size(int(public_key[0]))
  # Divide o texto de acordo com n e Converte para números longos
  test = base64_to_int_chunk(data, bs)
  # Encriptar dados
  encrypted = encrypt(public_key, test)
  # Escreve o arquivo encriptado
  with open(outputfile, 'w') as file:
    file.write('\n'.join(str(x) for x in encrypted))
  print("Arquivo encriptografado com sucesso!")

if __name__ == '__main__':
  keyfile = input("Qual o arquivo da chave publica? ")
  inputfile = input("Qual o arquivo da mensagem a ser criptografada? ")
  outputfile = input("Em qual arquivo gerar a mensagem criptografada? ")

  encrypt_file(keyfile, inputfile, outputfile)
