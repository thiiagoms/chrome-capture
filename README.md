###  Captura de senhas - Google chrome
####[pt-br]: 

1. Primeiro, faça o download do arquivo através do comando:
   - git clone https://github,com/ekkopy/chrome-capture.git ou baixe o arquivo em .zip e extraia no local de sua preferência.
2. Navegue pelo terminal até o diretório onde você extraiu o arquivo, e crie um virtualenv com o seguinte comando: 
```python
python -m venv cloud
```
3. Após isso, ative seu ambiente virtual da seguinte forma:
 - Para ambientes Linux/Unix: 
 ```python
 source cloud/bin/activate
 ```
 - Para ambientes windows:
```python
 .\cloud\Scripts\activate
 ```
4. Execute o script (lembrando que o navegador não pode estar em execução no momento):
```python
 python chrome_pass.py
 ```
5. Seja feliz :smile:

6. Colabore com um PR :feelsgood:
