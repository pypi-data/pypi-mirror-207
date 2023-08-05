import geopandas as gpd
import pickle
import pkg_resources
import glob
import os

def get_landsat_paths():
    # Get the directory path for landsat8 tif files 
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'landsat8_dataset'))
    sentinel_paths = glob.glob(os.path.join(dir_path, '*.tif'))
    
    return sentinel_paths
    
def load_train_lcsamples ():
    # Load training land cover samples saved as .geojson file
    filepath = pkg_resources.resource_filename(__name__, 'lc_samples/training_samples.geojson')
    data = gpd.read_file(filepath)
    
    return data

def load_val_lcsamples ():
    # Load validation land cover samples saved as .geojson file
    filepath = pkg_resources.resource_filename(__name__, 'lc_samples/validation_samples.geojson')
    data = gpd.read_file(filepath)

def load_trainedlc_rf():
    # Load the trained random forest model
    filepath = pkg_resources.resource_filename(__name__, 'trained_models/rf_classification_model.sav')
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    
    return model

def load_trained_pca():
    # Load the trained PCA model
    filepath = pkg_resources.resource_filename(__name__, 'trained_models/pca_decomposition_model.sav')
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    
    return model


    
    
 
