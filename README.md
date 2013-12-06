cidades-br
==========

App em Django com lista de cidades e estados brasileiros com base na última atualização do IBGE em 2010: http://www.cidades.ibge.gov.br/xtras/home.php

Requisitos
--------------
- Python >= 2.6.5
- Django >= 1.4.3
- South >= 0.7.6

Instalação
--------------

- Clone este repositório para junto das outras apps de seu projeto
- Adicone a app ***'localidades'*** na settings INSTALLED_APPS em seu arquivo ***settings.py***
- Execute o comando ***python manage.py migrate localidades***


SQL
--------------
Contém arquivo (localidades_cidade.sql) já pronto para carga MySQL, caso não utilizar Django.


EXCEL
--------------
Contém arquivo (cidades.xlsx) para utilização.
