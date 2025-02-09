# SGE_BLOC2

**PAS CONNECT.PY**

![image](https://github.com/user-attachments/assets/ce5bb635-e452-4551-a354-41dbb9dca0c1)

Es fa la trucada a la funció de coonnect a la base de dades Si el resultat es 0, s'ha fet correctament. Per tancar indiquem que la connexió es tanqui amb el següent codi.

![image](https://github.com/user-attachments/assets/0484b2c3-2554-400c-9959-43cc5484fa2d)

La sortida será:

![image](https://github.com/user-attachments/assets/27509157-36e6-4d50-afbb-5784471a2865)



**PAS CREACIÓ I INSERCIÓ DE DADES**

Es fa la trucada a create_tables() del arxiu create_table-to_db per crear la taula a la base de dades (la visualitzarem a pgadmin)

![image](https://github.com/user-attachments/assets/6d37abf3-2b4c-4b6b-908a-609c9bf05b24)

S'executa csv_to_dic.py per tal d'inserir a la taula creada anteriorment, les dades del excel convertit en format .csv

![image](https://github.com/user-attachments/assets/8cc37e4b-8dd7-4ee4-87e4-7ed7875ffcc2)



**PAS INSERCIÓ CREATE_REGISTRE**
![image](https://github.com/user-attachments/assets/af552cc4-2526-4297-b23e-451ecaeb12b2)

**PAS LISTS**

Des del main fem les trucades a read_registre per imprimir tipus i la llista

![img.png](img.png)

El resultat és el següent:

![img_1.png](img_1.png)

Ara des del read_registre probem a imprimir la llista de totes les dades
![img_2.png](img_2.png)

La sortida és:

![img_3.png](img_3.png)

Extreiem el registre de id_cliente = 5

![img_4.png](img_4.png)

I ara imprimirem el telèfon del id_cliente = 5

![img_5.png](img_5.png)

La sortida es la següent:

![img_6.png](img_6.png)

Ara extreurem, per acabar aquest pas, les següents dades:

1. Les dades de l’Andreu
2. El correu de l’Andreu
3. Les dades de la Vivian
4. La direcció de la Vivian
5. Les dades de l’Albert
6. La data de cumpleanys de l’Albert

![img_9.png](img_9.png)

La sortida és la següent:

![img_8.png](img_8.png)


**PAS MAIN.PY**

![img_10.png](img_10.png)

![img_11.png](img_11.png)


**PAS UPDATE.PY**

Modifiquem el teléfon de 3 clients diferents

![img_12.png](img_12.png)

![img_13.png](img_13.png)

![img_15.png](img_15.png)

![img_14.png](img_14.png)

![img_16.png](img_16.png)

![img_17.png](img_17.png)



**PAS DELETE.PY**

Eliminem el registre de 3 clients

![img_20.png](img_20.png)

- Abans de l'eliminació:

  ![img_19.png](img_19.png)

- Desprès de l'eliminació:

    ![img_21.png](img_21.png)

![img_22.png](img_22.png)

- Abans de l'eliminació:

  ![img_23.png](img_23.png)

- Desprès de l'eliminació:

    ![img_24.png](img_24.png)

![img_25.png](img_25.png)

- Abans de l'eliminació:

  ![img_26.png](img_26.png)

- Desprès de l'eliminació:

  ![img_27.png](img_27.png)
