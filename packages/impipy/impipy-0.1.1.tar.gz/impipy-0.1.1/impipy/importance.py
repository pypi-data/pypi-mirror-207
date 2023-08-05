import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn
from sklearn.linear_model import LinearRegression

from tqdm import tqdm
from typing import List, Tuple, Dict, Union, Any, Optional
from itertools import combinations

class Importance:
    
    """
    Class for computing feature importance and generating counterfactuals for a given regression model and dataset.
    """
    
    def __init__(self, clf: sklearn.base.ClassifierMixin, dataset: pd.DataFrame, continuous_features: List[int], 
                 ordinal_features: List[int] = [], sample_size: int = 1000, R: float = 1.0, N: int = 21,
                 eta: Union[float, List[float]] = 1.0, zeta: Union[float, List[float]] = 1.0,
                 random_state: Optional[int] = None):
        
        """
        Initializes an Importance object.

        Args:
            clf (sklearn estimator): The model used for regression.
            dataset (pd.DataFrame): The dataset used for fitting the classifier.
            continuous_features (list): The indices of the continuous features in the dataset.
            ordinal_features (list, optional): The indices of the ordinal features in the dataset. Defaults to [].
            sample_size (int, optional): The size of the sample used for calculating feature importances. Defaults to 1000.
            R (float, optional): The range of values for the numerical feature importance. Defaults to 1.0.
            N (int, optional): The number of values for the numerical feature importance. Defaults to 21.
            eta (Union[float, List[float]], optional): The relative importance of categorical variables. Defaults to 1.0.
            zeta (Union[float, List[float]], optional): The relative importance of ordinal variables. Defaults to 1.0.
            random_state (int, optional): The random seed value used to select a sample. Defaults to None.
        """
        
        self.clf = clf
        self.R = R
        self.N = N
        self.sample_size = min(dataset.shape[0], sample_size)
        self.X = dataset.sample(self.sample_size, random_state=random_state).reset_index(drop=True)
        
        self.numerical_cols = sorted(continuous_features)
        self.ordinal_cols = sorted(ordinal_features)
        self.categorical_cols = [ind for ind in range(dataset.shape[1]) 
                                 if ind not in continuous_features and ind not in ordinal_features]
            
        self.intervals, self.unique_values, interval = {}, {}, [None, None]
        self.weights, idx, S = np.linspace(-R, R, N), len(continuous_features) + len(ordinal_features), 0
        
        for col in self.ordinal_cols:
            unique_ordinal_values = np.sort(dataset.iloc[:, col].unique())
            self.unique_values[col] = unique_ordinal_values
        
        for col in self.categorical_cols:
            if interval[0] is None:
                interval[0] = col
            S += dataset.iloc[:, col].sum()
            if S == dataset.shape[0]:
                interval[1] = col
                self.intervals[idx] = tuple(interval)
                S, interval, idx = 0, [None, None], idx+1
        
        self.imps = np.zeros((self.sample_size, len(continuous_features) + len(ordinal_features) + len(self.intervals)),
                             dtype='float64')
        self.eta = np.repeat(eta, len(self.intervals)) if isinstance(eta, (int, float)) else eta
        self.zeta = np.repeat(zeta, len(ordinal_features)) if isinstance(zeta, (int, float)) else zeta
    
    def update_numerical_importance(self, row: int, algorithm: str = 'diff') -> None:
        
        """
        Update the importance of each numerical feature in the given row based on a specified algorithm.

        Args:
            row (int): The row index of the observation to compute feature importances for.
            algorithm (str, optional): The algorithm used to compute feature importances. Either 'diff', 'lr', or 'lrsort'.
                Defaults to 'diff'.

        Returns:
            None
        """
        
        obs = self.X.iloc[row].values.reshape(1, -1)
        grid = obs.repeat(self.N, axis=0)
        if algorithm in ['lr', 'lrsort']: lr = LinearRegression()

        for col in self.numerical_cols:

            cur = obs[0, col]
            grid[:, col] = cur + self.weights
            predictions = self.clf.predict(grid)
            grid[:, col] = cur
            
            if algorithm == 'diff':
                self.imps[row, col] = np.abs(np.diff(predictions)).sum()
            elif algorithm in ['lr', 'lrsort']:
                lr.fit(self.weights.reshape(-1, 1), predictions if algorithm == 'lr' else sorted(predictions))
                self.imps[row, col] = abs(lr.coef_[0])
    
    def update_categorical_importance(self, row: int, algorithm: str = 'diff') -> None:
        
        """
        Updates the importance measure of categorical features for a given row.

        Args:
            row (int): Index of the row to update the importance measure for.
            algorithm (str, optional): Algorithm used to calculate feature importance. Defaults to 'diff'.

        Returns:
            None
        """
        
        obs = self.X.iloc[row].values.reshape(1, -1)
        if algorithm in ['lr', 'lrsort']: lr = LinearRegression()
        
        for ind, col in enumerate(self.intervals):

            left, right = self.intervals[col]
            L = right-left+1

            cur = obs[0, left:right+1]
            grid_cat = obs.repeat(L, axis=0)
            grid_cat[:, left:right+1] = np.eye(L)
            predictions = self.clf.predict(grid_cat)

            if algorithm == 'diff':
                n_edges = (len(predictions) * (len(predictions) - 1) / 2)
                n_edges_adj = (n_edges * self.eta[ind]) / (2 * self.R)
                self.imps[row, col] = sum([abs(y-x) for x, y in combinations(predictions, 2)]) / n_edges_adj
            elif algorithm in ['lr', 'lrsort']:
                lr.fit((np.arange(len(predictions)) * self.eta[ind]).reshape(-1, 1), sorted(predictions))
                self.imps[row, col] = lr.coef_[0]
    
    def update_ordinal_importance(self, row: int, algorithm: str = 'diff') -> None:
        
        """
        Update the feature importance of ordinal variables for a single row in the dataset.

        Args:
            row (int): Index of the row to update feature importance for.
            algorithm (str, optional): The algorithm to use for calculating feature importance. 
                Must be one of 'diff', 'lr' or 'lrsort'. Defaults to 'diff'.

        Returns:
            None
        """
        
        obs = self.X.iloc[row].values.reshape(1, -1)
        if algorithm in ['lr', 'lrsort']: lr = LinearRegression()
        
        for ind, col in enumerate(self.ordinal_cols):

            cur = obs[0, col]
            grid_ord = obs.repeat(len(self.unique_values[col]), axis=0)
            grid_ord[:, col] = self.unique_values[col]
            predictions = self.clf.predict(grid_ord)

            if algorithm == 'diff':
                self.imps[row, col] = (2*np.abs(np.diff(predictions)).sum()*self.R) / (self.zeta[ind]*(len(predictions)-1))
            elif algorithm in ['lr', 'lrsort']:
                lr.fit((np.arange(len(predictions)) * self.zeta[ind]).reshape(-1, 1),
                       predictions if algorithm == 'lf' else sorted(predictions))
                self.imps[row, col] = abs(lr.coef_[0])
        
    def calculate_feature_importances(self, algorithm: str = 'diff', plot: bool = False,
                                      columns: List[str] = None, figsize: Tuple[int, int] = (10, 8),
                                      style: str = 'default', color: str = 'gray', fontsize: int = 14,
                                      title_fontsize: int = 18, fontname: str = 'serif',
                                      xlabel: str = 'Feature Importance Score', ylabel: str = 'Features',
                                      title: str = '') -> np.ndarray:
        
        """
        Calculate feature importances using the specified algorithm.

        Args:
            algorithm (str, optional): The algorithm used to calculate feature importances. Can be one of 'diff',
                'lr' or 'lrsort'. Defaults to 'diff'.
            plot (bool, optional): Whether to plot the feature importances. Defaults to False.
            columns (List[str], optional): The list of column names in the original dataset. Need to be specified when
                plot is set to True. Defaults to None.
            figsize (Tuple[int, int], optional): The size of the plot figure. Defaults to (10, 8).
            style (str, optional): The style of the plot. Defaults to 'default'.
            color (str, optional): The color of the plot. Defaults to 'gray'.
            fontsize (int, optional): The fontsize of the labels. Defaults to 14.
            title_fontsize (int, optional): The fontsize of the title. Defaults to 18.
            fontname (str, optional): The fontname of the title and the labels. Defaults to 'serif'.
            xlabel (str, optional): The label of the x-axis. Defaults to 'Feature Importance Score'.
            ylabel (str, optional): The label of the y-axis. Defaults to 'Features'.
            title (str, optional): The title of the plot. Defaults to an empty string.

        Returns:
            np.ndarray: An array of feature importances.
        """

        for row in tqdm(range(self.sample_size)):

            self.update_numerical_importance(row, algorithm=algorithm)
            self.update_categorical_importance(row, algorithm=algorithm)
            self.update_ordinal_importance(row, algorithm=algorithm)
        
        imps_mean = self.imps.mean(axis=0)
        self.feature_importances_ = imps_mean / sum(imps_mean)
        
        if plot:
            
            plt.figure(figsize=figsize)
            plt.style.use(style=style)
            
            default = self.X.columns[: len(self.numerical_cols) + len(self.ordinal_cols)].to_list() + \
                      ['_'.join(self.X.columns[ind].split('_')[:-1]) for ind in (x[0] for x in self.intervals.values())]
            columns = default if columns is None else columns
            plt.barh(columns, self.feature_importances_, color=color)
            
            plt.title(title, fontsize=title_fontsize, fontname=fontname, fontweight='bold')
            plt.xlabel(xlabel, fontsize=fontsize, fontname=fontname)
            plt.ylabel(ylabel, fontsize=fontsize, fontname=fontname)
            
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.gca().xaxis.grid(True, linestyle='--', linewidth=0.5, which='major', color='lightgray', alpha=0.5)
            
            plt.show()
        
        return self.feature_importances_
    
    def update_numerical_variables(self, obs: np.ndarray, grid: np.ndarray, 
                                   M_num: dict, m_num: dict, num_cols: List[int]) -> Tuple[dict, dict]:
        
        """
        Update the feature importance of numerical variables for a single observation in the dataset.

        Args:
            obs (numpy.ndarray): The observation to update the feature importance for.
            grid (numpy.ndarray): The grid of values to perturb the numerical features.
            M_num (dict): The maximum numerical feature importance found so far.
            m_num (dict): The minimum numerical feature importance found so far.
            num_cols (List[int]): The indices of the numerical columns in the dataset.

        Returns:
        A tuple of dictionaries containing the maximum and minimum numerical feature importance found after updating the
        current observation.
        """
        
        for col in num_cols:

            cur = obs[0, col]
            y_old = self.clf.predict(obs)

            grid[:, col] = cur + self.weights
            y_new = self.clf.predict(grid)
            grid[:, col] = cur

            dy = y_new - y_old
            dydx = np.divide(dy, np.abs(self.weights), out=np.zeros_like(dy), where=self.weights != 0)

            max_pos_num = np.argmax(dydx)
            min_pos_num = np.argmin(dydx)

            if dydx[max_pos_num] > M_num['val']:
                M_num['val'], M_num['change'] = dydx[max_pos_num], dy[max_pos_num]
                M_num['col'], M_num['step'] = col, 2*max_pos_num*self.R / (self.N-1) - self.R
            if dydx[min_pos_num] < m_num['val']:
                m_num['val'], m_num['change'] = dydx[min_pos_num], dy[min_pos_num]
                m_num['col'], m_num['step'] = col, 2*min_pos_num*self.R / (self.N-1) - self.R
        
        return M_num, m_num
    
    def update_categorical_variables(self, obs: np.ndarray, M_cat: dict, m_cat: dict,
                                     cat_cols: Dict[int, Tuple[int, int]]) -> \
                                     Tuple[Dict[str, Union[int, float, np.ndarray]],
                                     Dict[str, Union[int, float, np.ndarray]]]:
        
        """
        Update the feature importance of categorical variables for a single observation.

        Args:
            obs (numpy.ndarray): The observation to update the feature importance for.
            M_cat (dict): The dictionary containing the maximum feature importance values.
            m_cat (dict): The dictionary containing the minimum feature importance values.
            cat_cols Dict[int, Tuple[int, int]]): The dictionary containing the intervals for categorical columns.

        Returns:
            Tuple[Dict[str, Union[int, float, np.ndarray]], Dict[str, Union[int, float, np.ndarray]]]: 
            A tuple containing the updated M_cat and m_cat dictionaries.
        """
        
        for ind, col in enumerate(cat_cols):

            left, right = cat_cols[col]
            L = right-left+1

            cur = obs[0, left:right+1]
            y_old = self.clf.predict(obs)

            grid_cat = obs.repeat(L, axis=0)
            grid_cat[:, left:right+1] = np.eye(L)

            y_new = self.clf.predict(grid_cat)
            dy = (y_new - y_old)
            dydx = dy / self.eta[ind]

            max_pos_cat = np.argmax(dy)
            min_pos_cat = np.argmin(dy)

            if dydx[max_pos_cat] > M_cat['val']:
                M_cat['val'], M_cat['change'] = dydx[max_pos_cat], dy[max_pos_cat]
                M_cat['col'], M_cat['step'] = col, grid_cat[max_pos_cat, left:right+1]
            if dydx[min_pos_cat] < m_cat['val']:
                m_cat['val'], m_cat['change'] = dydx[min_pos_cat], dy[min_pos_cat]
                m_cat['col'], m_cat['step'] = col, grid_cat[min_pos_cat, left:right+1]
        
        return M_cat, m_cat
    
    def update_ordinal_variables(self, obs: np.ndarray, M_ord: Dict[str, Union[float, int]], 
                                 m_ord: Dict[str, Union[float, int]], ord_cols: List[int]) -> \
                                 Tuple[Dict[str, Union[float, int]], Dict[str, Union[float, int]]]:
        
        """
        Updates the ordinal variables using the input observation `obs` and the model `clf`.

        Args:
            obs (numpy.ndarray): The observation to update the feature importance for.
            M_ord: a dictionary representing the maximum importance of an ordinal variable, with keys 'val', 'change', 
                 'col', and 'step' and values corresponding to a float or an integer.
            m_ord: a dictionary representing the minimum importance of an ordinal variable, with keys 'val', 'change', 
                 'col', and 'step', and values corresponding to a float or an integer.
            ord_cols: a list of integers representing the column indices of the ordinal variables in the observation `obs`.

        Returns:
            A tuple containing two dictionaries `M_ord` and `m_ord` that represent the maximum and minimum importance 
            of the ordinal variables after updating.
        """
        
        for ind, col in enumerate(ord_cols):

            cur = obs[0, col]
            y_old = self.clf.predict(obs)

            grid_ord = obs.repeat(len(self.unique_values[col]), axis=0)
            grid_ord[:, col] = self.unique_values[col]

            y_new = self.clf.predict(grid_ord)
            dy = y_new - y_old
            dydx = np.divide(dy, (np.abs(self.unique_values[col] - cur) * self.zeta[ind]),
                             out=np.zeros_like(dy), where=self.unique_values[col] != cur)

            max_pos_ord = np.argmax(dydx)
            min_pos_ord = np.argmin(dydx)

            if dydx[max_pos_ord] > M_ord['val']:
                M_ord['val'], M_ord['change'] = dydx[max_pos_ord], dy[max_pos_ord]
                M_ord['col'], M_ord['step'] = col, grid_ord[max_pos_ord, col]
            if dydx[min_pos_ord] < m_ord['val']:
                m_ord['val'], m_ord['change'] = dydx[min_pos_ord], dy[min_pos_ord]
                m_ord['col'], m_ord['step'] = col, grid_ord[min_pos_ord, col]
        
        return M_ord, m_ord
    
    def select_column_change_step(self, target: int, M_num: Dict[str, Any], m_num: Dict[str, Any],
                                  M_cat: Dict[str, Any], m_cat: Dict[str, Any], M_ord: Dict[str, Any], 
                                  m_ord: Dict[str, Any]) -> Tuple[int, float, np.ndarray]:
        
        """
        Selects a column to update, along with the maximum/minimum change and step values.

        Args:
            target: An integer representing the target direction of the change.
            M_num: A dictionary containing the maximum positive change in the numerical variables.
            m_num: A dictionary containing the minimum negative change in the numerical variables.
            M_cat: A dictionary containing the maximum positive change in the categorical variables.
            m_cat: A dictionary containing the minimum negative change in the categorical variables.
            M_ord: A dictionary containing the maximum positive change in the ordinal variables.
            m_ord: A dictionary containing the minimum negative change in the ordinal variables.

        Returns:
            A tuple containing the following values:
                col: An integer representing the selected column.
                change: A float representing the maximum/minimum change in the selected column.
                step: A numpy array representing the values to add to the selected column.
        """
        
        if target > 0:
            if max(M_num['val'], M_cat['val'], M_ord['val']) == M_num['val']:
                col, change, step = M_num.get('col'), M_num.get('change', 0), M_num.get('step')
            elif max(M_num['val'], M_cat['val'], M_ord['val']) == M_cat['val']:
                col, change, step = M_cat.get('col'), M_cat.get('change', 0), M_cat.get('step')
            else:
                col, change, step = M_ord.get('col'), M_ord.get('change', 0), M_ord.get('step')
        else:
            if min(m_num['val'], m_cat['val'], m_ord['val']) == m_num['val']:
                col, change, step = m_num.get('col'), m_num.get('change', 0), m_num.get('step')
            elif min(m_num['val'], m_cat['val'], m_ord['val']) == m_cat['val']:
                col, change, step = m_cat.get('col'), m_cat.get('change', 0), m_cat.get('step')
            else:
                col, change, step = m_ord.get('col'), m_ord.get('change', 0), m_ord.get('step')
        
        return col, change, step
    
    def correct_last_numerical_change(self, obs: np.ndarray, target: float, col: int, change: float, step: float, 
                                      recommendation: Dict[int, float], S: float, delta: int) -> \
                                      Tuple[np.ndarray, Dict[int, float], float]:
        
        """
        Corrects the last numerical change to the dataset by varying the step size.
        
        Args:
            obs (np.ndarray): The dataset to be corrected.
            target (float): The target value of the predicted variable.
            col (int): The column index of the variable that was last updated.
            change (float): The value of the last change.
            step (float): The size of the last step.
            recommendation (Dict[int, float]): A dictionary with the recommendations for each variable in the dataset.
            S (float): The current regression prediction change after the last step.
            delta (int): The maximum number of steps.
        
        Returns:
            A tuple with the updated dataset, the updated recommendations and the updated regression prediction change.
        """
        
        S -= change
        cur = obs[0, col]
        y_old = self.clf.predict(obs)

        for ind, epsilon in enumerate(np.linspace(step / delta, step, delta)):

            obs[0, col] = cur + epsilon
            y_new = self.clf.predict(obs)
            dy = y_new - y_old

            if target * (target - S - dy) > 0: continue
            recommendation[col] = epsilon + recommendation.get(col, 0)
            obs[0, col] = cur + epsilon
            S += dy[0]
            break
        
        return obs, recommendation, S
    
    def get_recommendation(self, observation: np.ndarray, target: float, continuous_to_vary: Optional[List[int]] = None,
                           ordinal_to_vary: Optional[List[int]] = None, categorical_to_vary: Optional[List[int]] = None,
                           total_CFs: int = 1, loc: Optional[List[float]] = None, scale: Optional[List[float]] = None,
                           prec: int = 3, delta: int = 100, verbose: int = 0, tol: int = 1e-6) -> Tuple[pd.DataFrame, Dict]:
        
        """
        Generates recommendations that change the prediction of a trained regression model by a given amount.

        Parameters:
            observation (np.ndarray): A numpy array containing a single observation to start from.
            target (float): The target amount to change the prediction by.
            continuous_to_vary (List[int], optional): A list of indices of the continuous columns to vary.
                If None, all continuous columns will be used. Defaults to None.
            ordinal_to_vary (List[int], optional): A list of indices of the ordinal columns to vary.
                If None, all ordinal columns will be used. Defaults to None.
            categorical_to_vary (List[int], optional): A list of indices of the categorical columns to vary.
                If None, all categorical columns will be used. Defaults to None.
            total_CFs (optional, int): The total number of counterfactuals to return. Defaults to 1.
            loc (List[float], optional): The array of floats of the continuous_features length. Represents the mean
                of each feature in the original dataset.
            scale (List[float], optional): The array of floats of the continuous_features length. Represents the standard
                deviations of each feature in the original dataset.
            prec (int, optional): The precision of the displayed recommendations. Defaults to 3.
            delta (int, optional): The maximum step size when correcting the last numerical variable. Defaults to 100.
            verbose (int, optional): If 1, print the changes recommended. If 0, do not print anything. Defaults to 0.
            tol (float, optional): The tolerance to stop the algorithm. Defaults to 1e-6.

        Returns:
            Tuple[np.ndarray, Dict]: A tuple containing the modified observation array, and a dictionary of recommendations.
                The dictionary keys are column indices and the values are the amount by which to change the value in
                that column.
        """

        S, recommendation, obs = 0, {}, np.array(observation).reshape(1, -1)
        num_cols = self.numerical_cols if continuous_to_vary is None else continuous_to_vary
        ord_cols = self.ordinal_cols if ordinal_to_vary is None else ordinal_to_vary
        cat_cols = self.intervals if categorical_to_vary is None else {i: self.intervals[i] for i in categorical_to_vary}
        
        while abs(S) < abs(target):

            grid = obs.repeat(self.N, axis=0)

            M_num, m_num = {'val': 0}, {'val': 0}
            M_cat, m_cat = {'val': 0}, {'val': 0}
            M_ord, m_ord = {'val': 0}, {'val': 0}

            M_num, m_num = self.update_numerical_variables(obs, grid, M_num, m_num, num_cols)
            M_cat, m_cat = self.update_categorical_variables(obs, M_cat, m_cat, cat_cols)
            M_ord, m_ord = self.update_ordinal_variables(obs, M_ord, m_ord, ord_cols)

            col, change, step = self.select_column_change_step(target, M_num, m_num, M_cat, m_cat, M_ord, m_ord)

            S += change            
            if abs(change) < tol:
                print('Not possible.')
                break

            if col in num_cols and abs(S) < abs(target):
                recommendation[col] = step + recommendation.get(col, 0)
                obs[0, col] = obs[0, col] + step
            elif col in ord_cols:
                recommendation[col] = step
                obs[0, col] = step
            elif col not in num_cols and col not in ord_cols:
                recommendation[col] = step
                obs[0, self.intervals[col][0]:self.intervals[col][1]+1] = step

        if col in num_cols and change:
            obs, recommendation, S = self.correct_last_numerical_change(obs, target, col, change, step,
                                                                        recommendation, S, delta)

        if verbose == 1:
            
            print(f'Total change in prediction: {S:0,.{prec}f}')

            for col in recommendation:
                if col in num_cols:
                    mu = np.zeros_like(num_cols) if loc is None else loc
                    sigma = np.ones_like(num_cols) if scale is None else scale
                    idx = num_cols.index(col)
                    print(f'Change {self.X.columns[col]} by {recommendation[col] * sigma[idx]:0.{prec}g} to '
                          f'{obs[0, col] * sigma[idx] + mu[idx]:0,.{prec}g}')
                elif col in ord_cols: print(f'Change {self.X.columns[col]} from '
                                            f'{np.array(observation)[col]} to {recommendation[col]}')
                else: print(f'Change {self.X.columns[self.intervals[col][0]:self.intervals[col][1]+1].to_list()} from '
                            f'{np.array(observation)[self.intervals[col][0]:self.intervals[col][1]+1]} to '
                            f'{recommendation[col]}')
        
        return pd.DataFrame(obs, columns=self.X.columns), recommendation