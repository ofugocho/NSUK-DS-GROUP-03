import sys
sys.path.append("..")  

from src.cleaning import clean_yam_data

df_check = clean_yam_data(df_raw)
print(df_check.shape)       
print(df_check.equals(df))