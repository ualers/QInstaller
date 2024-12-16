import sys
import os
import ctypes
import shutil
import subprocess
import time
import concurrent.futures
import winshell
import pythoncom
import zipfile
from win32com.client import Dispatch

from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide2.QtCore import QThread, Signal
from PySide2extn.RoundProgressBar import roundProgressBar

from src_.icones_interpreter import *
from src_.ui_installer import Ui_MainWindow
from Custom_Widgets import loadJsonStyle
from Custom_Widgets.QCustomModals import QCustomModals

class GenericInstaller(QThread):
    """
    A multi-purpose, flexible installer for software applications on Windows.
    
    Features:
    - Multi-threaded file copying
    - Automatic shortcut creation
    - Dependency management
    - Progress tracking
    - Cross-platform compatibility considerations
    """
    
    progress = Signal(int)
    label_path_src_installing = Signal(str)
    finish = Signal()
    update_success = Signal(str)
    
    def __init__(self, 
                 install_path, 
                 exe_path, 
                 software_path, 
                 dependencies_path, 
                 dependencies_destination,
                 python_package_path,
                 python_package_destination):
        """
        Initialize the installer with paths for various components.
        
        Args:
            install_path (str): Target installation directory
            exe_path (str): Path to the main executable
            software_path (str): Source directory for software files
            dependencies_path (str): Source directory for dependencies
            dependencies_destination (str): Target directory for dependencies
            python_package_path (str): Path to compressed Python package
            python_package_destination (str): Extraction destination for Python package
        """
        super().__init__()
        self.install_path = install_path
        self.exe_path = exe_path
        self.software_path = software_path
        self.dependencies_path = dependencies_path
        self.dependencies_destination = dependencies_destination
        self.python_package_path = python_package_path
        self.python_package_destination = python_package_destination

    def run(self):
        """
        Main installation method. Handles file copying and package extraction.
        """
        # Shortcut creation
        self.create_desktop_shortcut(self.exe_path, "One-Click IP Rotation")
        
        # Copy software files
        self._copy_files(self.software_path, self.install_path)
        
        # Copy dependencies
        self._copy_files(self.dependencies_path, self.dependencies_destination)
        
        # Extract Python package
        self._extract_package(self.python_package_path, self.python_package_destination)
        
        self.progress.emit(100)
        self.finish.emit()

    def _copy_files(self, source_dir, destination_dir):
        """
        Multi-threaded file copying with progress tracking.
        
        Args:
            source_dir (str): Source directory
            destination_dir (str): Destination directory
        """
        files_to_copy = [
            os.path.join(root, file)
            for root, _, files in os.walk(source_dir)
            for file in files
        ]
        
        total_files = len(files_to_copy)
        copied_files = 0
        
        def copy_single_file(src_file):
            nonlocal copied_files
            relative_path = os.path.relpath(src_file, source_dir)
            dest_file = os.path.join(destination_dir, relative_path)
            
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copy2(src_file, dest_file)
            
            self.label_path_src_installing.emit(dest_file)
            
            copied_files += 1
            progress_percent = int((copied_files / total_files) * 100)
            self.progress.emit(progress_percent)
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            list(executor.map(copy_single_file, files_to_copy))

    def _extract_package(self, package_path, destination):
        """
        Extract compressed package with progress tracking.
        
        Args:
            package_path (str): Path to compressed package
            destination (str): Extraction destination
        """
        os.makedirs(destination, exist_ok=True)
        
        with zipfile.ZipFile(package_path, 'r') as zip_ref:
            total_files = len(zip_ref.infolist())
            
            for index, file_info in enumerate(zip_ref.infolist(), start=1):
                zip_ref.extract(file_info, destination)
                
                self.progress.emit(int((index / total_files) * 100))
                self.label_path_src_installing.emit(f"{destination}\\{file_info.filename}")

    def create_desktop_shortcut(self, exe_path, description=None):
        """
        Create a desktop shortcut for the installed application.
        
        Args:
            exe_path (str): Path to executable
            description (str, optional): Shortcut description
        """
        try:
            pythoncom.CoInitialize() 
            shell = Dispatch('WScript.Shell')
            desktop = shell.SpecialFolders("Desktop")
            filename = os.path.splitext(os.path.basename(exe_path))[0]  
            shortcut_path = os.path.join(desktop, filename + ".lnk")
            
            shortcut = shell.CreateShortcut(shortcut_path)
            shortcut.TargetPath = exe_path
            shortcut.WorkingDirectory = os.path.dirname(exe_path)
            shortcut.Description = description or f"Shortcut for {filename}"
            shortcut.Save()
            
            self.update_success.emit("Shortcut successfully created on the desktop!")
        except Exception as e:
            print(f"Shortcut creation error: {e}")
        finally:
            pythoncom.CoUninitialize()  

def ensure_admin_privileges():
    """
    Ensure the script runs with administrator privileges.
    Restart with elevated permissions if needed.
    """
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Administrator privileges required. Restarting with elevation...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, 
            '"' + '" "'.join(sys.argv) + '"', 
            None, 1
        )
        sys.exit(0)

class Main_installer(QMainWindow):
    """
    Main installer window with configurable UI and installation workflow.
    """
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._configure_ui()
        self._connect_signals()

        loadJsonStyle(self, self.ui, jsonFiles = {"JsonStyle/style.json"})
        
    def _configure_ui(self):
        """Configure UI components and initial settings."""
        self.app_name = "IVPN Auto Rotate"
        self.app_space_requirement = "3.19 - 5.10 GB"
        
        # UI component references
        self.stacked_widget = self.ui.stackedWidget
        self.progress_bar = self.ui.progressBar
        
        # Set labels and paths
        self._set_labels_and_paths()

    def _set_labels_and_paths(self):
        """Set dynamic labels and default installation paths."""
        self.ui.label_space_required.setText(
            f"At least {self.app_space_requirement} free disk space required."
        )
        self.ui.label_7.setText(f"Installer {self.app_name}")
        self.ui.label_8.setText(
            f"Installation of {self.app_name} completed.<br>"
            "Launch using the desktop shortcut."
        )
        self.ui.lineEdit_path_install.setPlainText(
            f"C:\\Program Files\\{self.app_name}"
        )
        self.ui.checkBoxRun.setText(
            f"Run {self.app_name} "
        )
        # Ensure installation directory exists
        os.makedirs(f"C:\\Program Files\\{self.app_name}", exist_ok=True)

    def _connect_signals(self):
        """Connect UI signals to handler methods."""
        self.ui.Tosearchfor.clicked.connect(self._show_path_dialog)
        self.ui.Button_next.clicked.connect(self._start_installation)
        self.ui.button_cancel.clicked.connect(self.close)
        self.ui.pushButton_finish_installer.clicked.connect(self._finalize_installation)

    def _show_path_dialog(self):
        """Display file dialog for installation path selection."""
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        
        if dialog.exec_():
            selected_path = dialog.selectedFiles()[0]
            self.ui.lineEdit_path_install.setPlainText(selected_path)
            self._show_notification("Installation path selected")

    def _start_installation(self):
        """Initialize and start the installation process."""
        self.stacked_widget.slideToNextWidget()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define installation paths
        paths = {
            'exe': os.path.join(script_dir, 'DataApp', 'IVPN Auto Rotate', 'IVPNAutoRotate.exe'),
            'software': os.path.join(script_dir, 'DataApp', 'IVPN Auto Rotate'),
            'install_path': self.ui.lineEdit_path_install.toPlainText(),
            'ivpn_client': os.path.join(script_dir, 'DataApp', 'IVPN Client'),
            'ivpn_dest': "C:\\Program Files\\IVPN Client",
            'python_package': os.path.join(script_dir, 'DataApp', 'Python.zip'),
            'python_dest': "C:\\Program Files\\IVPN Auto Rotate\\Dependenc"
        }
        
        self.installer = GenericInstaller(
            install_path=paths['install_path'],
            exe_path=paths['exe'],
            software_path=paths['software'],
            dependencies_path=paths['ivpn_client'],
            dependencies_destination=paths['ivpn_dest'],
            python_package_path=paths['python_package'],
            python_package_destination=paths['python_dest']
        )
        
        # Connect installer signals
        self.installer.progress.connect(self.progress_bar.setValue)
        self.installer.label_path_src_installing.connect(
            self.ui.label_path_src_installing.setText
        )
        self.installer.update_success.connect(self._show_notification)
        self.installer.finish.connect(self._complete_installation)
        
        self.installer.start()

    def _complete_installation(self):
        """Handle final installation steps."""
        self.stacked_widget.slideToNextWidget()
        self._show_notification("Installation completed!", duration=9000)

    def _finalize_installation(self):
        """Execute post-installation actions."""
        if self.ui.checkBoxRun.isChecked():
            os.chdir("C:/Program Files/IVPN Auto Rotate")
            os.system("IVPNAutoRotate.exe")
        
        self.close()

    def _show_notification(self, message, pos='top-right', duration=5000):
        """Display a custom notification."""
        QCustomModals.SuccessModal(
            title="Information", 
            parent=self.stacked_widget,
            position=pos,
            closeIcon=":/feather/icons/feather/window_close.png",
            modalIcon=":/material_design/icons/material_design/info.png",
            description=message,
            isClosable=False,
            duration=duration
        ).show()

def main():
    """Main entry point of the installer."""
    ensure_admin_privileges()
    app = QApplication(sys.argv)
    main_window = Main_installer()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()