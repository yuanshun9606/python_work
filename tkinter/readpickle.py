import pickle

fi = open('usrs_info.pickle','rb')
listt= pickle.load(fi)
print(listt)
fi.close()