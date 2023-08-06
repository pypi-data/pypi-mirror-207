import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class obrpy(object):
    """
        Main class for correct management of .obr files

            Initialization:
            
                An object of class obrpy can be initialized either by specifying the path or leaving it unspecified, 
                in this case, a wizard will be displayed to select the folder where the .obr and other files will 
                be saved.

            Atributes:

                path (str)                       : absolute path to the root folder
                name (str)                       : name of the root folder (used as the name of the object) 
                folders (dict)                   : dictionary with the name of the folders where different files are storaged
                INFO (dict)                      : dictionary which contains the name of each external file created by this clase
                OBRfiles (dict)                  : dictionary which contains all OBRfile objects labeled with its filename
                settings (obj of class Settings) : object which contains all settings information

            Methods:

                - obr -
                mainOBR()               
                genOBRbook()        
                computeOBR()        
                update_OBRfiles()  

                - obrsdk -
                OBRSDKcalibration() 
                OBRSDKalignment()
                OBRSDKscan()
                OBRSDKextendedScan()

                - settings -
                genSettingsTemplate()
                genSettings()

                - load -
                load()              
                
                - save -
                save()              
                save_OBRfiles()     
                save_something()
                save_settings()   

                - update -
                update_OBRfiles() 
                update_OBRbook()
                update_settings()

            Classes:

                OBRfile()
                Settings()
    """

    def __init__(self,path=None,showpath=False) -> None:


        ######### Folder definition #########

        # Launch GUI if no path is provided
        if not path:
            from .PathSelector import PathSelector
            import tkinter as tk
            # Initialize gui
            root = tk.Tk()
            root.geometry("400x100")
            root.title("Path Selector")

            # Create gui
            app = PathSelector(master=root)
            app.pack_propagate(0)
            app.mainloop()

            # Get path
            path = app.path

        # In construction generates absolute path and name based on the folder name
        self.path = os.path.abspath(path)
        self.name = f'{os.path.basename(os.path.normpath(path))}.pkl'

        # Just to check it
        if showpath:
             print(os.listdir(self.path))

        ######### Load or creation #########

        # Tries to load dataset object, else, if not found, creates one
        try:      
            self.load()

        except Exception as e:
            if 'No such file or directory' in str(e):
                print('No obrpy object found in path')
                print('Creating new one \n')
                self.new()
            else:
                print(e)
                exit()

            

    ######### Classes definitions #########

    class OBRfile(object):
        """ Container class for '.obr' file information """

        def __init__(self,ID,filename,date):

            self.ID             = ID             # see ID_generator() for information
            self.filename       = filename
            self.name           = filename.replace('.obr','')
            self.date           = date           # %Y,%M,%D,%h:%m:%s
            self.f              = None           # [GHz]
            self.z              = None           # [m]
            self.Data           = None           # P, S
    
    class Settings(object):
        """ Class to manage settings information """

        def __init__(self,situation):

            self.situation = situation         
            self.info = {'Calibration':None,'Test':None}

    class Signal(object):

        """ Class to contain all singal analysis functions available """

        def __init__(self) -> None:
            pass

        from .SIGNAL.cross_spectrum import PSSS
        from .SIGNAL.spectral_shift import spectral_shift, spectral_shift_GPU

    

    ######### Methods definitions #########

    # from .take_a_look import take_a_look # TO BE DONE

    from .load import load, new

    from .save import save, save_something , save_OBRbook, save_OBRfiles, save_settings

    from .update import update_OBRbook, update_OBRfiles, update_settings

    from .obr import mainOBR, genOBRbook, computeOBR

    from .obrsdk import OBRSDKcalibration, OBRSDKalignment, OBRSDKscan, OBRSDKextendedScan

    from .settings import genSettingsTemplate, genSettings, _getNewValuesFromOBRbook

    from .ANALYSIS.global_analysis import global_analysis, global_analysis_GPU
