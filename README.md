# Practica LLM

Informacion temporal para el desarrollo:

Aqui hay muchos datasets recogidos

https://huggingface.co/datasets/intelli-zen/spam_detect

## Integrantes del grupo:
- David Gil Vacas
- Nicolas Fernadez
- Nestor Villa Perez

## Librerias usadas:

- **openai**: En vez de hacer las request en crudo, usamos el sdk de openai, ademas este sdk se esta convirtiendo en un standard ya que muchas plataformas hacen su servicio compatible con el sdk de openai, como gemini, deepseek, huggingface...
- **pandas**: Para cargar los datasets, y para analizar las respuestas de la ia.
- **time**: Lo usamos para un sleep por si acaso las APIS publicas nos banean.
- **re**: Usamos regex, para formatear la respuesta de la IA

## APIS / MODELOS USADOS:

- Usamos gemini a traves del sdk de openai
- Usamos ollama a traves del sdk de openai, el servidor de ollama esta hosteado en mi pc, comporta el usuario y contrasena, pero no garantizo que este funcionando 24/7.

## Objetivo:

Dectectar si un mensaje es spam o si no es spam

## Datos:

Hemos usado 10 fuentes de datos diferentes: 

#### 1 - [Kaggle sms](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset?resource=download)
#### 2 - [Enron](https://github.com/MWiechmann/enron_spam_data)
#### 3 - [Kaggle mails](https://www.kaggle.com/datasets/venky73/spam-mails-dataset)
#### 4 - [Hugging face](https://huggingface.co/datasets/Deysi/spam-detection-dataset)
#### 5 - [Datacamp](https://www.datacamp.com/datalab/datasets/dataset-r-sms-spam-collection)
#### 6 - [Spamassassin](https://spamassassin.apache.org/old/publiccorpus/)
#### 7 - [Ling-Spam Dataset](https://www.kaggle.com/datasets/mandygu/lingspam-dataset)
#### 8 - [Spam and Ham Classification Balanced Dataset](https://www.kaggle.com/datasets/zubairmustafa/spam-and-ham-classification-balanced-dataset)
#### 9 - [YouTube Spam Collection Data Set, Eminem](https://www.kaggle.com/datasets/lakshmi25npathi/images)
#### 10 - [Enron subset](https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset)