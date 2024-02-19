import subprocess
import sys
import pandas as pd

df = pd.read_csv("AVR_dataframe.csv")

df = df.map(lambda x: str(x).lower())  ##df in lower casa

MCU = sys.argv[1] # ex. atmega328p, attiny

# # Nome do arquivo de saída (.elf)
output_elf = "build/main.elf"

# # Comando avr-size
avr_size_cmd = ["avr-size", output_elf]

# # Executa o comando avr-size
avr_size_output = subprocess.check_output(avr_size_cmd, universal_newlines=True)

# # Divide as linhas de saída em uma lista
output_lines = avr_size_output.splitlines()

# # Extrai a linha relevante contendo os tamanhos
info_line = output_lines[1]

# # Extrai os tamanhos das colunas
text_size = int(info_line.split()[0])
data_size = int(info_line.split()[1])
bss_size = int(info_line.split()[2])

Flash_memory = text_size
data_memory = data_size + bss_size

MCU_data = df[(df["MCU Name"] == MCU.lower())]

Total_Flash_memory = (MCU_data["Flash Memory (KB)"].values)
Total_Flash_memory = int(Total_Flash_memory[0])*1024
Total_RAM_memory = (MCU_data["RAM Memory (KB)"].values)
Total_RAM_memory = int(float(Total_RAM_memory[0])*1024)

Flash_percentage = round((float(Flash_memory/Total_Flash_memory)*100), 2)
Data_Memory_percentage = round((float(data_memory)/Total_RAM_memory)*100, 2)

# Exibe os tamanhos das seções
print(f"Flash: {Flash_memory}/{Total_Flash_memory} bytes => {Flash_percentage}%/100%")
print(f"RAM: {data_memory}/{Total_RAM_memory} bytes => {Data_Memory_percentage}%/100%")



# print(df["MCU Name"])

# MCU = "ATmega328P"


# print(Total_Flash_memory)
# print(Total_RAM_memory)