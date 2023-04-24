import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError('List must contain nine numbers.')
  list_array = np.array(list).reshape(3,3)
  calculations={'mean':[list_array.mean(axis =0).tolist(),list_array.mean(axis =1).tolist(),list_array.mean()],
'variance':[list_array.var(axis =0).tolist(),
list_array.var(axis=1).tolist(),list_array.var()],
'standard deviation':[list_array.std(axis =0).tolist(),list_array.std(axis =1).tolist(),list_array.std()],
'max':[list_array.max(axis=0).tolist(),list_array.max(axis =1).tolist(),list_array.max()],
'min':[list_array.min(axis =0).tolist(),list_array.min(axis =1).tolist(),list_array.min()],
'sum':[list_array.sum(axis =0).tolist(),list_array.sum(axis =1).tolist(),list_array.sum()]}
  return calculations