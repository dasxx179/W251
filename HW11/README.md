# Homework 11 -- More fun with OpenAI Gym!

In this homework, a Lunar Lander is trained to land properly using a Jetson TX2. 

There are two python scripts used for this process. The first file, `lunar_lander.py`, defines the Lunar Lander for OpenAI Gym, and it also defines the keras model.

The second file, `run_lunar_lander.py`, instantiates the Lunar Lander environment and runs it.

The code that creates the model in `lunar_lander.py` is:

```
def nnmodel(input_dim):
    model = Sequential()
    model.add(Dense(32, input_dim=input_dim, activation='relu'))
    model.add(Dense(16, activation='sigmoid'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model
```

In this homework, the model parameters and the training parameters (total iterations and threshold) are adjusted to get better results.  

The training parameters are in the `run_lunar_lander.py` file:

```
.
.
.
    model = nnmodel(10)

.
.
.
    training_thr = 3000
    total_itrs = 50000
.
.
.
        if steps > training_thr and steps %1000 ==0:
            # re-train a model
            print("training model model")
            modelTrained = True
            model.fit(np.array(X_train),np.array(y_train).reshape(len(y_train),1), epochs = 10, batch_size=20)
.
.
.

```

To run the environment, the following commands were run using the files in the repository:

```
sudo docker build -t lander -f Dockerfile.lander .
xhost +
sudo docker run -it --rm --net=host --runtime nvidia  -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix:rw --privileged -v /tmp/videos:/tmp/videos lander
```

The objective is to increase the number of successful landings.  The various adjustments are described as below:

## What parameters did you change?

Note the model had 68 original landings.  

### First Change

The structure of the network was changed.  Two additional layers were added with 128 and 64 nodes.  The additional lines were: 

```python
# Original
def nnmodel(input_dim):
    model = Sequential()
    model.add(Dense(32, input_dim=input_dim, activation='relu'))
    model.add(Dense(16, activation='sigmoid'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model
  
# New Model
def nnmodel(input_dim):
    model = Sequential()
    model.add(Dense(32, input_dim=input_dim, activation='relu'))
    model.add(Dense(64, input_dim=input_dim, activation='relu'))
    model.add(Dense(128, input_dim=input_dim, activation='sigmoid'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model
```

The model worsened with 57 landings.  

### Second Change

The model was changed from 50000 iterations to 100000 iterations.  

This was reflected with the change: 

```
total_itrs = 100000
```

This resulted in the landings increasing to 117.  This beats the default model.  

### Third Change

I changed the final activation function from 'sigmoid' to 'linear'.  

```python
model.add(Dense(128, input_dim=input_dim, activation='linear'))
```



## What values did you try?

I tried changing the number of iterations by doubling it from 50000 to 100000.  I also tried changing the batch size from 20 to 64.  

## Did you try any other changes?

I changed the activation function of the final layer from 'sigmoid' to 'linear'.  This did not help, and it worsened the model by changing the total number of landings to 25.  

### Did they improve or degrade the model?

The activation function change worsened the model.  I experimented with this change by incorporating it with the addition of the two layers to the model, and the total number of landings decreased to 25.  

## What conclusions can you draw about the different parameters?

In conclusion, changing the activation function from relu to linear results in a worse performance.  Furthermore, adding extra layers with more nodes also did not help.  Most likely, the model began to experience overfitting with the addition of these nodes.  Lastly, the successful attempt that resulted in a better performance than the default model is intuitive: changing the number of iterations from 50000 to 100000.  A greater training time of the default parameters resulted in better performance.  

The videos are stored in Cloud Object Storage.  The link to the bucket is here:

[Bucket Link](https://w251-bucket-sayan.s3.us-south.cloud-object-storage.appdomain.cloud)