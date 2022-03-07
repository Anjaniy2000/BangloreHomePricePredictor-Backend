import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath, balcony):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("Loading Saved Artifacts.....Start")
    global __data_columns
    global __locations

    with open("ml-data/Columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]  # first 4 columns are sqft, bath, bhk, balcony

    global __model
    if __model is None:
        with open('ml-data/Banglore_Home_Price_Predictor.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading Saved Artifacts.....Done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2, 2))  # other location
