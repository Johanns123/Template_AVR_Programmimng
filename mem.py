import subprocess
import sys

MCU = sys.argv[1] # ex. atmega328p, attiny

# Nome do arquivo de saída (.elf)
output_elf = "build/main.elf"

# Comando avr-size
avr_size_cmd = ["avr-size", output_elf]

# Executa o comando avr-size
avr_size_output = subprocess.check_output(avr_size_cmd, universal_newlines=True)

# Divide as linhas de saída em uma lista
output_lines = avr_size_output.splitlines()

# Extrai a linha relevante contendo os tamanhos
info_line = output_lines[1]

# Extrai os tamanhos das colunas
text_size = int(info_line.split()[0])
data_size = int(info_line.split()[1])
bss_size = int(info_line.split()[2])

Flash_memory = text_size
data_memory = data_size + bss_size

if MCU == "Atmega328p".lower():
    Total_Flash_memory = 32768 ##bytes
    Total_RAM_memory = 2048 ##bytes

else:
    print("MCU not found")
    Total_Flash_memory = int(input("Write the Flash memory size"))
    Total_RAM_memory = int(input("Write the RAM memory size"))

Flash_percentage = round((float(Flash_memory/Total_Flash_memory)*100), 2)
Data_Memory_percentage = round((float(data_memory)/Total_RAM_memory)*100, 2)

# Exibe os tamanhos das seções
print(f"Flash: {Flash_memory}/{Total_Flash_memory} bytes => {Flash_percentage}%/100%")
print(f"RAM: {data_memory}/{Total_RAM_memory} bytes => {Data_Memory_percentage}%/100%")
