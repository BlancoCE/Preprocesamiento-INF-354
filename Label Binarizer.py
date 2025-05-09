#Similar a One Hot Encoder pero específico para etiquetas de destino (target). Convierte etiquetas multiclase en formato binario.
#Ejemplo sin librerías:
def label_binarizer(labels, classes=None):
    if classes is None:
        classes = list(set(labels))
    return [[1 if label == cls else 0 for cls in classes] for label in labels]

etiquetas = ['gato', 'perro', 'pájaro', 'perro']
binarized = label_binarizer(etiquetas)
print(binarized)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
