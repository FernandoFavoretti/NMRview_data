# NMRview_data

Converte listas .xpk do NMWview em arquivo .csv. 
Ordena os resíduos e atribue os aminoácidos com base em sua sequencia FASTA.

# Como usar

> Instalar python 2.7:

* [Python 2.7.13](https://www.python.org/downloads/release/python-2713/)


```
> Instalar pip:

> (linux) sudo apt-get install python-pip python-dev build-essential 

> Instalar os pacotes necessários

> pip install -r requirements.txt
```

```
Para rodar:

python nvmrview_data.py --file 'local_arquivo_xpk' --names 'local_sec_file'
 
```
