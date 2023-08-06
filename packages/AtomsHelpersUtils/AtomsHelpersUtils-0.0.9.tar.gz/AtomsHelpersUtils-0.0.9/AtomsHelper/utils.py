# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:08:02 2022

@author: eccn3
"""

import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt

import networkx as nx

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from itertools import compress

from ase.data.colors import jmol_colors
from ase.data import chemical_symbols
from ase import formula

from sklearn.neighbors import NearestNeighbors


def draw_surf_graph(graph, cutoff = 0.3, 
                    node_label_type = 'element', edge_labels = False, edge_label_type = 'weight'):
   
    '''
    Draws graph of atoms system
    Input:
        graph: networkx graph of atoms
        cutoff: min edge value to be drawn
        node_label_type: what attribute to print as node label
        edge_labels: boolean to draw edge labels
        edge_label_type: what attribute to print as edge label
    Output:
        prints graph
    '''
    
    if edge_label_type !='weight' and edge_labels == False:
        edge_labels=True
    
    if cutoff:
        graph = remove_small_edges(graph, cutoff = cutoff)

    plt.figure(figsize=(6,5))
   
    colors = {i:j.reshape(1,-1) for i,j in zip(chemical_symbols, jmol_colors)}  

    metals = [i for i in chemical_symbols if i not in formula.non_metals]
    
    colors['M'] = [0.5, 0.5, 0.5]

    # for i in colors.keys():
    #     colors[i] = np.array(colors[i]).reshape(1,-1)              

    element_count = {i: [] for i in colors.keys()}

    for i in nx.get_node_attributes(graph, 'element').items():
        element_count[i[1]].append(i[0])
   
    init_pos = nx.get_node_attributes(graph, 'element')
   
    for i in init_pos.keys():
        if any([init_pos[i] ==j for j in metals]):
            init_pos[i] = [np.random.uniform(),0.05 +0.1* np.random.uniform()]
        else:
            init_pos[i] = [np.random.uniform(), 0.85 +0.1* np.random.uniform()]
   
    pos = nx.spring_layout(graph,pos=init_pos)    
       
       
    system_count = {'metal surface coordinated': [], 'adsorbate surface coordinated': []}
    keys = system_count.keys()
    for i in nx.get_node_attributes(graph, 'system_type').items():
        if any([i[1] == j for j in keys]):
            system_count[i[1]].append(i[0])
           
           
    options = {"edgecolors": "tab:cyan"}
    for i in system_count.keys():    
        nx.draw_networkx_nodes(graph, pos, nodelist = system_count[i],node_size=500, **options)
       
    for i in element_count.keys():
        if not element_count[i]:
            continue
        if any(i==j for j in metals):
            nx.draw_networkx_nodes(graph, pos, nodelist=element_count[i],
                                   node_size=200, node_color = colors[i],
                                   edgecolors = (0,0,0), alpha = 0.5)
        else:
            nx.draw_networkx_nodes(graph, pos, nodelist=element_count[i],
                                   node_size=400, node_color = colors[i],
                                   edgecolors=(0,0,0), alpha = 0.5)

       
       
    nx.draw_networkx_edges(graph, pos, alpha = 0.5)
   
    labels = nx.get_node_attributes(graph, node_label_type)
    
    nx.draw_networkx_labels(graph, pos, labels)
    
    if edge_labels:
        ed_labels = nx.get_edge_attributes(graph, edge_label_type)
        nx.draw_networkx_edge_labels(graph, pos, ed_labels)
    # plt.close()

def remove_small_edges(graph, cutoff = 0.3):
    small_weights = []

    for i in graph.edges():
        if graph.edges[i]['weight'] < cutoff:
            small_weights.append(i)
            
    copy_graph = copy.deepcopy(graph)
    for i in small_weights:
        copy_graph.remove_edge(*i)

    return copy_graph

def data_keep(X, X_names, idx):
    
    
    
    return X[:, idx], X_names[ idx]

def correlation(df, threshold):

    cor_matrix = df.corr().abs()
    upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > threshold)]
    print(to_drop)
    df1 = df.drop(to_drop, axis=1)

    return df1

def number_select(df, column):
    
    # Selects only rows that have a TYPE NUMBER in specified column
    
    # Input: df = df to search; column = 
    
    df1 = df[pd.to_numeric(df[column], errors='coerce').notnull()]
    
    
    return df1

def match(df1, df2, feature, substrate = True, graph = False):
    
    # Iterates through df1: looks at adsorbate, substrate, and site combination
    # Find matches in df2 for adsorbate/substrate/site combination to grab its energy
    
    if feature in list(df1.columns):
        newfeat = feature + ' 2'
        df1.insert(int(np.where(df1.columns == feature)[0][0])+1, newfeat, np.nan)
    
    else:
        newfeat = feature
        df1[newfeat] = np.nan
    
    if graph:
        df1[newfeat] = pd.DataFrame(df1[newfeat], dtype = object)
    
    match_feats=['Adsorbate', 'Site']
    
    if substrate:
       match_feats.append('Substrate') 
        
    for count, i in df1.iterrows():
        comparison_column = (df2[match_feats] == i[match_feats]).all(axis = 1)
        if any(comparison_column):
            df1.at[count, newfeat] = df2[feature][comparison_column].iloc[0]
    
    df1 = df1.dropna()

    return df1

def plot_parity(x, y, label = None, alp = 0.75):

    # Plots scatter parity between x and y, with label if desired
    # In: x = x-axis data; y = y-axis data; label = scatter label; alp = alpha for dots
    # Out: scatter plot

    if not label:
        l = 'Parity'

    else:
        l = label

    plt.scatter(x, y, alpha = alp, label = l)
    minx = min(x)-abs(min(x)*0.25)
    miny = min(y)-abs(min(y)*0.25)
    maxx = max(x)+abs(max(x)*0.25)
    maxy = max(y)+abs(max(y)*0.25)
    
    
    minimum = min(minx, miny)
    maximum = max(maxx, maxy)
    
    plt.ylim(minimum, maximum)
    plt.xlim(minimum, maximum)
    plt.plot([minimum,maximum], [minimum, maximum], alpha = 0.5)

def plot_hist(X):
    plt.hist(x=X, bins='auto', rwidth=0.85, label = "Difference in Eads")


def print_results(models, model_selects, model_data, y= []):
    
    # Print results for your fitting. Companion to test_fit
    # In: models = list of models; model_selects = splitting methods used; 
        # model_data = fit results; y = response targets
    # Out: prints for Mean Absolute Error values
    
    if y!=[]:
        MAD = np.round(np.mean(abs(y)),3)
        MADstdev = np.round(np.std(y),3)
    
        print('Mean Absolute Error = ' + str(MAD))

        print('Difference Stdev = ' + str(MADstdev) + '\n')
    
    model_names = [type(i).__name__ for  i in models]
    
    for count, i in enumerate(model_data):
        print(model_names[count])
        MAEs = [np.round(j['MAE'],3) for j in i]
        print('MAEs: ', MAEs)
        StDs = [np.round(np.mean(j['Error Stdev']),3) for j in i]
        print('Error Stdev = ' + str(StDs))
        StDs = [np.round(np.mean(j['Coef Stdevs']),3) for j in i]
        print('Coef Stdevs: ', StDs)
        print()

def plot_across_modelselects(models, feature, percents):
    
    # Plots a feature across model selection methods
    # In: models = results of fittings; feature = what to plot across models; 
        # percents = x-axis data, usually percent of data learned on
        
    # Out: plot of feature versus percent-learned on
    
    y = [i[feature] for i in models]
    stdev = [np.std(i['Errors']) for i in models]
    plt.figure()
    plt.errorbar(percents, y, yerr = stdev)
    
    plt.ylabel(feature)
    plt.xlabel('Percent of Dataset Learned On')
    
    plt.title('Learning Curve')


def drop(df, adsorbate, site):
    
    # Drop from df, based on adsorbate and site. And sensitive.
    # In: df = dataframe of data; adsorbate = adsorbate to drop; site = site to drop
    
    a = (df['Adsorbate'] == adsorbate) & (df['Site'] == site)
    a = [not elem for elem in a]
    
    df = df[a]
    
    return df

def test_fit(X, y, models, model_selects, df1, scale_x = None, scale_y = None, 
             hyper_param_tune = None, group = 'Adsorbate'): 
    
    # Make model_fit_data 
   
    keys = ['Model', 'Predictions', 'Hyperparameters','Coefficients', 
            'Scaled Coefficients','Coef Stdevs', 'Errors', 'MAE', 
            'Error Stdev', 'Feat. Imp', 'Alphas', 'Model Select', 'Weights', 
            'Y scaler', 'X scaler', 'Pred_std']
    
    model_fit_data = {k: [] for k in keys}
    
    model_data = [[] for i in model_selects]

    data = [copy.deepcopy(model_data) for i in models]

    # Shape y properly
    y = y.reshape(-1,1) 
   
    # Scale y if y scaler input
    if scale_y:
        
        scale_y.fit(y)
        y = scale_y.transform(y)
        model_fit_data['Y scaler'] = scale_y
    
    if scale_x: 
        scale_x.fit(X)
        X = scale_x.transform(X)
        model_fit_data['X scaler'] = scale_x


    for count1, model in enumerate(models):
        
        for count2, model_select in enumerate(model_selects):
            
            m = copy.deepcopy(model_fit_data)
            
            m['Model Select'] = model_select
            m['Train Index'] = []
            m['Test Index'] = []
            m['Test Adsorbate Index'] = []
            test_ind = np.array([]).astype(int)

            
            splits = []
            if str(type(model_select)) == "<class 'sklearn.model_selection._split.KFold'>":
                for i,j in model_select.split(X,y):
                    splits.append((i, j))
                    
            if str(type(model_select)) ==  "<class 'sklearn.model_selection._split.GroupKFold'>":
                for i,j in model_select.split(X,y,df1[group]):
                    splits.append((i, j))

            if str(type(model_select)) ==  "<class 'sklearn.model_selection._split.StratifiedKFold'>":
                for i,j in model_select.split(X = X, y=df1[group]):
                    splits.append((i, j))

            for train_index, test_index in splits:

                test_ind = np.append(test_ind, test_index)                

                m['Train Index'].append(train_index)
                m['Test Index'].append(test_index)
                m['Test Adsorbate Index'] = df1['Adsorbate'].iloc[test_index]
                
                X_train, X_test = X[train_index], X[test_index]
                Y_train, Y_test = y[train_index], y[test_index]
                
                
                if hyper_param_tune:
                    hyper_param_tune.fit(X_train, Y_train)
                    params=hyper_param_tune.best_params_
                    m['Hyperparameters'].append(copy.deepcopy(hyper_param_tune.best_params_))
                    model = model.set_params(**params)    
                
                fitted_model = model.fit(X_train, Y_train)
                
                m['Model'].append(copy.deepcopy(fitted_model))
                
                prediction = fitted_model.predict(X_test).reshape(-1,1)
                
                if scale_y:
                    
                    m['Predictions'].append(scale_y.inverse_transform(prediction))
                    m['Errors'].append(scale_y.inverse_transform(Y_test) - scale_y.inverse_transform(prediction))
                    
                else:
                    m['Predictions'].append(prediction)
                    m['Errors'].append(Y_test - prediction)
                    
                if str(type(model)) == "<class 'sklearn.gaussian_process._gpr.GaussianProcessRegressor'>":
                    std_pred = fitted_model.predict(X_test, return_std = True)[1]
                    if scale_y:
                        m['Pred_std'].append(np.sqrt(np.power(std_pred,2)*scale_y.var_))
                    else:
                        m['Pred_std'].append(m['Pred_std'])
                
                if str(type(model)) == "<class 'sklearn.linear_model._coordinate_descent.LassoCV'>":
                    m['Alphas'].append(fitted_model.alpha_)
                    
                if str(type(model)) == "<class 'sklearn.linear_model._ridge.RidgeCV'>":
                    m['Alphas'].append(fitted_model.alpha_)
                    
                if str(type(model)) == "<class 'sklearn.linear_model._coordinate_descent.ElasticNetCV'>":
                    m['Alphas'].append(fitted_model.alpha_)
                
                if str(type(model)) == "<class 'sklearn.ensemble._forest.RandomForestRegressor'>":
                    m['Feat. Imp'].append(fitted_model.feature_importances_)
                
                if type(model).__name__ == 'XGBRegressor':
                    m['Feat. Imp'].append(fitted_model.feature_importances_)
                    weights = fitted_model.get_booster().get_score(importance_type = 'weight')
                    weight_keys = sorted(list(weights.keys()))
                    weight = [weights[i] for  i in weight_keys]
                    m['Weights'].append(weight)
                
                
                try:
                    
                    if scale_x:
                        xcoefs  = scale_x.transform(fitted_model.coef_.reshape(1,-1))
                        
                            
                        m['Scaled Coefficients'].append(fitted_model.coef_.reshape(1,-1))
                        m['Coefficients'].append(xcoefs)
                        
                    else:
                        m['Coefficients'].append(fitted_model.coef_.reshape(1,-1))
                except:
                    pass
                
            try:
                m['Coefficients'] = np.array(m['Coefficients'])
                m['Coef Stdevs'] = np.std(m['Coefficients'], axis = 0)
            except:
                pass
            
            try:
                
                m['Errors'] = np.concatenate(m['Errors'], axis = 0)[np.argsort(test_ind)]
                m['Predictions'] = np.concatenate(m['Predictions'], axis = 0)[np.argsort(test_ind)]
                m['MAE'] = np.mean(abs(m['Errors']))
                m['Error Stdev'] = np.std(m['Errors'])
            except:
                pass
                
                
            try:
                m['Feat. Imp'] = np.array(m['Feat. Imp'])
                if m['Feat. Imp'].any():
                    m['Coef Stdevs'] = np.std(m['Feat. Imp'], axis = 0)
                
            except:
                pass
            
            data[count1][count2] = m
            
    return data

def lowest_Eads(df):
    
    df_return = np.array([])
    
    for i in list(df.Adsorbate.unique()):
        a = df[df['Adsorbate']==i]
        for j in list(a.Substrate.unique()):
            b = a[a['Substrate']==j]
            df_return= np.append(df_return, b['Eads'].idxmin())
    
    df_return = copy.deepcopy(df).loc[df_return]
    return df_return

def atomic_breakdown(adsorbates):
    uniquechars = ''.join(adsorbates)
    uniquechars = ''.join(set(uniquechars))
    uniquechars = list(''.join([i for i in uniquechars if not i.isdigit()]))
    
    atomsmatrix = np.zeros((len(adsorbates), len(uniquechars)))
    
    for count, i in enumerate(adsorbates):
        counts = dict.fromkeys(uniquechars, 0)
        while len(i)>0:
            if len(i) == 1:
                counts[i] +=1
                i = ''
                continue
            if i[1].isdigit():
                string = i[0:2]
                counts[string[0]] += int(string[1])
                i = i[2:]
                continue
            if not i[1].isdigit():
                counts[i[0]] +=1
                i = i[1:]
                continue
            
        for count2, j in enumerate(uniquechars):
            atomsmatrix[count, count2] = counts[j]
    
    
    return uniquechars, atomsmatrix

def pca_analysis(X, pca = PCA(), cutoff = 0.9):

    pca.fit(X)

    X_new= pca.fit_transform(X)
    
    exp_var = np.cumsum(pca.explained_variance_ratio_)
    
    if str(type(pca)) == "<class 'sklearn.decomposition._pca.PCA'>":
        plt.figure()
        plt.plot(range(len(X_new[0,:])+1), np.append(0, exp_var))
        plt.bar(range(len(X_new[0,:])+1), np.append(0, pca.explained_variance_ratio_))
        plt.ylabel('Explained Variance')
        plt.xlabel('# Principle Components')
        plt.title('PCA: Variance Explained')
        plt.grid()
        
        plt.figure()
        
    if str(type(pca)) == "<class 'sklearn.decomposition._kernel_pca.KernelPCA'>":
        plt.figure()
        plt.plot(range(len(X_new[0,:])+1), np.append(0, np.cumsum(pca.eigenvalues_)/np.sum(pca.eigenvalues_)))
        
    return pca, X_new


def myplot(X, pca = PCA(), labels=None):
    
    plot_pca, X_pca = pca_analysis(X, pca = pca)
    
    score = X_pca[:,0:2]
    coeff= np.transpose(plot_pca.components_[0:2, :])
    
    xs = score[:,0]
    ys = score[:,1]
    n = coeff.shape[0]
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    plt.scatter(xs * scalex,ys * scaley,s=5)
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5)
        if labels is None:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'green', ha = 'center', va = 'center')
        else:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, labels[i], color = 'g', ha = 'center', va = 'center')
 
    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.grid()

def loadingplot(coeff,labels=None):

    n = coeff.shape[0]
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5)
        
        if labels is None:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'green', ha = 'center', va = 'center')
        else:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, labels[i], color = 'g', ha = 'center', va = 'center')

    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.ylim((-0.5,0.5))
    plt.xlim((-0.5,0.5))
    plt.grid()

        
def cluster_PCs(x, pca=PCA(), cutoff=0.9, clustering = 'kmeans'):
    
    new_pca, x_pca = pca_analysis(x, pca=pca, cutoff=cutoff)
    exp_var = np.cumsum(pca.explained_variance_ratio_)
    cutoff_ind = sum(exp_var<cutoff)+1
    components = new_pca.components_[:cutoff_ind, :].T
    for i in components:
        if i[0] >0:
            i = -i
            
    if clustering == 'kmeans':
        cluster_fit = KMeans(n_clusters= cutoff_ind)
        
    cluster_fit.fit(components)
    centers=cluster_fit.cluster_centers_
    closest = []
    
    for i in centers:
        closest.append(np.argmin(np.linalg.norm(components - i, axis = 1)))
    
    plt.figure()
    plt.scatter(new_pca.components_[0,:], new_pca.components_[1,:], c=cluster_fit.labels_)
    plt.ylim((-0.5,0.5))
    plt.xlim((-0.5,0.5))
    return x_pca, new_pca, cluster_fit,closest
    
def test_predictions(X, models, y, x_scale = None, y_scale = None):
    
    if x_scale:
        X = x_scale.transform(X)

    
    predictions = []
    errors = []
    
    pred_mean = []
    pred_std = []
    err_mean = []
    
    for i in models:
        
        p = i.predict(X)
        
        if y_scale:
            p=y_scale.inverse_transform(p.reshape(-1,1)).reshape(1,-1)[0]
        
        predictions.append(p)
        errors.append(y-p)

    
    for i in range(len(X)):
      
        thisone = []
        
        for j in predictions:
            thisone.append(j[i])
        pred_mean.append(np.mean(thisone))
        pred_std.append(np.std(thisone))
        err_mean.append(np.mean(y[i]-thisone))
        
    return predictions, pred_mean, pred_std, errors, err_mean

def match_not_pt(x, y,xname, yname):
    
    substrates = x.Substrate.unique()

    
    returns={k: {K:[] for K in ['X', 'y']} for k in substrates}
        
    
    for index, i in x.iterrows():
        ads = i['Adsorbate']
        site = i['Site']
        returns[i['Substrate']]['X'].append(copy.deepcopy(i[xname]))
        returns[i['Substrate']]['y'].append(copy.deepcopy(y[(y['Adsorbate'] ==ads) & (y['Site'] == site)][yname].to_numpy()[0]))
        
    return returns

def min_img_dist(cell, pos1, pos2):
    periodics = np.array([-1, 0, 1])
    distances = np.empty(27)
    
    idx = 0
    
    for i in periodics:
        for j in periodics:
            for k in periodics:
                distances[idx] = np.linalg.norm(np.sum(pos1 + np.array([i,j,k]) * cell.T, axis = 1))
                idx +=1
    return min(distances)


def best_fit_transform(A, B):
    '''
    Calculates the least-squares best-fit transform that maps corresponding points A to B in m spatial dimensions
    Input:
      A: Nxm numpy array of corresponding points
      B: Nxm numpy array of corresponding points
    Returns:
      T: (m+1)x(m+1) homogeneous transformation matrix that maps A on to B
      R: mxm rotation matrix
      t: mx1 translation vector
    '''

    assert A.shape == B.shape

    # get number of dimensions
    m = A.shape[1]

    # translate points to their centroids
    centroid_A = np.mean(A, axis=0)
    centroid_B = np.mean(B, axis=0)
    AA = A - centroid_A
    BB = B - centroid_B

    # rotation matrix
    H = np.dot(AA.T, BB)
    U, S, Vt = np.linalg.svd(H)
    R = np.dot(Vt.T, U.T)

    # special reflection case
    if np.linalg.det(R) < 0:
       Vt[m-1,:] *= -1
       R = np.dot(Vt.T, U.T)

    # translation
    t = centroid_B.T - np.dot(R,centroid_A.T)

    # homogeneous transformation
    T = np.identity(m+1)
    T[:m, :m] = R
    T[:m, m] = t

    return T, R, t


def nearest_neighbor(src, dst):
    '''
    Find the nearest (Euclidean) neighbor in dst for each point in src
    Input:
        src: Nxm array of points
        dst: Nxm array of points
    Output:
        distances: Euclidean distances of the nearest neighbor
        indices: dst indices of the nearest neighbor
    '''

    assert src.shape == dst.shape

    neigh = NearestNeighbors(n_neighbors=1)
    neigh.fit(dst)
    distances, indices = neigh.kneighbors(src, return_distance=True)
    return distances.ravel(), indices.ravel()


def icp(A, B, init_pose=None, max_iterations=20, tolerance=0.001):
    '''
    The Iterative Closest Point method: finds best-fit transform that maps points A on to points B
    Input:
        A: Nxm numpy array of source mD points
        B: Nxm numpy array of destination mD point
        init_pose: (m+1)x(m+1) homogeneous transformation
        max_iterations: exit algorithm after max_iterations
        tolerance: convergence criteria
    Output:
        T: final homogeneous transformation that maps A on to B
        distances: Euclidean distances (errors) of the nearest neighbor
        i: number of iterations to converge
    '''

    assert A.shape == B.shape

    # get number of dimensions
    m = A.shape[1]

    # make points homogeneous, copy them to maintain the originals
    src = np.ones((m+1,A.shape[0]))
    dst = np.ones((m+1,B.shape[0]))
    src[:m,:] = np.copy(A.T)
    dst[:m,:] = np.copy(B.T)

    # apply the initial pose estimation
    if init_pose is not None:
        src = np.dot(init_pose, src)

    prev_error = 0

    for i in range(max_iterations):
        # find the nearest neighbors between the current source and destination points
        distances, indices = nearest_neighbor(src[:m,:].T, dst[:m,:].T)

        # compute the transformation between the current source and nearest destination points
        T,_,_ = best_fit_transform(src[:m,:].T, dst[:m,indices].T)

        # update the current source
        src = np.dot(T, src)

        # check error
        mean_error = np.mean(distances)
        if np.abs(prev_error - mean_error) < tolerance:
            break
        prev_error = mean_error

    # calculate final transformation
    T,_,_ = best_fit_transform(A, src[:m,:].T)

    return T, distances, i
    