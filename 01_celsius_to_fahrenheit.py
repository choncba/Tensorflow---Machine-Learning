# Ejemplo de modelo de machine learning para convertir grados Farenheit a Celsius
# La fórmula de cálculo es F = C * 1.8 + 32, pero el modelo la calcula en base a los
# valores de entrada y salida dados

# %%
# Importo dependencias
import tensorflow as tf
import numpy as np
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# %%
# Cargo los datos de entrenamiento del modelo
celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float) # Entrada
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float) # Salida

for i,c in enumerate(celsius_q):
  print("{} degrees Celsius = {} degrees Fahrenheit".format(c, fahrenheit_a[i]))

# %%
# Creo el modelo
# Creo el Layer 0, utilizo Keras y una red neuronal Dense
l0 = tf.keras.layers.Dense(units=1,         # Especifica una única neurona 
                           input_shape=[1]  # Especifica que la entrada es un unico valor
                           ) 
# Ensamblo el layer en el modelo 
model = tf.keras.Sequential([l0])

# %%
# Compilo el modelo
model.compile(loss='mean_squared_error',                # Loss function
              optimizer=tf.keras.optimizers.Adam(0.1)   # Optimizer
              )

# %%
# Entreno el modelo
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")

# %%
# Muestro estadísticas del entrenamiento
import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])

# %%
# Uso el modelo para predecir un valor
print(model.predict([100.0]))

# %%
# Muestro las variables generadas por el modelo
print("These are the layer variables: {}".format(l0.get_weights()))

# %%
# A modo de prueba, repito el entrenamiento agregando más layers
l0 = tf.keras.layers.Dense(units=4, input_shape=[1])
l1 = tf.keras.layers.Dense(units=4)
l2 = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([l0, l1, l2])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")
print(model.predict([100.0]))
print("Model predicts that 100 degrees Celsius is: {} degrees Fahrenheit".format(model.predict([100.0])))
print("These are the l0 variables: {}".format(l0.get_weights()))
print("These are the l1 variables: {}".format(l1.get_weights()))
print("These are the l2 variables: {}".format(l2.get_weights())) 
# %%
