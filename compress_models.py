import gzip
import pickle

# Compress the model files
with open('regmodel.pkl', 'rb') as f_in, gzip.open('regmodel.pkl.gz', 'wb') as f_out:
    f_out.writelines(f_in)

with open('scaling.pkl', 'rb') as f_in, gzip.open('scaling.pkl.gz', 'wb') as f_out:
    f_out.writelines(f_in)
