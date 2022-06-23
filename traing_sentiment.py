
from text_preprocess.text_pre import text_processing
from data_ingestion.data_loader import Get_data
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from best_find_model.touner import model_finder
from file_operation.file_methods import file_operations


le = LabelEncoder()
df = Get_data('train/train.csv').getdata()
df["sentiment"] = le.fit_transform(df["sentiment"])

t = text_processing()
normalize_data = t.text_preprocese(df['review'])
cv = CountVectorizer(binary=False)
model = model_finder()
cv_train_feature = cv.fit_transform(normalize_data)
cv_tranfomer = file_operations().save_model(cv,'tran')
lg_model = model.get_best_param_logistic(cv_train_feature,df['sentiment'])
save_model = file_operations().save_model(lg_model,filename='logis')

