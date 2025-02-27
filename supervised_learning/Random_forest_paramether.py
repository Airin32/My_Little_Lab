from sklearn.ensemble import RandomForestClassifier

# Membuat instance RandomForestClassifier
clf = RandomForestClassifier(
    n_estimators=100,  # Jumlah pohon dalam hutan. Default: 100
    criterion='gini',  # Fungsi untuk mengukur kualitas split. Pilihan: 'gini', 'entropy', 'log_loss'. Default: 'gini'
    max_depth=None,  # Kedalaman maksimum dari pohon. Jika None, node akan diperluas sampai semua daun murni atau mengandung kurang dari min_samples_split sampel. Default: None
    min_samples_split=2,  # Jumlah minimum sampel yang diperlukan untuk membagi node internal. Default: 2
    min_samples_leaf=1,  # Jumlah minimum sampel yang diperlukan untuk berada di node daun. Default: 1
    min_weight_fraction_leaf=0.0,  # Fraksi bobot minimum dari total bobot yang diperlukan untuk berada di node daun. Default: 0.0
    max_features='sqrt',  # Jumlah fitur yang dipertimbangkan saat mencari split terbaik. Default: 'sqrt'
    max_leaf_nodes=None,  # Jumlah maksimum node daun dalam pohon. Default: None
    min_impurity_decrease=0.0,  # Ambang batas untuk pengurangan impuritas. Default: 0.0
    bootstrap=True,  # Apakah menggunakan bootstrap sampel saat membangun pohon. Default: True
    oob_score=False,  # Apakah menggunakan sampel out-of-bag untuk memperkirakan akurasi umum. Default: False
    n_jobs=None,  # Jumlah pekerjaan yang dijalankan secara paralel. Default: None
    random_state=None,  # Mengontrol keacakan estimator. Default: None
    verbose=0,  # Mengontrol tingkat detail dari output. Default: 0
    warm_start=False,  # Apakah menggunakan solusi dari panggilan sebelumnya untuk menyesuaikan dan menambah estimator. Default: False
    class_weight=None,  # Bobot yang terkait dengan kelas. Default: None
    ccp_alpha=0.0,  # Parameter kompleksitas untuk pruning minimal cost-complexity. Default: 0.0
    max_samples=None  # Jumlah maksimum sampel yang diambil dari bootstrap sampel untuk membangun setiap pohon. Default: None
)

# Melatih classifier dengan data pelatihan
clf.fit(X_train, y_train)
from sklearn.ensemble import RandomForestRegressor

# Membuat instance RandomForestRegressor
regressor = RandomForestRegressor(
    n_estimators=100,  # Jumlah pohon dalam hutan. Default: 100
    criterion='squared_error',  # Fungsi untuk mengukur kualitas split. Pilihan: 'squared_error', 'absolute_error', 'friedman_mse', 'poisson'. Default: 'squared_error'
    max_depth=None,  # Kedalaman maksimum dari pohon. Jika None, node akan diperluas sampai semua daun murni atau mengandung kurang dari min_samples_split sampel. Default: None
    min_samples_split=2,  # Jumlah minimum sampel yang diperlukan untuk membagi node internal. Default: 2
    min_samples_leaf=1,  # Jumlah minimum sampel yang diperlukan untuk berada di node daun. Default: 1
    min_weight_fraction_leaf=0.0,  # Fraksi bobot minimum dari total bobot yang diperlukan untuk berada di node daun. Default: 0.0
    max_features=1.0,  # Jumlah fitur yang dipertimbangkan saat mencari split terbaik. Default: 1.0
    max_leaf_nodes=None,  # Jumlah maksimum node daun dalam pohon. Default: None
    min_impurity_decrease=0.0,  # Ambang batas untuk pengurangan impuritas. Default: 0.0
    bootstrap=True,  # Apakah menggunakan bootstrap sampel saat membangun pohon. Default: True
    oob_score=False,  # Apakah menggunakan sampel out-of-bag untuk memperkirakan akurasi umum. Default: False
    n_jobs=None,  # Jumlah pekerjaan yang dijalankan secara paralel. Default: None
    random_state=None,  # Mengontrol keacakan estimator. Default: None
    verbose=0,  # Mengontrol tingkat detail dari output. Default: 0
    warm_start=False,  # Apakah menggunakan solusi dari panggilan sebelumnya untuk menyesuaikan dan menambah estimator. Default: False
    ccp_alpha=0.0,  # Parameter kompleksitas untuk pruning minimal cost-complexity. Default: 0.0
    max_samples=None  # Jumlah maksimum sampel yang diambil dari bootstrap sampel untuk membangun setiap pohon. Default: None
)

# Melatih regressor dengan data pelatihan
regressor.fit(X_train, y_train)
