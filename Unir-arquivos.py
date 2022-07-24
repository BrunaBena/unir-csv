#Este código precisa estar localizado na mesma pasta que está os arquivos em csv que você deseja concatenar
#importando as bibliotecas
import os
import pandas as pd

master_df = pd.DataFrame()

#unindo csv de acordo com a inicial do arquivos - neste caso 'ca'
for file in os.listdir(os.getcwd()):
    if file.startswith('ca'):
        master_df = master_df.append(pd.read_csv(file, sep=';'))

#gerar arquivo em csv com o nome concateno -- pode dar o nome que quiser para o arquivo
master_df.to_csv('Concatenado.csv', index=False)