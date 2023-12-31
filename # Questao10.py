# Questao10

# Esse exemplo simples de implementação utilizando o conjunto de dados Iris para uma tarefa de classificação. Neste exemplo, usaremos o algoritmo KNN para classificar as espécies de flores no conjunto de dados Iris



# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


# Carregando o conjunto de Dados Iris
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target



# Dividindo o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Inicializando o modelo KNN
knn_model = KNeighborsClassifier(n_neighbors=3)



# Treinando o modelo
knn_model.fit(X_train, y_train)



# Fazendo previsões no conjunto de teste
y_pred = knn_model.predict(X_test)



# Avaliando a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)

print(f"Acurácia do modelo: {accuracy:.2f}")



# Exibindo o relatório de classificação
class_report = classification_report(y_test, y_pred, target_names=iris.target_names)

print("Relatório de Classificação:")

print(class_report)