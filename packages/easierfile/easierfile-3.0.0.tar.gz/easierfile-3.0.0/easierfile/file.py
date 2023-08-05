import sys

# This module's built-in functions about file lock.
if sys.platform.startswith("win"):  # For Windows.
    import msvcrt

    def _lock_file(file):
        msvcrt.locking(file.fileno(), msvcrt.LK_RLCK, 0)

    def _unlock_file(file):
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 0)

else:  # For Linux, Unix, MacOS.
    import fcntl

    def _lock_file(file):
        fcntl.flock(file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

    def _unlock_file(file):
        fcntl.flock(file.fileno(), fcntl.LOCK_UN)


import os
from dynoptimdict import DynamicDict
import chardet


class File:
    def __init__(self, file_path, is_auto_create=True, is_occupy=True):
        # Get static file information.
        self.__m_static_info = {}
        self.__m_static_info["path"] = os.path.abspath(file_path)
        self.__m_static_info["dir_path"] = os.path.dirname(self.__m_static_info["path"])
        self.__m_static_info["full_name"] = os.path.basename(self.__m_static_info["path"])
        self.__m_static_info["name"], self.__m_static_info["ext"] = os.path.splitext(self.__m_static_info["full_name"])
        self.__m_static_info["ext"] = self.__m_static_info["ext"].split(".")[-1]  # Format ext of info to remove str<.>.

        self.__m_is_occupy = is_occupy
        self.__m_is_lock = False  # Initialize file lock state.

        if is_auto_create:
            try:
                self.create()
            except FileExistsError:  # Indicates that the file exists and no further exception handling is required.
                pass

        if is_occupy and (not self.__m_is_lock):
            self.__lock(True)

    def __del__(self):
        # Release file lock.
        if self.__m_is_lock:
            try:
                self.__lock(False)
            except FileNotFoundError:  # Indicates that the file lock does not exist and no further exception handling is required.
                pass

    def __lock(self, is_lock):
        if self.state["exist"]:
            if is_lock:
                self.__m_file = open(self.__m_static_info["path"])
                _lock_file(self.__m_file)
                self.__m_is_lock = is_lock
            else:
                _unlock_file(self.__m_file)
                self.__m_file.close()
                self.__m_is_lock = is_lock
        else:
            if is_lock:
                raise FileNotFoundError("File was about to be occupied, but not found: " + self.__m_static_info["path"])
            else:
                raise FileNotFoundError("File was about to be unoccupied, but not found: " + self.__m_static_info["path"])

    def create(self):
        if not self.state["exist"]:
            if not os.path.exists(self.__m_static_info["dir_path"]):  # Create the file directory if it doesn't exist, so that code<open()> doesn't throw the exception.
                os.mkdir(self.__m_static_info["dir_path"])
            try:
                file_temp = open(self.__m_static_info["path"], "x")
            except FileExistsError:  # Avoid exception caused by creating corresponding file in other ways during program execution intervals.
                pass
            else:
                file_temp.close()
            if self.__m_is_occupy:
                self.__lock(True)
        else:
            raise FileExistsError("File exists: " + self.__m_static_info["path"])

    def delete(self):
        if self.__m_is_lock:
            self.__lock(False)
        if self.state["exist"]:
            os.remove(self.__m_static_info["path"])

    def rewrite(self,content):
        if self.state["exist"]:
            """
            Automatically obtain the most suitable encoding format for the input content.
            
            :samp: chardet.detect(content.encode())["encoding"]
            """
            file_temp = open(self.__m_static_info["path"], "w", encoding=chardet.detect(content.encode())["encoding"])
            file_temp.write(content)
            file_temp.close()
        else:
            raise FileNotFoundError("File not found: " + self.__m_static_info["path"])

    def append(self,content):
        if self.state["exist"]:
            file_temp = open(self.__m_static_info["path"], "a", encoding=chardet.detect(content.encode())["encoding"])
            file_temp.write(content)
            file_temp.close()
        else:
            raise FileNotFoundError("File not found: " + self.__m_static_info["path"])

    @property
    def content(self):
        if self.state["exist"]:
            """
            Automatically obtain the most suitable encoding format for the output content.
            
            :samp: self.info["encoding"]
            
            In fact, it gets the encoding format of the read file. 
            """
            file_temp = open(self.__m_static_info["path"], "r", encoding=self.info["encoding"])
            content = file_temp.read()
            file_temp.close()
            return content
        else:
            raise FileNotFoundError("File not found: " + self.__m_static_info["path"])

    @property
    def info(self):
        # Get dynamic file information.
        def get_info_encoding():
            file_temp = open(self.__m_static_info["path"],'rb')
            encoding = chardet.detect(file_temp.read())["encoding"]
            file_temp.close()
            return encoding

        info = DynamicDict()

        # Store static file information directly.
        info["path"] = self.__m_static_info["path"]
        info["dir_path"] = self.__m_static_info["dir_path"]
        info["full_name"] = self.__m_static_info["full_name"]
        info["name"] = self.__m_static_info["name"]
        info["ext"] = self.__m_static_info["ext"]

        # Store the acquisition way of dynamic file information.
        info["encoding"] = get_info_encoding

        return info

    @property
    def state(self):
        def get_status_file_lock():
            return self.__m_is_lock

        def get_status_exist():
            return os.path.isfile(self.__m_static_info["path"])

        status = DynamicDict()
        # Pass function pointers for obtaining dynamic data into object:Dict<status>.
        status["file_lock"] = get_status_file_lock
        status["exist"] = get_status_exist
        return status
