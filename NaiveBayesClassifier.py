from sklearn.naive_bayes import GaussianNB
X = [[180, 80, 44],[187, 90, 46],[177, 70, 43],[160, 60, 38], [175, 64, 39],
[181, 85, 45],[190, 90, 47],[159, 48, 36],[180, 80, 44]]
Y = ['male', 'male', 'male','female','female',
'male','male','female','male']
gnb = GaussianNB()
gnb.fit(X,Y)
prediction = gnb.predict([[190,90,47]])
print prediction
