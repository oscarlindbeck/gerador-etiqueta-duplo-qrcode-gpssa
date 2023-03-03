# Gerador de etiquetas, duplo qrcode

## Sobre
Este gerador de etiquetas auxiliará na implantação do GPSVista e ferramentas desenvolvidas pela regional Paraná, facilitando e otimizando a geração de qrcodes. São geradas aproximadamente 15 páginas por minuto, com 9 etiquetas e 12 qrcodes, totalizando 8.100 etiquetas e 16.200 qrcodes gerados no período de 1h.

<br>

<div align="center">
  <img height="400" width="266" src="https://github.com/oscarlindbeck/gerador-etiqueta-duplo-qrcode-gpssa/blob/master/src/templates/example.png">
</div>

<br>

## Como utilizar
Após baixar o projeto, no terminal, insira o comando abaixo para que todas as bibliotecas necessárias para que o código rode sejam instaladas.
```
pip install -r requirements.txt
```

<br>

O arquivo *.xlsx* deverá ser inserido na pasta input e as colunas deverão conter a mesma nomenclatura abaixo e em seguida será necessário apenas executar o arquivo *main.py*. O arquivo *.pdf* será salvo na pasta *output*.

#|A          |B        |C
-|-----------|---------|--------------
1|description|link main|link secondary

<br>

Após a utilização sugiro que sejam excluídos os arquivos gerados no diretório *src/png* para que na próxima geração de qrcodes não ocorra nenhum problema na hora de sobreescrever estes arquivos.

## Personalização
O layout poderá ser alterado desde que as posições do qrcode e descrição se mantenham fixas. Na pasta *src/templates* contém o arquivo *.psd* para que as alterações sejam realizadas.

Para que a alteração seja realizada substitua o arquivo *layout.png* no diretório *src/layout*.
