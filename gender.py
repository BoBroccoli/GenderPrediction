from sklearn import tree

#height, weight and shoe size
X = [[180, 80, 44],[187, 90, 46],[177, 70, 43],[160, 60, 38], [175, 64, 39],
[181, 85, 45],[190, 90, 47],[159, 48, 36],[180, 80, 44]]
Y = ['male', 'male', 'male','female','female',
'male','male','female','male']
# *******************Use decision tree classifier***********
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X,Y)
#prediction = clf.predict([[190,90,47]])
#print prediction

# ********************Use naive bayes classifier*********************
#from sklearn.naive_bayes import GaussianNB
#gnb = GaussianNB()
#gnb.fit(X,Y)
#prediction = gnb.predict([[190,90,47]])
#print prediction

# *******************Stochastic Gradient Descent***********
from sklearn.linear_model import SGDClassifier
clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
clf.fit(X,Y)
prediction = clf.predict([[190,90,47]])
print prediction