# from sklearn improt *
# iris = datasets.load_iris()
# digits =datasets.load_digits()

# print digits.data
from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)  




import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0])

y[0]