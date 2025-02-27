import joblib 
from tensorflow import keras
import pandas as pd 
import numpy as np 
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Machine_Prototype :
    def __init__ (self):
        pass 

    def target_data (self):
        pass
    def machine_main (self):
        pass 

class MACHINE_STATUS_CHECKER (Machine_Prototype) : 
    def __init__(self,Data):
        super().__init__()
        self.__Data = Data
        self.__machine = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/checking_status_Machines.pkl')
    
    def target_data(self):
        return self.__Data.values

    def Machine_main(self):
        machine = self.__machine
        data = self.target_data()
        return machine.predict(data)

class  COMPONEN_CHECKER_ENGINE_SYSTEM (Machine_Prototype):
    def __init__(self,cpu_data,disk_data,ram_data,network_data):
        super().__init__()
        self.__cpu_data = cpu_data
        self.__disk_data = disk_data
        self.__ram_data = ram_data
        self.__network_data = network_data
        self.__cpu_checker = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/cpu_checker.pkl')
        self.__ram_checker = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/ram_checker.pkl')
        self.__diks_checker = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/Disk_checker.pkl')
        self.__network_checker = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/Network_Checker.pkl')
    
    def machine_main (self):
        cpu_target = self.__cpu_data.values.reshape(-1,1)
        disk_target = self.__disk_data.values.reshape(-1,1)
        ram_target = self.__ram_data.values.reshape(-1,1)
        network_target = self.__network_data.values.reshape(-1,1)
        cpu_machine_checker = self.__cpu_checker
        ram_machine_checker = self.__ram_checker
        disk_machine_checker = self.__diks_checker
        network_machine_checker = self.__network_checker

        cpu_result = cpu_machine_checker.predict(cpu_target)
        disk_result = disk_machine_checker.predict(disk_target)
        ram_result = ram_machine_checker.predict(ram_target)
        network_result = network_machine_checker.predict(network_target)
        data = pd.DataFrame(data={'cpu_warning' : cpu_result,'disk_warning' : disk_result,'ram_warning' : ram_result,'network_warning' : network_result})
        return data

class  ABNORMAL_CHECKER_MACHINE (Machine_Prototype) :
    def __init__ (self,machine_data) :
        super().__init__()
        self.__machine_data = machine_data
        self.__Abnormal_machine_checker = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/abnormal_level_decision.pkl')

    def target_data(self):
        target_data = self.__machine_data
        return target_data
    
    def main_machine(self) :
        target_data = self.target_data()
        abnormal_machine_checker = self.__Abnormal_machine_checker
        result = abnormal_machine_checker.predict(target_data)
        return result

class CONFIRMERS_STATUS_TO_ACTION (Machine_Prototype) :
    def __init__(self,target_data):
        super().__init__()
        self.__target_data = target_data
        self.__machine = joblib.load('C:/Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/confimer_machine.pkl')
    
    
    def target_data(self):
        target_data = self.__target_data.values
        return target_data
    
    def machine_main(self):
        machine = self.__machine
        target_data = self.target_data()
        confimation_result = machine.predict(target_data)
        return confimation_result

class Machine_deep_Scaners :
    def __init__ (self):
        pass 

    def Main_machine (self) :
        pass 

    def Probability_Counter (self) :
        pass

class Log_Scaners (Machine_deep_Scaners) :
    def __init__ (self,Target):
        super().__init__()
        self.__Target = Target
        self.__Model_Machine = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/Abnormal_Activity_Detector.pkl')
        self.__encoder_log = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/log_encoder.pkl')
        self.__encoder_Sw = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/Sofware_encoder.pkl')
    def Main_machine(self):
        Target = self.__Target
        log_encoder = self.__encoder_log
        Software_encoder = self.__encoder_Sw
        Target['Log Activity'] = log_encoder.transform(Target['Log Activity'])
        Target['Software'] = Software_encoder.transform(Target['Software'])
        machine = self.__Model_Machine
        result = machine.predict(Target)
        return result 
    
class User_pattern_Scanners (Machine_deep_Scaners) :
    def __init__(self,target):
        super().__init__()
        self.__target = target 
        self.__tokenizer = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/Tokenizer_Activity.pkl')
        self.__Model_Machine = keras.models.load_model('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/User_pattern_Detector.keras')
    def Main_machine(self):
        target = self.__target
        tokenizer = self.__tokenizer
        Model_Machine = self.__Model_Machine
        predict_target = tokenizer.texts_to_sequences(target)
        predict_target = pad_sequences(predict_target,maxlen=17,padding='post')
        result = Model_Machine.predict(predict_target)
        return result 

class Profil_detector_Scanner (Machine_deep_Scaners) :
    def __init__(self,Target):
        super().__init__()
        self.__Target = Target 
        self.__Machine_Models = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/Profil_detector.pkl')

    
    def Main_machine(self):
        Target = self.__Target
        Machine_Models = self.__Machine_Models
        result = Machine_Models.predict(Target)
        return result 

class Network_Step_Scanners (Machine_deep_Scaners) :
    def __init__(self,Target):
        super().__init__()
        self.__target = Target
        self.__Machine_Models = joblib.load('C:/Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/Ip_Abnormal_Detector.pkl')
        self.__encoder = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/IP_machine_Encoder.pkl')
    
    def Main_machine(self):
        target = self.__target 
        Machine_Models = self.__Machine_Models
        enc = self.__encoder
        target['Protocols'] = enc.transform(target['Protocols'])
        for i in range(len(target['Protocols'])) :
            try :
                data_ip = enc.transform([target.loc[i,'Ip']])
                target.loc[i,'Ip'] = data_ip[0]
            except :
                print("Anomali Detected!! Encoder can't get it")
                rand_data = [1000,2000,3000]
                target.loc[i,'Ip'] = random.choice(rand_data)
            
            try :
                data_Foreign= enc.transform([target.loc[i,'Foreign']])
                target.loc[i,'Foreign'] = data_Foreign[0]
            except :
                print("Anomali Detected!! Encoder can't get it")
                rand_data = [10000,20000,30000]
                target.loc[i,'Foreign'] = random.choice(rand_data)

        target['State'] = enc.transform(target['State'])
        target = target.values
        results = Machine_Models.predict(target)
        return results
class Security_Abnormal_Reported (Machine_deep_Scaners) :
    def __init__(self,Target):
        super().__init__()
        self.__Target = Target
        self.__Machine_Models = joblib.load('C://Users/ASUS/Documents/Kognitiff_neuron_project/NLP_with_TF/Security_log_machine.pkl')
    
    def Main_machine(self):
        Target = self.__Target
        Machine_Models = self.__Machine_Models
        result = Machine_Models.predict(Target)
        return result 
    
class Scanners_System :
    def __init__(self,Target):
        self.__Target = Target

    def Logisctic_Scanners (self):
        Target = self.__Target
        Scanners_Machine = COMPONEN_CHECKER_ENGINE_SYSTEM(cpu_data=Target['Cpu'],ram_data=Target['Ram'],
                                                          disk_data=Target['Diks'],network_data=Target['Network'])
        result = Scanners_Machine.machine_main()
        return result['cpu_warning'],result['disk_warning'],result['ram_warning'],result['network_warning']
    
    def Log_status_system_scanners (self):
        target = self.__Target 
        cpu_warning,diks_wanrning,ram_warning,network_warning = self.Logisctic_Scanners()
        target['cpu warning'] = cpu_warning
        target['disk warning'] = diks_wanrning
        target['ram warning'] = ram_warning
        target['network warning'] = network_warning
        Scanner_Machine = MACHINE_STATUS_CHECKER(target)
        return Scanner_Machine.Machine_main()
    
    def Confirmer_To_DeepScanners (self) :
        try :
            data_scaners = self.__Target
            target1,target2,target3,target4 = self.Logisctic_Scanners()
            dataset = pd.DataFrame(data={'data1' : target1,'data2' : target2,'data3' : target3, 'data4' : target4})
            Decision = None 
            confirme_decision = self.Log_status_system_scanners()
            if 1 in confirme_decision :
                print("Abnormal in System Detected!! Scaning Start")
                Machine_Decision = ABNORMAL_CHECKER_MACHINE(dataset.values)
                Status_level = Machine_Decision.main_machine()
                System_state_Average = np.array((data_scaners['Cpu'].values + data_scaners['Ram'].values + data_scaners['Diks'].values + data_scaners['Network'].values) / 4 )
                confirmers_target = pd.DataFrame(data={'System_state' : System_state_Average,'status Level' : Status_level})
                Machine_confirmers= CONFIRMERS_STATUS_TO_ACTION(confirmers_target)
                Decision = Machine_confirmers.machine_main()
            else :
                print("Normal Detected!! No Scaning")
        except :
            print("Warning Basic Scanners Get Critics Damage, need regeneration")
        return Decision
            
class Deep_Scaners_System :
    def __init__(self,Target,Activity_users,Network_Activity):
        self.__Target = Target
        self.__Activity_users = Activity_users
        self.__Network_Activity = Network_Activity
    
    def Log_Activation_System (self) :
        try :
            Target = self.__Target
            Machine_models = Log_Scaners(Target)
            result = Machine_models.Main_machine()
                
        except :
            print("Something Wrong With input")
        return result
    
    def Users_actitivity_Pattern (self):
        try :
            Target = self.__Activity_users
            Machine_Models = User_pattern_Scanners(target=Target)
            result = Machine_Models.Main_machine()
        except :
            print("Something Wrong with Input")
        return result
    
    def Network_Activity (self) :
        try :
            target = self.__Network_Activity 
            Machine_Models = Network_Step_Scanners(target)
            result = Machine_Models.Main_machine()
        except :
            print("Something Wrong with Input")
        return result
    
    def Non_profil_detector (self) :
        try : 
            Target = self.Users_actitivity_Pattern()
            Target = np.array(Target).flatten()
            Target = np.array([i * 100 for i in Target])
            Target = np.array(Target).reshape(-1,1)
            Model_Machine = Profil_detector_Scanner(Target)
            result = Model_Machine.Main_machine()
        except :
            print("Error : Something Wrong with input")
        return result
    
    def Security_Warning_reported (self,Target) :
        Model_Machine = Security_Abnormal_Reported(Target)
        result = Model_Machine.Main_machine()
        return result 

class Virutual_Computer :
    def __init__(self,Interuption_System) :
        self.__Interup_System = Interuption_System
        self.__Cpu = np.array([np.random.randint(10,30) / 100 for i in range(100)])
        self.__Ram = np.array([np.random.randint(10,30) / 100 for i in range(100)])
        self.__Diks = np.array([np.random.randint(10,30) / 100 for i in range(100)])
        self.__Network = np.array([np.random.randint(10,30) / 100 for i in range(100)])
        self.__drive = np.array(['Drive Gpu','Drive OS','Drive Ram','Drive Disk','Drive Monitor'])
        self.__internal_sw = np.array(['Music player','Video player','Chrome','Fire fox','File Manager','Microsoft Software','Defender','Fire wall',
                        'Setting'])
        self.__eksternal_sw = np.array(['Left 4 dead','Video Editor','IDE Programming','Microsoft Office','Foto Editor',
                         'GNS3','Virtual Machine','Cisco','Game'])
    @property 
    def System_Manager (self) :
        data_Frame = pd.DataFrame(data={'Cpu' : self.__Cpu,'Ram' : self.__Ram,'Diks' : self.__Diks,'Network' : self.__Network})
        return data_Frame
    
    @property
    def Software_Hardware (self) :
        Software = np.concatenate([self.__drive,self.__internal_sw,self.__eksternal_sw])
        Log_activity = np.array(['Gpu managing','OS managing','Ram managing','Disk managing',
                        'Monitor managing','Playing Music','Playing Video','Browsing',
                        'Browsing','File managing','Microsoft work','System Protect',
                        'System Protect','System managing','Playing Game','Edit Video',
                        'Programing','Microsft work','Foto Editing','Network Protyping',
                        'Virtual Machine','Network Protyping','Playing Game'])
        Log = []
        SW = [] 
        ram = []
        for i in range(50) :
            SW.append(np.random.choice(Software))
            Log.append(np.random.choice(Log_activity))
            ram.append(np.random.randint(10,50) / 100)
            if self.__Interup_System == 'Attack' :
                SW.append(np.random.choice(Software))
                Log.append(np.random.choice(Log_activity))
                ram.append(np.random.randint(60,100) / 100)
        Activity = pd.DataFrame(data={'Software' : SW,'Log Activity' : Log,'Ram Use' : ram})
        return Activity

    @property 
    def user_pattern (self):
        Software = np.concatenate([self.__drive,self.__internal_sw,self.__eksternal_sw])
        time = ['pagi','siang','malam']
        pattern = [] 
        for i in range(10) :
            app = Software[np.random.randint(1,22)] +', '+ Software[np.random.randint(1,22)] + ','+ Software[np.random.randint(1,22)] +', '+ np.random.choice(time)
            pattern.append(app)
        return pattern
    def System_Manager_Interaction (self):
        cpu = np.array([np.random.randint(0,100) / 100])
        ram = np.array([np.random.randint(0,100) / 100])
        diks = np.array([np.random.randint(0,100) / 100])
        network = np.array([np.random.randint(0,100) / 100])
        return pd.DataFrame(data={
            'Cpu' : cpu,
            'Ram' : ram,
            'Diks' : diks,
            'Network' : network
        })
    def Trigger_Attack (self) :
        cpu = np.array([np.random.randint(60,100) /100 for i in range(5)])
        ram = np.array([np.random.randint(60,100) /100 for i in range(5)])
        diks = np.array([np.random.randint(60,100) /100 for i in range(5)])
        network = np.array([np.random.randint(60,100) /100 for i in range(5)])
        return pd.DataFrame(data={
            'Cpu' : cpu,
            'Ram' : ram,
            'Diks' : diks,
            'Network' : network
        })
    @property
    def Network_Acivity(self) :
        Local_Ip_trust = ['192.168.56.1','192.168.7.101','.127.0.0.1']
        Foreign_Ip_Trust = ['127.0.0.1','20.198.118.190','216.24.57.252','64.233.170.188','20.212.88.177','172.64.155.209',
                    '104.18.32.47','142.251.12.132','23.33.184.226','150.171.31.254']
        State = ['Listening','Established','Time Wait','Close Wait']
        Protocol_dont_Trust = ['Ftp','Telnet','NBT','SMB','HTTPS','BitTorrent','C&C']
        ip = []
        fore_ip = []
        Sty = []
        pro = [] 
        for i in range(10) :
            ip.append(np.random.choice(Local_Ip_trust))
            fore_ip.append(np.random.choice(Foreign_Ip_Trust))
            Sty.append(np.random.choice(State))
            pro.append('Tcp')
            if (self.__Interup_System == 'Attack'):
                ip.append(np.random.choice(['192.177.111.22','192.168.22.11','1.1.22.111','200.444.88.1']))
                pro.append(np.random.choice(Protocol_dont_Trust))
                fore_ip.append(np.random.choice(['200.100.11','111.999.222','192.111.11.1','233.3443.234']))
                Sty.append(np.random.choice(State))
        Network_Triggers = pd.DataFrame(data={'Protocols' : pro,'Ip' : ip,'Foreign' : fore_ip,'State' : Sty})
        return Network_Triggers

    def System_Knightbot_Scanning (self) :
        Target = self.System_Manager_Interaction()
        if self.__Interup_System == 'Attack' :
            Target = self.Trigger_Attack()

        machine = Scanners_System(Target)
        print("=================================================================================")
        print("Scanning Log : ")
        print("Component Status : \n ",machine.Logisctic_Scanners())
        print("Log System Scaning : \n ",machine.Log_status_system_scanners)
        print("log decision to deeep scaners : \n ",machine.Confirmer_To_DeepScanners())
        print("=================================================================================")
        data = machine.Confirmer_To_DeepScanners()     
        if data is not None and 1 in data :
            deep_machine_scann = Deep_Scaners_System(Target=self.Software_Hardware,Activity_users=self.user_pattern,Network_Activity=self.Network_Acivity)
            Abnormal_Log = deep_machine_scann.Log_Activation_System()
            Abnormal_pattern = deep_machine_scann.Users_actitivity_Pattern()
            abnormal_network = deep_machine_scann.Network_Activity()
            abnormal_profil = deep_machine_scann.Non_profil_detector()
            return Abnormal_Log,Abnormal_pattern,abnormal_network,abnormal_profil
        return 'Normal','Normal','Normal','Normal'

if __name__ == '__main__' :
    run = True 
    while run : 
        decision = None
        print("1. Attacks!!")
        print("2. Stop !!")
        print("3. Shutdown")
        choice = int(input("Choice (1/2) : "))
        if choice == 1 :
            decision = 'Attack'
        elif choice == 2:
            decision = 'Non'
        Testing =  Virutual_Computer(Interuption_System=decision)
        Log,patter,network,profil=Testing.System_Knightbot_Scanning()
        print("=============================================================================")
        print( "Log System Scanned : \n",Log)
        print("=============================================================================")
        print("Pattern Users Scanned : \n",patter)
        print("=============================================================================")
        print("Network Activity Scaned : \n",network)
        print("=============================================================================")
        print("Profil Detector Scanned : \n",profil)
        print("=============================================================================")

        if choice == 3 :
            run = False 