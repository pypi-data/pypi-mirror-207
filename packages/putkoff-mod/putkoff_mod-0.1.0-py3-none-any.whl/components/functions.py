import os
import subprocess
import sys
import requests
import json
import time
from datetime import datetime
import sys
from pathlib import Path

from askPassHelper import *
def getHome():
    if change_glob('slash','\\') not in change_glob('home',os.getcwd()):
        change_glob('slash','/')
def get_abs_path_of_this():
    return Path( __file__ ).absolute()
def get_abs_name_of_this():
    return Path( __name__ ).absolute()
def get_here():
    return os.getcwd()
def get_saved_variables(module,file_name,make=''):
    return dict_check_conversion(exists_make(mk_dir_add_file(['/home/hmmm/Documents/python_scripts/shared/crypto/web3','saved_variables',module],file_name),make))
def save_variables(data,module,file_name):
    dump_it_save(data,mk_dir_add_file(['/home/hmmm/Documents/python_scripts/shared/crypto/web3','saved_variables',module],file_name))
def mk_dir_add_file(dirs_ls,file_name):
    return create_path(mkdirs(create_paths(dirs_ls)),file_name)
def change_glob(x,y):
    globals()[x] = y
    return y
def get_values_js(js):
    return list(js.values())
def reader(filepath):
    with open(filepath, 'r') as f:
        return f.read()
def pen(data, filepath):
    with open(filepath, 'w') as f:
        f.write(data)
    return data
def make_list_lower(ls):
    for k in range(0,len(ls)):
        if ls[k] not in [None]:
            ls[k] = ls[k].lower()
    return ls
def get_time_stamp():
    return datetime.now().timestamp()
def get_milisecond_time_stamp():
    return datetime.now().timestamp()*1000
def get_day(now=get_time_stamp()):
    return now.strftime("%A")
def get_time(now=get_time_stamp()):
    return str(datetime.now())[10:]
def get_date(now=get_time_stamp()):
    return str(datetime.now())[:10]
def save_last_time(now = get_time_stamp()):
    return pen(str(now),'last.txt')
def get_day_seconds():
    return float(24*60*60)
def get_week_seconds():
    return float(7*24*60*60)
def get_hour_seconds():
    return float(60*60)
def get_minute_seconds():
    return float(60)
def get_second():
    return float(1)
def get_24_hr_start(now=get_time_stamp()):
    return int(now) - int(get_day_seconds())
def create_paths(ls):
    y = create_path(ls[0],ls[1])
    for k in range(2,len(ls)):
        y = create_path(y,ls[k])
    return y
def rename_file(old_filename,new_filename):
    os.rename(old_filename, new_filename)
def create_path(x,y):
    return os.path.join(x,y)
def combineList(ls,lsN):
    for k in range(0,len(lsN)):
        ls.append(lsN[k])
    return ls
def createFolds(ls):
    for k in range(0,len(ls)):
        mkdirs(ls[k])
def mkdirs(path):
    os.makedirs(path,exist_ok=True)  
    return path
def add_js(js,jsN):
    keys = getKeys(jsN)
    for k in range(0,len(keys)):
        js[keys[k]] = jsN[keys[k]]
    return js
def is_dict(obj):
    if isinstance(obj, dict):
        return True
    return False
def is_str_convertible_dict(obj):
    if isinstance(obj, str):
        try:
            json.loads(obj)
            return True
        except json.JSONDecodeError:
            return False
    return False
def is_dict_or_convertable(obj):
    if is_dict(obj):
        return True
    if is_str_convertible_dict(obj):
        return True
    return False
def dict_check_conversion(obj):
    if is_dict_or_convertable(obj):
        if is_dict(obj):
            return obj
        return json.loads(obj)
    return obj
def file_exists(file_path):
    return os.path.exists(file_path)
def dir_exists(path):
    return os.path.isdir(path)
def load_it(path):
    return dict_check_conversion(exists_make(path,{}))
def dump_it(js):
    return json.dumps(js)
def dump_it_save(js,file_path):
    return pen(dump_it(js),file_path)
def exists_make(filepath, exception=''):
    if not file_exists(filepath):
        if is_dict_or_convertable(exception):
            with open(filepath, 'w') as f:
                json.dump(exception, f)
        else:
            pen(str(exception), filepath)
    return dict_check_conversion(reader(filepath))
def crPa(x,y):
    return os.path.join(str(x),str(y))
def isFile(x):
    return os.path.isfile(crPa(home,x))
def exists(x):
    try:
        x = reader(x)
        return True
    except:
        return False
def getKeys(obj):
    obj = dict_check_conversion(obj)
    if not obj:
        return []
    return list(obj.keys())
def getVals(js):
  lsN = []
  try:
    for key in js.values():
      lsN.append(key)
    return lsN
  except:
    return lsN
def pen(x,p):
  with open(p, 'w',encoding='UTF-8') as f:
    f.write(str(x))
    return p
def reader(x):
  with open(x, 'r',encoding='UTF-8') as f:
    return f.read()
def isLs(ls):
  if type(ls) is list:
    return True
  return False
def mkLs(ls):
  if isLs(ls) == False:
    ls = [ls]
  return ls
def exists(x):
    if isFile(x):
        return True
    return False
def reader(filename, contents=''):
    try:
        # Try to read the file
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        # If the file doesn't exist, create it with the specified contents
        with open(filename, 'w') as f:
            f.write(contents)
    return contents
def existJsRead(x,y):
    if exists(y) == False:
        pen(x,y)
    return jsIt(reader(y))
def jsRead(x):
    return jsIt(reader(x))
def existRead(x,y):
    if exists(y) == False:
        pen(str(x),y)
    return reader(y)
def existJsRead(x,y):
    if exists(str(y)) == False:
        pen(str(x),str(y))
    return jsRead(str(y))
def get_multiply_remainder(x,y):
    if x<=y:
        return 0,x
    mul = int(float(x)/float(y))
    return mul,int(x)-int(mul*y)
def alpha():
    return 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
def get_alpha(k):
    alph = alpha()
    mul,rem = get_multiply_remainder(k,len(alph))
    if mul-1 >-1:
        return str(alph[mul])+str(alph[rem])
    return str(alph[rem])
def quoteIt(st,ls):
    lsQ = ["'",'"']
    for i in range(0,len(ls)):
        for k in range(0,2):
            if lsQ[k]+ls[i] in st:
                st = st.replace(lsQ[k]+ls[i],ls[i])
            if ls[i]+lsQ[k] in st:
                st = st.replace(ls[i]+lsQ[k],ls[i])
        st = st.replace(ls[i],'"'+str(ls[i])+'"')
    return st
def jsIt(x):
    return json.loads(quoteIt(str(x),['False','None','True']).replace("'",'"'))
def find_it_alph(x,k):
    i = 0
    while str(x[i]) != str(k):
        i = i + 1
    return i
def eatInner(x,ls):
    for i in range(0,len(x)):
        if x[0] not in ls:
            return x
        x = x[1:]
    return ''
def eatOuter(x,ls):
    for i in range(0,len(x)):
        if x[-1] not in ls:
            return x
        x = x[:-1]
    return ''
def eatAll(x,ls):
    return eatOuter(eatInner(x,ls),ls)
def get_types_list():
    return '''object,str,int,float,bool,list,tuple,set,dict,frozenset,bytearray,bytes,memoryview,range,enumerate,zip,filter,map,property,slice,super,type,Exception,attr'''.split(',')
def safe_split(obj,ls):
    for k in range(0,len(ls)):
        if is_list(ls[k]):
            if ls[k][0] in obj or ls[k][1] == 0:
                obj = obj.split(ls[k][0])[ls[k][1]]
        else:
            obj = obj.split(ls[0])[ls[1]]
            return obj
    return obj
def clean_spaces(obj):
    if len(obj) ==0:
        return obj
    while obj[0] in [' ','\t']:
        obj = obj[1:]
    return obj
def get_num_list():
    return '1,2,3,4,5,6,7,8,9'.split(',')
def is_number(obj):
    if is_int(obj):
        return True
    if is_float(obj):
        return True
    obj = make_str(obj)
    num_ls = get_num_list()
    for k in range(0,len(obj)):
        if obj[k] not in num_ls:
            return False
    return True
def get_type(obj):
    if is_number(obj):
        obj = int(obj)
    if is_float(obj):
        return float(obj)
    elif obj == 'None':
        obj =  None
    elif is_str(obj):
        obj =  str(obj)
    return obj
def is_object(obj):
    if type(obj) is object:
        return True
    else:
        return False
def is_str(obj):
    if type(obj) is str:
        return True
    else:
        return False
def is_int(obj):
    if type(obj) is int:
        return True
    else:
        return False
def is_float(obj):
    if type(obj) is float:
        return True
    else:
        return False
def is_bool(obj):
    if type(obj) is bool:
        return True
    else:
        return False
def is_list(obj):
    if type(obj) is list:
        return True
    else:
        return False
def is_tuple(obj):
    if type(obj) is tuple:
        return True
    else:
        return False
def is_set(obj):
    if type(obj) is set:
        return True
    else:
        return False
def is_dict(obj):
    if type(obj) is dict:
        return True
    else:
        return False
def is_frozenset(obj):
    if type(obj) is frozenset:
        return True
    else:
        return False
def is_bytearray(obj):
    if type(obj) is bytearray:
        return True
    else:
        return False
def is_bytes(obj):
    if type(obj) is bytes:
        return True
    else:
        return False
def is_memoryview(obj):
    if type(obj) is memoryview:
        return True
    else:
        return False
def is_range(obj):
    if type(obj) is range:
        return True
    else:
        return False
def is_enumerate(obj):
    if type(obj) is enumerate:
        return True
    else:
        return False
def is_zip(obj):
    if type(obj) is zip:
        return True
    else:
        return False
def is_filter(obj):
    if type(obj) is filter:
        return True
    else:
        return False
def is_map(obj):
    if type(obj) is map:
        return True
    else:
        return False
def is_property(obj):
    if type(obj) is property:
        return True
    else:
        return False
def is_slice(obj):
    if type(obj) is slice:
        return True
    else:
        return False
def is_super(obj):
    if type(obj) is super:
        return True
    else:
        return False
def is_type(obj):
    if type(obj) is type:
        return True
    else:
        return False
def is_Exception(obj):
    if type(obj) is Exception:
        return True
    else:
        return False
def is_none(obj):
    if type(obj) is None:
        return True
    else:
        return False
def retNums():
  return str('0,1,2,3,4,5,6,7,8,9').split(',')
def isNum(x):
  if x == '':
      return False
  if isInt(x):
    return True
  if isFloat(x):
    return True
  x,nums = str(x),retNums()
  for i in range(0,len(x)):
    if x[i] not in nums:
      return False
  return True
def mkFloat(x):
  if isFloat(x):
    return x
  if isInt(x):
    return float(str(x))
  if isNum(x):
    return float(str(x))
  z = ''
  for i in range(0,len(x)):
    if isNum(x[i]):
      z = z + str(x[i])
  if len(z) >0:
    return float(str(z))
  return float(str(1))
def mkBool(x):
    if isBool(x):
        return x
    boolJS = {'0':'True','1':'False','true':'True','false':'False'}
    if str(x) in boolJS:
        return bool(str(boolJs[str(x)]))
    return None
def make_str(x):
    if is_str(x):
        return x
    return str(x)
def getObjObj(obj,x):
    if obj in ['str','file','image','mask','input','prompt']:
        return str(x)
    if obj == 'bool':
        return bool(x)
    if obj == 'float':
        return float(x)
    if obj == 'map':
        return map(x)
    if obj == 'int':
        return int(x)
    return x
def create_path_if_not_exist(path):
    # Remove trailing slash if present
    if path[-1] == os.sep:
        path = path[:-1]
    # Split the path into its components
    path_parts = os.path.normpath(path).split(os.sep)
    # Check if the last component has a file extension
    is_file = "." in path_parts[-1]
    # Remove the last component if it's a file
    if is_file:
        path_parts.pop()
    # Create the directories if they don't exist
    current_path = ""
    for part in path_parts:
        current_path = os.path.join(current_path, part)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    # Return the type of the path
    return "file" if is_file else "directory"
def display_values(json_obj, indent=0):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if isinstance(value, (dict, list)):
                print('  ' * indent + f"{key}:")
                display_values(value, indent + 1)
            else:
                print('  ' * indent + f"{key}: {value}")
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            if isinstance(item, (dict, list)):
                print('  ' * indent + f"[{index}]:")
                display_values(item, indent + 1)
            else:
                print('  ' * indent + f"[{index}]: {item}")
def list_dir(path):
    return os.listdir(path)
