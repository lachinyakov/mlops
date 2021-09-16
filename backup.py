#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os.path as path
import numpy as np
from matplotlib import pyplot as plt
from utils.generator import generator
from keras.models import Sequential
from keras import layers
from keras.optimizers import RMSprop

import mlflow
import mlflow.keras

from mlflow.tracking import MlflowClient
import os

cur_dir = path.curdir
data_dir = "data"
fname = path.join(cur_dir, data_dir, "data.csv")


# In[2]:


f = open(fname)
data = f.read()
f.close()


# In[3]:


lines = data.split('\n')
header =  lines[0].split(',')
lines = lines[1:]
print(header)



# In[4]:


float_data = np.zeros((len(lines), len(header)-1))

for i, line in enumerate(lines):
    values = [float(x) for x in line.split(',')[1:]]
    float_data[i, :] = values

temp = float_data[:, 1]
plt.plot(range(1440), temp[:1440])



mean = float_data[:200000].mean(axis=0)
float_data -= mean
std = float_data[:200000].std(axis=0)
float_data /= std




# In[9]:


lookback = 1440
step = 6
delay = 144
batch_size = 128
train_gen = generator(
    float_data,
    lookback=lookback,
    delay=delay,
    min_index=0,
    max_index=200000,
    shuffle=False,
    step=step,
    batch_size=batch_size
)

val_gen = generator(
    float_data,
    lookback=lookback,
    delay=delay,
    min_index=200001,
    max_index=300000,
    step=step,
    batch_size=batch_size
)

test_gen = generator(
    float_data,
    lookback=lookback,
    delay=delay,
    min_index=300001,
    max_index=None,
    step=step,
    batch_size=batch_size
)

# Сколько нужно обратится к val_gen, что бы получить набор целиком
val_steps = (300000 - 200001 - lookback) // batch_size

# Сколько нужно обратится к test_gen, что бы получить контролььный набор циликом 
test_steps = (len(float_data) - 300001 - lookback) // batch_size



model = Sequential()
model.add(layers.Flatten(input_shape=(lookback // step, float_data.shape[-1])))
model.add(layers.Dense(32,  activation='relu'))
model.add(layers.Dense(1))
model.compile(optimizer=RMSprop(), loss='mae')
history = model.fit_generator(
    train_gen,
    steps_per_epoch=500,
    epochs=20,
    validation_data=val_gen,
    validation_steps=val_steps
)


# In[ ]:


loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss)+1)
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()


# In[16]:



os.environ["MLFLOW_TRACKING_URI"] = "http://127.0.0.1:5000"
os.environ["AWS_ACCESS_KEY_ID"] = "root"
os.environ["AWS_SECRET_ACCESS_KEY"] = "password"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://127.0.0.1:9000"


# In[18]:



# client = MlflowClient()
# experiment_id = client.create_experiment("home test")
# client.set_experiment_tag(experiment_id, "keras", "keras")
# mlflow.end_run()
with mlflow.start_run() as run:
    mlflow.keras.log_model(model, "keras")


# In[1]:





# In[ ]:




