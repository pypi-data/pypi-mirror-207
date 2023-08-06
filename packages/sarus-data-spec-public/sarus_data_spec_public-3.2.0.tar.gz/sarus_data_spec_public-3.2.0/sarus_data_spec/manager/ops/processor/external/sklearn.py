from __future__ import annotations

from typing import Any

try:
    from sklearn import (
        cluster,
        compose,
        decomposition,
        ensemble,
        impute,
        inspection,
        linear_model,
        metrics,
        model_selection,
        pipeline,
        preprocessing,
        svm,
    )
except ModuleNotFoundError:
    pass  # error message in typing.py


async def model_fit(model: Any, *args: Any, **kwargs: Any) -> Any:
    fitted_model = model.fit(*args, **kwargs)
    return fitted_model


async def sk_get_n_splits(model: Any, *args: Any, **kwargs: Any) -> Any:
    return model.split(*args, **kwargs)


async def sk_inverse_transform(model: Any, *args: Any, **kwargs: Any) -> Any:
    return model.inverse_transform(*args, **kwargs)


async def sk_predict(model: Any, *args: Any, **kwargs: Any) -> Any:
    return model.predict(*args, **kwargs)


async def sk_predict_log_proba(model: Any, *args: Any, **kwargs: Any) -> Any:
    return model.predict_log_proba(*args, **kwargs)


async def sk_predict_proba(model: Any, *args: Any, **kwargs: Any) -> Any:
    return model.predict_proba(*args, **kwargs)


async def sk_split(model: Any, *args: Any, **kwargs: Any) -> Any:
    return model.split(*args, **kwargs)


async def sk_score(model: Any, *args: Any, **kwargs: Any) -> Any:
    return model.score(*args, **kwargs)


async def sk_transform(model: Any, *args: Any, **kwargs: Any) -> Any:
    return model.transform(*args, **kwargs)


async def sk_scale(val: Any, *args: Any, **kwargs: Any) -> Any:
    return preprocessing.scale(val, *args, **kwargs)


async def sk_cross_val_score(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return model_selection.cross_val_score(*args, **kwargs)


async def sk_train_test_split(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return model_selection.train_test_split(*args, **kwargs)


# metrics


async def sk_accuracy_score(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.accuracy_score(*args, **kwargs)


async def sk_average_precision_score(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.average_precision_score(*args, **kwargs)


async def sk_classification_report(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.classification_report(*args, **kwargs)


async def sk_confusion_matrix(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.confusion_matrix(*args, **kwargs)


async def sk_f1_score(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.f1_score(*args, **kwargs)


async def sk_plot_confusion_matrix(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.plot_confusion_matrix(*args, **kwargs)


async def sk_precision_recall_curve(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.precision_recall_curve(*args, **kwargs)


async def sk_precision_score(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.precision_score(*args, **kwargs)


async def sk_recall_score(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.recall_score(*args, **kwargs)


async def sk_roc_auc_score(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.roc_auc_score(*args, **kwargs)


async def sk_auc(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.auc(*args, **kwargs)


async def sk_roc_curve(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.roc_curve(*args, **kwargs)


async def sk_plot_roc_curve(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.plot_roc_curve(*args, **kwargs)


async def sk_plot_precision_recall_curve(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return metrics.plot_precision_recall_curve(*args, **kwargs)


async def sk_label_encoder_fit_transform(
    model: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    X_transformed = model.fit_transform(*args, **kwargs)
    return X_transformed


async def sk_permutation_importance(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return inspection.permutation_importance(*args, **kwargs)


async def sk_pipeline(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return pipeline.Pipeline(*args, **kwargs)


async def sk_function_transformer(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return preprocessing.FunctionTransformer(*args, **kwargs)


async def sk_column_transformer(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return compose.ColumnTransformer(*args, **kwargs)


async def sk_time_series_split(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return model_selection.TimeSeriesSplit(*args, **kwargs)


async def sk_simple_imputer(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return impute.SimpleImputer(*args, **kwargs)


async def sk_linear_regression(
    *args: Any,
    **kwargs: Any,
) -> Any:
    return linear_model.LinearRegression(*args, **kwargs)


async def sk_svc(*args: Any, **kwargs: Any) -> Any:
    return svm.SVC(*args, **kwargs)


async def sk_onehot(*args: Any, **kwargs: Any) -> Any:
    return preprocessing.OneHotEncoder(*args, **kwargs)


async def sk_label_encoder(*args: Any, **kwargs: Any) -> Any:
    return preprocessing.LabelEncoder(*args, **kwargs)


async def sk_pca(*args: Any, **kwargs: Any) -> Any:
    return decomposition.PCA(*args, **kwargs)


async def sk_affinity_propagation(*args: Any, **kwargs: Any) -> Any:
    return cluster.AffinityPropagation(*args, **kwargs)


async def sk_agglomerative_clustering(*args: Any, **kwargs: Any) -> Any:
    return cluster.AgglomerativeClustering(*args, **kwargs)


async def sk_birch(*args: Any, **kwargs: Any) -> Any:
    return cluster.Birch(*args, **kwargs)


async def sk_dbscan(*args: Any, **kwargs: Any) -> Any:
    return cluster.DBSCAN(*args, **kwargs)


async def sk_feature_agglomeration(*args: Any, **kwargs: Any) -> Any:
    return cluster.FeatureAgglomeration(*args, **kwargs)


async def sk_kmeans(*args: Any, **kwargs: Any) -> Any:
    return cluster.KMeans(*args, **kwargs)


async def sk_minibatch_kmeans(*args: Any, **kwargs: Any) -> Any:
    return cluster.MiniBatchKMeans(*args, **kwargs)


async def sk_mean_shift(*args: Any, **kwargs: Any) -> Any:
    return cluster.MeanShift(*args, **kwargs)


async def sk_optics(*args: Any, **kwargs: Any) -> Any:
    return cluster.OPTICS(*args, **kwargs)


async def sk_spectral_clustering(*args: Any, **kwargs: Any) -> Any:
    return cluster.SpectralClustering(*args, **kwargs)


async def sk_spectral_biclustering(*args: Any, **kwargs: Any) -> Any:
    return cluster.SpectralBiclustering(*args, **kwargs)


async def sk_spectral_coclustering(*args: Any, **kwargs: Any) -> Any:
    return cluster.SpectralCoclustering(*args, **kwargs)


async def sk_adaboost_classifier(*args: Any, **kwargs: Any) -> Any:
    return ensemble.AdaBoostClassifier(*args, **kwargs)


async def sk_adaboost_regressor(*args: Any, **kwargs: Any) -> Any:
    return ensemble.AdaBoostRegressor(*args, **kwargs)


async def sk_bagging_classifier(*args: Any, **kwargs: Any) -> Any:
    return ensemble.BaggingClassifier(*args, **kwargs)


async def sk_bagging_regressor(*args: Any, **kwargs: Any) -> Any:
    return ensemble.BaggingRegressor(*args, **kwargs)


async def sk_extra_trees_classifier(*args: Any, **kwargs: Any) -> Any:
    return ensemble.ExtraTreesClassifier(*args, **kwargs)


async def sk_extra_trees_regressor(*args: Any, **kwargs: Any) -> Any:
    return ensemble.ExtraTreesRegressor(*args, **kwargs)


async def sk_gradient_boosting_classifier(*args: Any, **kwargs: Any) -> Any:
    return ensemble.GradientBoostingClassifier(*args, **kwargs)


async def sk_gradient_boosting_regressor(*args: Any, **kwargs: Any) -> Any:
    return ensemble.GradientBoostingRegressor(*args, **kwargs)


async def sk_isolation_forest(*args: Any, **kwargs: Any) -> Any:
    return ensemble.IsolationForest(*args, **kwargs)


async def sk_random_forest_classifier(*args: Any, **kwargs: Any) -> Any:
    return ensemble.RandomForestClassifier(*args, **kwargs)


async def sk_random_forest_regressor(*args: Any, **kwargs: Any) -> Any:
    return ensemble.RandomForestRegressor(*args, **kwargs)


async def sk_random_trees_embedding(*args: Any, **kwargs: Any) -> Any:
    return ensemble.RandomTreesEmbedding(*args, **kwargs)


async def sk_stacking_classifier(*args: Any, **kwargs: Any) -> Any:
    return ensemble.StackingClassifier(*args, **kwargs)


async def sk_stacking_regressor(*args: Any, **kwargs: Any) -> Any:
    return ensemble.StackingRegressor(*args, **kwargs)


async def sk_voting_classifier(*args: Any, **kwargs: Any) -> Any:
    return ensemble.VotingClassifier(*args, **kwargs)


async def sk_voting_regressor(*args: Any, **kwargs: Any) -> Any:
    return ensemble.VotingRegressor(*args, **kwargs)


async def sk_hist_gradient_boosting_classifier(
    *args: Any, **kwargs: Any
) -> Any:
    return ensemble.HistGradientBoostingClassifier(*args, **kwargs)


async def sk_hist_gradient_boosting_regressor(
    *args: Any, **kwargs: Any
) -> Any:
    return ensemble.HistGradientBoostingRegressor(*args, **kwargs)


async def sk_repeated_stratified_kfold(*args: Any, **kwargs: Any) -> Any:
    return model_selection.RepeatedStratifiedKFold(*args, **kwargs)


async def sk_kfold(*args: Any, **kwargs: Any) -> Any:
    return model_selection.KFold(*args, **kwargs)
