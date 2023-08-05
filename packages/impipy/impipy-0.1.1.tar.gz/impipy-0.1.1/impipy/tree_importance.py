import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

import sklearn
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.inspection import permutation_importance
from typing import List, Tuple, Optional

class TreeImportance:
    
    """
    Class for computing feature importance for a given tree-like classifier and dataset.
    """
    
    def __init__(self, clf: sklearn.base.ClassifierMixin, dataset: pd.DataFrame,
                 outcome_name: str, random_state: Optional[int] = None) -> None:
        
        """
        Initializes a TreeImportance object.
        
        Parameters:
            clf (ClassifierMixin): A fitted tree-like classifier or regressor.
            dataset (pd.DataFrame): A pandas DataFrame that contains the data used to train the classifier.
            outcome_name (str): The name of the outcome variable (i.e., the target variable) in the DataFrame.
            random_state (Optional[int]): Controls the random seed used in the permutation_importance method. 
        
        Returns:
        None
        """
        
        self.clf = clf
        self.random_state = random_state
        
        self.X = dataset.drop(outcome_name, axis=1)
        self.y = dataset[outcome_name]
        self.n_rows, self.n_cols = self.X.shape
        
    def update_importance(self, clf: sklearn.base.ClassifierMixin, imp: List[float]) -> List[float]:
        
        """
        Updates feature importances based on the decision tree regressor and previous importances.

        Args:
            clf (ClassifierMixin): A decision tree regressor used to get the feature importances.
            imp (List[float]): A list of floats containing the feature importances.

        Returns:
            A list of floats containing the updated feature importances.
        """
    
        node_indicator = clf.decision_path(self.X.values)
        leaf_path = {}

        for i in range(self.n_rows):
            node_index = node_indicator.indices[node_indicator.indptr[i]:node_indicator.indptr[i+1]-1]
            leaf_index = node_indicator.indices[node_indicator.indptr[i+1]-1]
            if leaf_index in leaf_path: leaf_path[leaf_index]['count'] += 1
            else: leaf_path[leaf_index] = {'path': node_index, 'count': 1}

        for val in leaf_path.values():
            path, count = val['path'], val['count']
            for node_id in path:
                feature_id = clf.tree_.feature[node_id]
                imp[feature_id] += count / len(path)

        return imp
    
    def calculate_ebi(self) -> np.ndarray:
        
        """
        Calculates the example-based importance of the features.

        Returns:
            numpy array representing the example-based importance of the features.
        """
        
        if isinstance(self.clf, DecisionTreeClassifier) or isinstance(self.clf, DecisionTreeRegressor):
            imp = self.update_importance(self.clf, np.zeros(self.n_cols, dtype='float64'))
            ebi = imp / self.n_rows
        else:
            imp = np.zeros(self.n_cols, dtype='float64')
            for c in self.clf.estimators_:
                classifier = c[0] if isinstance(self.clf, GradientBoostingClassifier) \
                                     or isinstance(self.clf, GradientBoostingRegressor) else c
                imp = self.update_importance(classifier, imp)
            ebi = imp / (self.n_rows * len(self.clf.estimators_))
        
        return ebi
    
    def calculate_mdg(self) -> np.ndarray:
        
        """
        Calculates the MDG importance of the features.

        Returns:
            numpy array representing the MDG importance of the features.
        """
        
        return self.clf.feature_importances_
    
    def calculate_mda(self, n_repeats=5) -> np.ndarray:
        
        """
        Calculates the MDA importance of the features.

        Returns:
            numpy array representing the MDA importance of the features.
        """
        
        perm = permutation_importance(self.clf, self.X.values, self.y, n_repeats=n_repeats, random_state=self.random_state)
        perm_imps = np.array([x.mean() for x in perm['importances']])
        perm_std = (perm_imps - perm_imps.min()) / (perm_imps.max() - perm_imps.min())
        mda = perm_std / np.sum(perm_std)
        
        return mda
    
    def calculate_feature_importances(self, n_repeats: int = 5) -> pd.DataFrame:
        
        """
        Calculate feature importances using EBI, MDG, and MDA methods.

        Args:
            n_repeats (int): Number of times to repeat MDA calculation for each feature (default: 5).

        Returns:
            pd.DataFrame: A DataFrame containing feature importances calculated using EBI, MDG, and MDA methods.
        """
        
        ebi = self.calculate_ebi()
        mdg = self.calculate_mdg()
        mda = self.calculate_mda(n_repeats=n_repeats)
        
        imps = pd.DataFrame(zip(ebi, mdg, mda), columns=['EBI', 'MDG', 'MDA'], index=self.X.columns)
        imps = imps[(imps.EBI > 0) | (imps.MDG > 0) | (imps.MDA > 0)]
        
        return imps
    
    def plot_feature_importances(self, n_repeats: int = 5, figsize: Tuple[int, int] = (10, 8),
                                 style: str = 'default', palette: str = 'colorblind',
                                 fontsize: int = 14, title_fontsize: int = 18, fontname: str = 'serif',
                                 xlabel: str = 'Feature Importance Score', ylabel: str = 'Features',
                                 title: str = '', filename: str = None) -> matplotlib.figure.Figure:
        
        """
        Plots the feature importances.

        Args:
            n_repeats: An integer indicating the number of times to repeat the MDA calculation (default 5).
            figsize: A tuple specifying the figure size (default (10, 8)).
            style: A string specifying the style of the plot (default 'default').
            palette: A string specifying the palette of the plot (default: 'colorblind')
            fontsize (int, optional): The fontsize of the labels. Defaults to 14.
            title_fontsize (int, optional): The fontsize of the title. Defaults to 18.
            fontname (str, optional): The fontname of the title and the labels. Defaults to 'serif'.
            xlabel (str, optional): The label of the x-axis. Defaults to 'Feature Importance Score'.
            ylabel (str, optional): The label of the y-axis. Defaults to 'Features'.
            title (str, optional): The title of the plot. Defaults to an empty string.
            filename (str, optional): The file name to save the figure. Defaults to None.

        Returns:
            matplotlib.figure.Figure
        """

        imps = self.calculate_feature_importances(n_repeats=n_repeats)

        plt.style.use(style=style)
        sns.set_style('ticks')
        
        colors = sns.color_palette(palette=palette, n_colors=len(imps))
        sns.set_palette(colors)

        fig, ax = plt.subplots(figsize=figsize)
        imps.plot.barh(ax=ax)

        ax.xaxis.grid(True, linestyle='--', linewidth=0.5, which='major', color='lightgray', alpha=0.5)
        ax.set_xlabel(xlabel, fontsize=fontsize, fontname=fontname)
        ax.set_ylabel(ylabel, fontsize=fontsize, fontname=fontname)
        ax.set_title(title, fontsize=title_fontsize, fontname=fontname, fontweight='bold')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1])
        
        if filename is not None: plt.savefig(filename)
        plt.close(fig)

        return fig