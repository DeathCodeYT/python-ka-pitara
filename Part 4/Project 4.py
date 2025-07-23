# Custom Confirgration System


class ConfigField:
    def __init__(self,name,default_value=None,description=""):
        self.name = name
        self.__value = default_value
        self.description = description

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,val):
        self.__value = val

    def validate(self,val):
        # Validation Login, subclass will override
        return True

    def __repr__(self):
        return f"ConfigField(name='{self.name}' value='{self.__value}', des='{self.description}')"
    

class StringField(ConfigField):
    def __init__(self, name, default_value="", description=""):
        super().__init__(name, default_value, description)
    
    def validate(self, val):
        return isinstance(val,str)
    
class IntegerField(ConfigField):
    def __init__(self, name, default_value=0, description=""):
        super().__init__(name, default_value, description)
    
    def validate(self, val):
        return isinstance(val,int)
    

class ConfigMeta(type):
    def __new__(cls,name,bases,attrs):
        _confgis = {}
        for attr_name,obj in list(attrs.items()):
            if isinstance(obj,ConfigField):
                _confgis[attr_name] = obj 
                del attrs[attr_name]
        attrs['_configs'] = _confgis
        return super().__new__(cls,name,bases,attrs)


class BaseConfig(metaclass=ConfigMeta):
    def __init__(self):
        self._config_fields = {name:field for name,field in self._configs.items()}
    
    def __getattr__(self,name):
        if name in self._config_fields:
            return self._config_fields[name].value
        raise AttributeError(f"'{self.__class__.__name__}' Object has no attribute {name}")
    
    def __setattr__(self,name,value):
        if '_config_fields' in self.__dict__ and name in self._config_fields:
            field = self._config_fields[name]
            if field.validate(value):
                field.value = value
            else:
                print(f"Error: Invalid value '{value}' for config '{name}'. Type mismatch.")
        else:
            super().__setattr__(name,value)

    def __call__(self):
        print(f"--- Calling {self.__class__.__name__} Configuration ---")
        for _,field in self._config_fields.items():
            print(f"- {field.name} ({field.description}): {field.value}")
        print("-"*40)

    @classmethod
    def load_from_dict(cls,config_dict):
        instance = cls()
        for name,field in config_dict.items():
            if name in instance._config_fields:
                instance._config_fields[name].value = field
            else:
                print(f"Warning: Unkown Config key '{name}' encountered.")
        return instance

    @staticmethod
    def get_config_help():
        print("This is a dynamic Configuration system. Define settings as Config Filed instances.")

class AppSettings(BaseConfig):
    api_key = StringField("API Key","DEFAULT_API_KEY", "API key for external services")
    max_retries = IntegerField("Max Retries",3,"Maximum number of retries for network operations")
    debug_mode = ConfigField("Debug Mode",False,"Enable or disable debug logging")
    coin = 77

# AppSettings.get_config_help()

my_app_config = AppSettings()


# print(f"Initial API Key: {my_app_config.api_key}")
# print(f"Initial Max Retries: {my_app_config.max_retries}")


# my_app_config.api_key = "MY_NEW_API_KEY"
# my_app_config.max_retries = 10
# my_app_config.debug_mode = True
# print(f"After Update API Key: {my_app_config.api_key}")
config_values = {
    "api_key" : "NEW_API_KEY_klUHDFLKSJDHVLWNSUJ7934bJ",
    "max_retries": 9,
    "debug_mode":True,
    "unknown_key":"THIS_WILL_BE_IGNORED"
}
loaded_config = AppSettings.load_from_dict(config_values)
loaded_config()
print(loaded_config.coin)
loaded_config.coin = 6
print(loaded_config.coin)


