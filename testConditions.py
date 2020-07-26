import sys
import MongoDBUtils
import json
import tensorflow as tf
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import requests

class Learner():
    df: any
    BATCH_SIZE = 256
    BUFFER_SIZE = 10000

    train_univariate = tf.data.Dataset.from_tensor_slices((x_train_uni, y_train_uni))
    train_univariate = train_univariate.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

    val_univariate = tf.data.Dataset.from_tensor_slices((x_val_uni, y_val_uni))
    val_univariate = val_univariate.batch(BATCH_SIZE).repeat()
    def __init__(self):
        self.runUni(self)

    

    def runUni(self):
        mpl.rcParams['figure.figsize'] = (8, 6)
        mpl.rcParams['axes.grid'] = False
        mongo = MongoDBUtils.MongoUtils()
        mongo.connect()
        mongo.connectToCollectino("dev","bitcoin")


        values = mongo.getAll()
        VMKPT = list(values)[0]
        self.df = pd.DataFrame(data=VMKPT)
        df = self.df


        print(df.tail())
        TRAIN_SPLIT = 1800
        tf.random.set_seed(13)
        
        uni_data = df['prices']
        uni_data.index = df['timestamps']
        uni_data.tail()

        uni_data.plot(subplots=True)
        uni_data = uni_data.values
        #It is important to scale features before training a neural network. Standardization is a common way of doing this scaling by subtracting the mean and dividing by the standard deviation of each feature.You could also use a tf.keras.utils.normalize method that rescales the values into a range of [0,1].
        #Note: The mean and standard deviation should only be computed using the training data.

        # [ ]
        uni_train_mean = uni_data[:TRAIN_SPLIT].mean()
        uni_train_std = uni_data[:TRAIN_SPLIT].std()


        # [ ]
        uni_data = (uni_data-uni_train_mean)/uni_train_std

        univariate_past_history = 20
        univariate_future_target = 0

        x_train_uni, y_train_uni = self.univariate_data(uni_data, 0, TRAIN_SPLIT,
                                                univariate_past_history,
                                                univariate_future_target)
        x_val_uni, y_val_uni = self.univariate_data(uni_data, TRAIN_SPLIT, None,
                                            univariate_past_history,
                                            univariate_future_target)

        # [ ]
        print ('Single window of past history')
        print (x_train_uni[0])
        print ('\n Target temperature to predict')
        print (y_train_uni[0])
        show_plot([x_train_uni[0], y_train_uni[0], baseline(x_train_uni[0])], 0,
            'Baseline Prediction Example')


    # Let's now use tf.data to shuffle, batch, and cache the dataset.
    

        
    def create_time_steps(length):
      return list(range(length, 0))
    def show_plot(plot_data, delta, title):
        labels = ['History', 'True Future', 'Model Prediction']
        marker = ['.-', 'rx', 'go']
        time_steps = create_time_steps(plot_data[0].shape[0])
        if delta:
            future = delta
        else:
            future = 0

        plt.title(title)
        for i, x in enumerate(plot_data):
            if i:
                plt.plot(future, plot_data[i], marker[i], markersize=10,
                        label=labels[i])
            else:
                plt.plot(time_steps, plot_data[i].flatten(), marker[i], label=labels[i])
                plt.legend()
                plt.xlim([time_steps[0], (future+5)*2])
                plt.xlabel('Time-Step')
        return plt

    def baseline(history):
      return np.mean(history)
    def univariate_data(dataset, start_index, end_index, history_size, target_size):
        data = []
        labels = []

        start_index = start_index + history_size
        if end_index is None:
            end_index = len(dataset) - target_size

        for i in range(start_index, end_index):
            indices = range(i-history_size, i)
            # Reshape data from (history_size,) to (history_size, 1)
            data.append(np.reshape(dataset[indices], (history_size, 1)))
            labels.append(dataset[i+target_size])
        return np.array(data), np.array(labels)
    def create_time_steps(length):
      return list(range(-length, 0))
    def show_plot(plot_data, delta, title):
        labels = ['History', 'True Future', 'Model Prediction']
        marker = ['.-', 'rx', 'go']
        time_steps = create_time_steps(plot_data[0].shape[0])
        if delta:
            future = delta
        else:
            future = 0

        plt.title(title)
        for i, x in enumerate(plot_data):
            if i:
                plt.plot(future, plot_data[i], marker[i], markersize=10,
                    label=labels[i])
            else:
                plt.plot(time_steps, plot_data[i].flatten(), marker[i], label=labels[i])
            plt.legend()
            plt.xlim([time_steps[0], (future+5)*2])
            plt.xlabel('Time-Step')
        return plt
        show_plot([x_train_uni[0], y_train_uni[0]], 0, 'Sample Example')
# Baseline
# let's first set a simple baseline. Given an input point, the baseline method looks at all the history and predicts the next point to be the average of the last 20 observations.

Learner()
    # def baseline(history):
    #     return np.mean(history)




# import tensorflow as tf
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
# import os
# import pandas as pd
# import requests
# mpl.rcParams['figure.figsize'] = (8, 6)
# mpl.rcParams['axes.grid'] = False




# df.tail()



# TRAIN_SPLIT = 1800
# #Setting seed to ensure reproducibility.
# tf.random.set_seed(13)
# #univariate on price



 
# show_plot([x_train_uni[0], y_train_uni[0]], 0, 'Sample Example')
# # Baseline
# # let's first set a simple baseline. Given an input point, the baseline method looks at all the history and predicts the next point to be the average of the last 20 observations.

# def baseline(history):
#   return np.mean(history)

# show_plot([x_train_uni[0], y_train_uni[0], baseline(x_train_uni[0])], 0,
#            'Baseline Prediction Example')


# # Let's now use tf.data to shuffle, batch, and cache the dataset.
# BATCH_SIZE = 256
# BUFFER_SIZE = 10000

# train_univariate = tf.data.Dataset.from_tensor_slices((x_train_uni, y_train_uni))
# train_univariate = train_univariate.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

# val_univariate = tf.data.Dataset.from_tensor_slices((x_val_uni, y_val_uni))
# val_univariate = val_univariate.batch(BATCH_SIZE).repeat()
# # The following visualisation should help you understand how the data is represented after batching.

# # Time Series

# # You will see the LSTM requires the input shape of the data it is being given.

# simple_lstm_model = tf.keras.models.Sequential([
#     tf.keras.layers.LSTM(8, input_shape=x_train_uni.shape[-2:]),
#     tf.keras.layers.Dense(1)
# ])

# simple_lstm_model.compile(optimizer='adam', loss='mae')

# for x, y in val_univariate.take(1):
#     print(simple_lstm_model.predict(x).shape)

# EVALUATION_INTERVAL = 200
# EPOCHS = 10

# simple_lstm_model.fit(train_univariate, epochs=EPOCHS,
#                       steps_per_epoch=EVALUATION_INTERVAL,
#                       validation_data=val_univariate, validation_steps=50)
# # Predict using the simple LSTM model
# # Now that you have trained your simple LSTM, let's try and make a few predictions.
# for x, y in val_univariate.take(3):
#   plot = show_plot([x[0].numpy(), y[0].numpy(),
#                     simple_lstm_model.predict(x)[0]], 0, 'Simple LSTM model')
#   plot.show()
# # This looks better than the baseline. Now that you have seen the basics, let's move on to part two, where you will work with a multivariate time series.

# # Part 2: Forecast a multivariate time series
# # The original dataset contains fourteen features. For simplicity, this section considers only three of the original fourteen. The features used are air temperature, atmospheric pressure, and air density.

# # To use more features, add their names to this list.

# features_considered = ['prices', 'total_volumes', 'market_caps']

# features = df[features_considered]
# features.index = df['timestamps']
# features.head()

# features.plot(subplots=True)

# dataset = features.values
# data_mean = dataset[:TRAIN_SPLIT].mean(axis=0)
# data_std = dataset[:TRAIN_SPLIT].std(axis=0)

# dataset = (dataset-data_mean)/data_std

# def multivariate_data(dataset, target, start_index, end_index, history_size,
#                       target_size, step, single_step=False):
#   data = []
#   labels = []

#   start_index = start_index + history_size
#   if end_index is None:
#     end_index = len(dataset) - target_size

#   for i in range(start_index, end_index):
#     indices = range(i-history_size, i, step)
#     data.append(dataset[indices])

#     if single_step:
#       labels.append(target[i+target_size])
#     else:
#       labels.append(target[i:i+target_size])

#   return np.array(data), np.array(labels)


# past_history = 720
# future_target = 72
# STEP = 6

# x_train_single, y_train_single = multivariate_data(dataset, dataset[:, 1], 0,
#                                                 TRAIN_SPLIT, past_history,
#                                                 future_target, STEP,
#                                                 single_step=True)
# x_val_single, y_val_single = multivariate_data(dataset, dataset[:, 1],
#                                             TRAIN_SPLIT, None, past_history,

# print ('Single window of past history : {}'.format(x_train_single[0].shape))

# train_data_single = tf.data.Dataset.from_tensor_slices((x_train_single, y_train_single))
# train_data_single = train_data_single.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

# val_data_single = tf.data.Dataset.from_tensor_slices((x_val_single, y_val_single))
# val_data_single = val_data_single.batch(BATCH_SIZE).repeat()

# single_step_model = tf.keras.models.Sequential()
# single_step_model.add(tf.keras.layers.LSTM(32,
#                                         input_shape=x_train_single.shape[-2:]))
# single_step_model.add(tf.keras.layers.Dense(1))

# single_step_model.compile(optimizer=tf.keras.optimizers.RMSprop(), loss='mae')

# for x, y in val_data_single.take(1):
# print(single_step_model.predict(x).shape)

# single_step_history = single_step_model.fit(train_data_single, epochs=EPOCHS,
#                                             steps_per_epoch=EVALUATION_INTERVAL,
#                                             validation_data=val_data_single,
#                                             validation_steps=50)

# def plot_train_history(history, title):
# loss = history.history['loss']
# val_loss = history.history['val_loss']

# epochs = range(len(loss))

# plt.figure()

# plt.plot(epochs, loss, 'b', label='Training loss')
# plt.plot(epochs, val_loss, 'r', label='Validation loss')


# plot_train_history(single_step_history,
#                 'Single Step Training and validation loss')
# Predict a single step future


# for x, y in val_data_single.take(3):
# plot = show_plot([x[0][:, 1].numpy(), y[0].numpy(),
#                     single_step_model.predict(x)[0]], 12,
#                 'Single Step Prediction')
# plot.show()

# future_target = 72
# x_train_multi, y_train_multi = multivariate_data(dataset, dataset[:, 1], 0,
#                                                 TRAIN_SPLIT, past_history,
#                                                 future_target, STEP)
# x_val_multi, y_val_multi = multivariate_data(dataset, dataset[:, 1],
#                                             TRAIN_SPLIT, None, past_history,
#                                             future_target, STEP)

# print ('Single window of past history : {}'.format(x_train_multi[0].shape))
# print ('\n Target temperature to predict : {}'.format(y_train_multi[0].shape))

# train_data_multi = tf.data.Dataset.from_tensor_slices((x_train_multi, y_train_multi))
# train_data_multi = train_data_multi.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

# val_data_multi = tf.data.Dataset.from_tensor_slices((x_val_multi, y_val_multi))
# val_data_multi = val_data_multi.batch(BATCH_SIZE).repeat()
# Plotting a sample data-point.


# def multi_step_plot(history, true_future, prediction):
# plt.figure(figsize=(12, 6))
# num_in = create_time_steps(len(history))
# num_out = len(true_future)

# plt.plot(num_in, np.array(history[:, 1]), label='History')
# plt.plot(np.arange(num_out)/STEP, np.array(true_future), 'bo',
#         label='True Future')
# if prediction.any():
#     plt.plot(np.arange(num_out)/STEP, np.array(prediction), 'ro',

# for x, y in train_data_multi.take(1):
# multi_step_plot(x[0], y[0], np.array([0]))

# multi_step_model = tf.keras.models.Sequential()
# multi_step_model.add(tf.keras.layers.LSTM(32,
#                                         return_sequences=True,
#                                         input_shape=x_train_multi.shape[-2:]))
# multi_step_model.add(tf.keras.layers.LSTM(16, activation='relu'))
# multi_step_model.add(tf.keras.layers.Dense(72))

# multi_step_model.compile(optimizer=tf.keras.optimizers.RMSprop(clipvalue=1.0), loss='mae')
# Let's see how the model predicts before it trains.


# for x, y in val_data_multi.take(1):
# print (multi_step_model.predict(x).shape)

# multi_step_history = multi_step_model.fit(train_data_multi, epochs=EPOCHS,
#                                         steps_per_epoch=EVALUATION_INTERVAL,
#                                         validation_data=val_data_multi,
#                                         validation_steps=50)

# plot_train_history(multi_step_history, 'Multi-Step Training and validation loss')
# # Predict a multi-step future
# # Let's now have a look at how well your network has learnt to predict the future.

# # [ ]
# for x, y in val_data_multi.take(3):
# multi_step_plot(x[0], y[0], multi_step_model.predict(x)[0])
# # Next steps
# # This tutorial was a quick introduction to time series forecasting using an RNN. You may now try to predict the stock market and become a billionaire.

# # In addition, you may also write a generator to yield data (instead of the uni/multivariate_data function), which would be more memory efficient. You may also check out this time series windowing guide and use it in this tutorial.

# # For further understanding, you may read Chapter 15 of Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow, 2nd Edition and Chapter 6 of Deep Learning with Python.

# # Loading...





#     # def univariate_data(dataset, start_index, end_index, history_size, target_size):
#     #     data = []
#     #     labels = []

#     #     start_index = start_index + history_size
# #     if end_index is None:
# #         end_index = len(dataset) - target_size

#     #     for i in range(start_index, end_index):
#     #         indices = range(i-history_size, i)
#     #         # Reshape data from (history_size,) to (history_size, 1)
#     #         data.append(np.reshape(dataset[indices], (history_size, 1)))
#     #         labels.append(dataset[i+target_size])
#     #     return np.array(data), np.array(labels)

#     # features_considered = ['prices', 'total_volumes', 'market_caps']
#     # features = df[features_considered]
#     # features.index = df['timestamps']
#     # features.head()
#     # features.plot(subplots=True)