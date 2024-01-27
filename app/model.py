import streamlit as st

@st.cache_data
def model():

    st.header("Model Analysis")
    st.markdown("---")

    st.subheader("Models tested and their scores:")
    st.write("""
1. K Nearest Neighbours:     0.8333530432040366
2. Logistic Regression:      0.8459476505834121
3. Decision Tree Classifier: 0.7673446862188584
4. LinearSVC: 0.8456125827814569
5. HistGradientBoostingClassifier: 0.8514861242510249
6. BernoulliNB: 0.8170726900031536
7. AdaBoostClassifier: 0.8494165878271839
8. XGBClassifier: 0.8504415011037527
9. RandomForestClassifier: 0.8420845159255755
10. SGDClassifier: 0.8453563544623147
11. Quadratic Discriminant Analysis: 0.7511628823714916
12. Passive Aggressive Classifier: 0.8173289183222958
13. Perceptron: 0.8056803847366761
14. MLPClassifier: 0.8503429517502366
15. NearestCentroid: 0.6991091138442131
16. SVC: 0.8447847682119205
""")
    
    st.write("Since, out of all the models tested, HistGradientBoostingClassifier had the highest initial score and has native support for missing values, it was chosen to be further trained and tested upon.")
    st.markdown("---")

    st.subheader("HistGradientBoostingClassifier Hyper-parameters: ")
    st.write("The HistGradientBoosting model was first exhaustively trained on the following parameters and then 4 more iterations of it were tuned based on the previous models best parameters.")
    st.markdown("""`learning_rate`: float, default = 0.1, best_iter_param = 0.01

The learning rate, also known as shrinkage. This is used as a multiplicative factor for the leaves values. Use 1 for no shrinkage.""")
    st.markdown("""`max_iter`: int, default = 100, best_iter_param = 25

The maximum number of iterations of the boosting process, i.e. the maximum number of trees for binary classification. For multiclass classification, n_classes trees per iteration are built.""")
    st.markdown("""`max_depth`: int or None, default = None, best_iter_param = 2

The maximum depth of each tree. The depth of a tree is the number of edges to go from the root to the deepest leaf. Depth isn’t constrained by default.""")
    st.markdown("""`l2_regularization`: float, default = 0, best_iter_param = 5.0

The L2 regularization parameter. Use 0 for no regularization (default).""")
    st.markdown("""`max_features`: float, default=1.0, best_iter_param = 0.05

Proportion of randomly chosen features in each and every node split. This is a form of regularization, smaller values make the trees weaker learners and might prevent overfitting. If interaction constraints from `interaction_cst` are present, only allowed features are taken into account for the subsampling.""")
    st.markdown("")
    st.markdown("On top of these tuning parameters, the model also had some more hyperparameters assigned. These are:")
    st.markdown("""`n_iter_no_change`: int, default = 10, assigned = 5

Used to determine when to “early stop”. The fitting process is stopped when none of the last n_iter_no_change scores are better than the n_iter_no_change - 1 -th-to-last one, up to some tolerance. Only used if early stopping is performed.""")
    st.markdown("""`class_weight`: dict or ‘balanced’, default=None, assigned = 'balanced'

Weights associated with classes in the form {class_label: weight}. If not given, all classes are supposed to have weight one. The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as n_samples / (n_classes * np.bincount(y)). Note that these weights will be multiplied with sample_weight (passed through the fit method) if sample_weight is specified.""")
    st.markdown("""`random_state`: int, RandomState instance or None, default=None, assigned = 42

Pseudo-random number generator to control the subsampling in the binning process, and the train/validation data split if early stopping is enabled. Pass an int for reproducible output across multiple function calls.""")
    st.markdown("---")

    st.subheader("Evaluation metric of the model")
    st.markdown("The model was evaluated with the `f1_weighted` evaluation rule. [According to the scikit-learn docs, the f1 score is defined as follows:](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score)")
    st.markdown("""Compute the F1 score, also known as balanced F-score or F-measure.

The F1 score can be interpreted as a harmonic mean of the precision and recall, where an F1 score reaches its best value at 1 and worst score at 0. The relative contribution of precision and recall to the F1 score are equal. The formula for the F1 score is:

    F1 = 2 * TP / (2 * TP + FN + FP)

Where “TP” is the number of true positives, “FN” is the number of false negatives, and “FP” is the number of false positives. F1 is by default calculated as 0.0 when there are no true positives, false negatives, nor false positives.""")
    st.markdown("""The `average` parameter was set to `weighted` because the model is trained on multi-classification data. Its function is defined as to:
                
Calculate metrics for each label, and find their average weighted by support (the number of true instances for each label). This alters ‘macro’ to account for label imbalance; it can result in an F-score that is not between precision and recall.""")
