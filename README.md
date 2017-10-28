# NMRview_data

Converte listas .xpk do NMWview em arquivo .csv. 
Ordena os resíduos e atribue os aminoácidos com base em sua sequencia FASTA.

# Como usar

> Instalar GIT (https://git-scm.com/download/win)

> Clonar esse repositorio:

```
> git clone https://github.com/FernandoFavoretti/NMRview_data.git
```


> Instalar python 2.7:

* [Python 2.7.13](https://www.python.org/downloads/release/python-2713/)


> Instalar pip:


```
> sudo apt-get install python-pip python-dev build-essential 

ou rodar o arquivo get-pip.py nesse local

> python get-pip.py
```

> Instalar os pacotes necessários
```
> pip install -r requirements.txt
```

> Para Rodar:
```
python nvmrview_data.py --file 'local_arquivo_xpk' --names 'local_sec_file'
 
```
