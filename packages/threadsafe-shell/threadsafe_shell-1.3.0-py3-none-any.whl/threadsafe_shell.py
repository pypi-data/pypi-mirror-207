import sys
import readline # adds up/down arrow support in shell
import threading
from queue import deque
import io

class Shell:
    class colors:
        GREY   = "\033[30m"
        GRAY   = "\033[30m"
        RED    = "\033[31m"
        GREEN  = "\033[32m"
        YELLOW = "\033[33m"
        BLUE   = "\033[34m"
        PURPLE = "\033[35m"
        CYAN   = "\033[36m"
        WHITE  = "\033[37m"
        RESET  = "\033[0m"
    class highlights:
        BLACK  = "\033[40m"
        RED    = "\033[41m"
        GREEN  = "\033[42m"
        YELLOW = "\033[43m"
        BLUE   = "\033[44m"
        PURPLE = "\033[45m"
        CYAN   = "\033[46m"
        WHITE  = "\033[47m"
        RESET  = "\033[0m"
    
    
    def __init__(self, log_file:io.IOBase=None, error_file:io.IOBase=None, debug_level=3):
        # stream and file io
        self.__log_file = log_file
        self.__write_to_log_file = log_file is not None
        self.__error_file = error_file
        self.__write_to_error_file = error_file is not None
        # debug info
        self.DEBUG_LEVEL = debug_level
        self.__is_debug_active = True
        # threading
        self.__queue = deque()
        self.__get_write_loop_thread().start()
        self.__queue_lock = threading.Lock()
        self.__file_lock = threading.Lock()
        self.__input_lock = threading.Lock()
    
    def set_log_output_file(self, file: io.IOBase):
        self.__log_file = file
        self.__write_to_log_file = file is not None
    
    def set_error_output_file(self, file: io.IOBase):
        self.__error_file = file
        self.__write_to_error_file = file is not None        

    
    def __handle_to_file(self, data:dict={}) -> None:
        if "text" not in data: raise KeyError("Key 'text' not found")
        if "is_error" not in data: raise KeyError("Key 'is_error' not found")
        with self.__file_lock:
            # print to console
            print(data["text"], end='', flush=True, file=sys.stderr if data["is_error"] else sys.stdout)
            # print to file
            if self.__write_to_log_file:
                print(data["text"], end='', flush=True, file=self.__log_file)
            if self.__write_to_error_file and data["is_error"]:
                print(data["text"], end='', flush=True, file=self.__error_file)


    def __add_to_queue(self, header:str, *args, is_error:bool=False, console_only:bool=False, file_only:bool=False, end='\n', sep=' ') -> None:
        if console_only and file_only: raise AttributeError("console_only and file_only cannot both be True")
        header += "\033[0m"
        end += "\033[0m"
        out = header + sep.join(str(arg) for arg in args) + end
        out.replace('\n', '\n'+header)
        with self.__queue_lock:
            self.__queue.append({ "text": out, "is_error": is_error })
     
    def __write_loop(self):
        while True:
            if len(self.__queue):
                with self.__queue_lock: val = self.__queue.popleft()
                self.__handle_to_file(val)
    
    def __get_write_loop_thread(self):
        try:
            return self.thread
        except AttributeError:
            self.thread = threading.Thread(target=self.__write_loop, name="ShellWriteLoop-Daemon", daemon=True)
            return self.thread
    
    
    @staticmethod
    def highlight(obj: object, color:str=colors.PURPLE) -> str:
        return color + str(obj) + "\033[0m"
    
    def set_debug_level(self, level:int):
        self.DEBUG_LEVEL = level
    
    def set_debug_active(self, is_debug_active:bool):
        self.__is_debug_active = is_debug_active

    def debug(self, *args, level:int=3, **kwargs):
        if level >= self.DEBUG_LEVEL and self.__is_debug_active:
            self.__add_to_queue("\033[30mDEBUG  ", *args, **kwargs)
    
    def log(self, *args, **kwargs):      self.__add_to_queue("\033[34mLOG    ", *args, **kwargs)
    def success(self, *args, **kwargs):  self.__add_to_queue("\033[32mPASS   ", *args, **kwargs)
    def warn(self, *args, **kwargs):     self.__add_to_queue("\033[33mWARN   ", *args, is_error=True, **kwargs)
    def error(self, *args, **kwargs):    self.__add_to_queue("\033[31mERROR  ", *args, is_error=True, **kwargs)


    def ask(self, string: str, default:str=None) -> str:
        """
        Asks the user a question and returns the answer.
        If `default` is `None`, will ask again until an answer is given. Otherwise, when no answer is given, returns `default`.
        """
        string += "\033[35mPROMPT "+string+"\033[0m "
        with self.__input_lock:
            self.__add_to_queue("\033[35mPROMPT ", string, end='', console_only=True)
            val = input().strip()
            while default is None and len(val) == 0:
                self.__add_to_queue("\033[35mPROMPT ", string, end='', console_only=True)
                val = input().strip()
        if not (self.__log_file is None): self.__add_to_queue("\033[35mPROMPT ", string, val, file_only=True, sep='')
        return default if val=="" else val


    def prompt(self, string: str, default: bool = None) -> bool:
        """
        Prompts a yes-or-no question and returns the boolean answer.
        kwarg `default` controls `'Y|n'` (`True`) or `'y|N'` (`False`), or if to ask infinitely (`None`).
        """
        if default is None:
            val = ""
            string += " (y|n)  "
            with self.__input_lock:
                while len(val)==0 or not (val[0] in "ynYN"):
                    self.__add_to_queue("\033[35mPROMPT ", string, end='', console_only=True)
                    val = input().strip()
            if not (self.__log_file is None): self.__add_to_queue("\033[35mPROMPT ", string, val, file_only=True, sep='')
            return val[0].lower() == "y"
        else:
            string += f" ({'Y|n' if default else 'y|N'})  "
            with self.__input_lock:
                self.__add_to_queue("\033[35mPROMPT ", string, end='', console_only=True)
                val = input().strip()
            if not (self.__log_file is None): self.__add_to_queue("\033[35mPROMPT ", string, val, file_only=True, sep='')
            if len(val)==0 or val[0] not in "ynYN":
                val = "y" if default else "n"
            if default: return val[0].lower() != "n"
            else:       return val[0].lower() == "y"


def get_shell() -> Shell:
    """ Gets the current active global shell object. """
    try:
        return Shell.shell
    except AttributeError:
        Shell.shell = Shell()
        return Shell.shell
