# LuisOR
from src.utils import clear, pause

def clear_con():
    def decorate(function):
        def package(*data, **obj):
            clear()
            return function(*data, **obj)
        return package
    return decorate

def pause_con():
    def decorate(function):
        def package(*data, **obj):
            function(*data, **obj)
            pause()
        return package
    return decorate