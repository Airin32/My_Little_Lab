from sklearn.neural_network import MLPClassifier

# Membuat instance MLPClassifier
mlp_clf = MLPClassifier(
    hidden_layer_sizes=(100,),  # Jumlah neuron di setiap lapisan tersembunyi. Default: (100,)
    activation='relu',  # Fungsi aktivasi untuk lapisan tersembunyi. Pilihan: 'identity', 'logistic', 'tanh', 'relu'. Default: 'relu'
    solver='adam',  # Algoritma untuk optimasi bobot. Pilihan: 'lbfgs', 'sgd', 'adam'. Default: 'adam'
    alpha=0.0001,  # Kekuatan dari regularisasi L2. Default: 0.0001
    batch_size='auto',  # Ukuran minibatch untuk optimasi stokastik. Default: 'auto'
    learning_rate='constant',  # Jadwal laju pembelajaran. Pilihan: 'constant', 'invscaling', 'adaptive'. Default: 'constant'
    learning_rate_init=0.001,  # Laju pembelajaran awal. Default: 0.001
    power_t=0.5,  # Eksponen untuk invscaling laju pembelajaran. Default: 0.5
    max_iter=200,  # Jumlah maksimum iterasi. Default: 200
    shuffle=True,  # Apakah data akan diacak setiap epoch. Default: True
    random_state=None,  # Mengontrol keacakan estimator. Default: None
    tol=0.0001,  # Toleransi untuk optimasi. Default: 0.0001
    verbose=False,  # Apakah akan mencetak pesan kemajuan ke stdout. Default: False
    warm_start=False,  # Apakah menggunakan solusi dari panggilan sebelumnya untuk menyesuaikan dan menambah estimator. Default: False
    momentum=0.9,  # Momentum untuk optimasi stokastik. Default: 0.9
    nesterovs_momentum=True,  # Apakah menggunakan momentum Nesterov. Default: True
    early_stopping=False,  # Apakah menghentikan pelatihan lebih awal jika skor validasi tidak meningkat. Default: False
    validation_fraction=0.1,  # Fraksi data pelatihan yang digunakan sebagai data validasi jika early_stopping adalah True. Default: 0.1
    beta_1=0.9,  # Parameter beta1 untuk optimizer Adam. Default: 0.9
    beta_2=0.999,  # Parameter beta2 untuk optimizer Adam. Default: 0.999
    epsilon=1e-08,  # Nilai epsilon untuk stabilitas numerik dalam optimizer Adam. Default: 1e-08
    n_iter_no_change=10,  # Jumlah iterasi tanpa perubahan untuk menghentikan pelatihan lebih awal. Default: 10
    max_fun=15000  # Jumlah maksimum evaluasi fungsi dalam solver lbfgs. Default: 15000
)

# Melatih classifier dengan data pelatihan
mlp_clf.fit(X_train, y_train)
from sklearn.neural_network import MLPRegressor

# Membuat instance MLPRegressor
mlp_reg = MLPRegressor(
    hidden_layer_sizes=(100,),  # Jumlah neuron di setiap lapisan tersembunyi. Default: (100,)
    activation='relu',  # Fungsi aktivasi untuk lapisan tersembunyi. Pilihan: 'identity', 'logistic', 'tanh', 'relu'. Default: 'relu'
    solver='adam',  # Algoritma untuk optimasi bobot. Pilihan: 'lbfgs', 'sgd', 'adam'. Default: 'adam'
    alpha=0.0001,  # Kekuatan dari regularisasi L2. Default: 0.0001
    batch_size='auto',  # Ukuran minibatch untuk optimasi stokastik. Default: 'auto'
    learning_rate='constant',  # Jadwal laju pembelajaran. Pilihan: 'constant', 'invscaling', 'adaptive'. Default: 'constant'
    learning_rate_init=0.001,  # Laju pembelajaran awal. Default: 0.001
    power_t=0.5,  # Eksponen untuk invscaling laju pembelajaran. Default: 0.5
    max_iter=200,  # Jumlah maksimum iterasi. Default: 200
    shuffle=True,  # Apakah data akan diacak setiap epoch. Default: True
    random_state=None,  # Mengontrol keacakan estimator. Default: None
    tol=0.0001,  # Toleransi untuk optimasi. Default: 0.0001
    verbose=False,  # Apakah akan mencetak pesan kemajuan ke stdout. Default: False
    warm_start=False,  # Apakah menggunakan solusi dari panggilan sebelumnya untuk menyesuaikan dan menambah estimator. Default: False
    momentum=0.9,  # Momentum untuk optimasi stokastik. Default: 0.9
    nesterovs_momentum=True,  # Apakah menggunakan momentum Nesterov. Default: True
    early_stopping=False,  # Apakah menghentikan pelatihan lebih awal jika skor validasi tidak meningkat. Default: False
    validation_fraction=0.1,  # Fraksi data pelatihan yang digunakan sebagai data validasi jika early_stopping adalah True. Default: 0.1
    beta_1=0.9,  # Parameter beta1 untuk optimizer Adam. Default: 0.9
    beta_2=0.999,  # Parameter beta2 untuk optimizer Adam. Default: 0.999
    epsilon=1e-08,  # Nilai epsilon untuk stabilitas numerik dalam optimizer Adam. Default: 1e-08
    n_iter_no_change=10,  # Jumlah iterasi tanpa perubahan untuk menghentikan pelatihan lebih awal. Default: 10
    max_fun=15000  # Jumlah maksimum evaluasi fungsi dalam solver lbfgs. Default: 15000
)

# Melatih regressor dengan data pelatihan
mlp_reg.fit(X_train, y_train)
