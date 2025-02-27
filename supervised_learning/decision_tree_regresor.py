from sklearn.tree import DecisionTreeRegressor

# Membuat instance DecisionTreeRegressor
regressor = DecisionTreeRegressor(
    criterion='squared_error',  # Fungsi untuk mengukur kualitas split. Pilihan: 'squared_error', 'friedman_mse', 'absolute_error', 'poisson'. Default: 'squared_error'
    splitter='best',  # Strategi untuk memilih split di setiap node. Pilihan: 'best', 'random'. Default: 'best'
    max_depth=None,  # Kedalaman maksimum dari pohon. Jika None, node akan diperluas sampai semua daun murni atau mengandung kurang dari min_samples_split sampel. Default: None
    min_samples_split=2,  # Jumlah minimum sampel yang diperlukan untuk membagi node internal. Default: 2
    min_samples_leaf=1,  # Jumlah minimum sampel yang diperlukan untuk berada di node daun. Default: 1
    min_weight_fraction_leaf=0.0,  # Fraksi bobot minimum dari total bobot yang diperlukan untuk berada di node daun. Default: 0.0
    max_features=None,  # Jumlah fitur yang dipertimbangkan saat mencari split terbaik. Default: None
    random_state=None,  # Mengontrol keacakan estimator. Default: None
    max_leaf_nodes=None,  # Jumlah maksimum node daun dalam pohon. Default: None
    min_impurity_decrease=0.0,  # Ambang batas untuk pengurangan impuritas. Default: 0.0
    ccp_alpha=0.0  # Parameter kompleksitas untuk pruning minimal cost-complexity. Default: 0.0
)

# Melatih regressor dengan data pelatihan
regressor.fit(X_train, y_train)
