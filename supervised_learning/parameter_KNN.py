from sklearn.neighbors import KNeighborsClassifier

# Membuat instance KNeighborsClassifier
knn_clf = KNeighborsClassifier(
    n_neighbors=5,  # Jumlah tetangga yang digunakan untuk query kneighbors. Default: 5
    weights='uniform',  # Fungsi bobot yang digunakan dalam prediksi. Pilihan: 'uniform', 'distance'. Default: 'uniform'
    algorithm='auto',  # Algoritma yang digunakan untuk menghitung tetangga terdekat. Pilihan: 'auto', 'ball_tree', 'kd_tree', 'brute'. Default: 'auto'
    leaf_size=30,  # Ukuran daun yang diteruskan ke BallTree atau KDTree. Default: 30
    p=2,  # Parameter kekuatan untuk metrik Minkowski. Default: 2 (Euclidean distance)
    metric='minkowski',  # Metrik yang digunakan untuk menghitung jarak. Default: 'minkowski'
    metric_params=None,  # Parameter tambahan untuk fungsi metrik. Default: None
    n_jobs=None  # Jumlah pekerjaan paralel yang dijalankan untuk pencarian tetangga. Default: None
)

# Melatih classifier dengan data pelatihan
knn_clf.fit(X_train, y_train)
from sklearn.neighbors import KNeighborsRegressor

# Membuat instance KNeighborsRegressor
knn_reg = KNeighborsRegressor(
    n_neighbors=5,  # Jumlah tetangga yang digunakan untuk query kneighbors. Default: 5
    weights='uniform',  # Fungsi bobot yang digunakan dalam prediksi. Pilihan: 'uniform', 'distance'. Default: 'uniform'
    algorithm='auto',  # Algoritma yang digunakan untuk menghitung tetangga terdekat. Pilihan: 'auto', 'ball_tree', 'kd_tree', 'brute'. Default: 'auto'
    leaf_size=30,  # Ukuran daun yang diteruskan ke BallTree atau KDTree. Default: 30
    p=2,  # Parameter kekuatan untuk metrik Minkowski. Default: 2 (Euclidean distance)
    metric='minkowski',  # Metrik yang digunakan untuk menghitung jarak. Default: 'minkowski'
    metric_params=None,  # Parameter tambahan untuk fungsi metrik. Default: None
    n_jobs=None  # Jumlah pekerjaan paralel yang dijalankan untuk pencarian tetangga. Default: None
)

# Melatih regressor dengan data pelatihan
knn_reg.fit(X_train, y_train)
