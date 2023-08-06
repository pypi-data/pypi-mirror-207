import sqlite3


def make_db(dbname='maindb.db'):
  """DEPRECIATED NOW ! , DO NOT USE , YOU CAN USE SET PROPERTY DIRECTLY! make db using this function , params: dbname is needed but not necessary , you can use it for creating custom named db"""
  try:
    conn = sqlite3.connect(dbname)
    c = conn.cursor()  
    return (True,'Created db successfully!')
  except Exception as e:
    return(False,f'ERROR : {e}')
  

def set_property_int(uniqueid='0',propertyname='OK',value=0,dbname='maindb.db'):
    """set a property of a user with a integer value """
    try:
      conn = sqlite3.connect(dbname)
      c = conn.cursor()
      c.execute(f'''CREATE TABLE IF NOT EXISTS {propertyname}
             (uniqueid TEXT PRIMARY KEY,othervalue INTEGER)''')
      c.execute(f'INSERT OR IGNORE INTO {propertyname} (uniqueid,othervalue) VALUES (?,?) ',(uniqueid,value))
      c.execute(f"UPDATE {propertyname} SET othervalue={int(value)} WHERE uniqueid={uniqueid}")
      conn.commit()
      return (True,'DB INFO EDITED SUCCESSFULLY!')
    except Exception as e:
      return(False,f'{e}')
    
def set_property_str(uniqueid='0',propertyname='OK',value="None",dbname='maindb.db'):
    """set a property of a user with a string value """
    try:
      conn = sqlite3.connect(dbname)
      c = conn.cursor()
      c.execute(f'''CREATE TABLE IF NOT EXISTS {propertyname}
             (uniqueid TEXT PRIMARY KEY,othervalue TEXT)''')
      c.execute(f'INSERT OR IGNORE INTO {propertyname} (uniqueid,othervalue) VALUES (?,?) ',(uniqueid,value))
      c.execute(f"UPDATE {propertyname} SET othervalue={str(value)} WHERE uniqueid={uniqueid}")
      conn.commit()
      return (True,'DB INFO EDITED SUCCESSFULLY!')
    except Exception as e:
      return(False,f'{e}')
    


def get_property(uniqueid='0',propertyname='OK',dbname='maindb.db'):
  """get any user property , returns str or int result"""
  try:
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {propertyname} WHERE uniqueid={uniqueid}")
    ok = c.fetchone()[1]
    return(True,f'{ok}')
  except Exception as e:
    return (False,f'{e}')


def deleteproperty(uniqueid='0',propertyname='OK',dbname='maindb.db'):
  """delete a user with uniqueid from property , used to ban or delete them"""
  try:
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"DELETE FROM {propertyname} WHERE uniqueid={uniqueid}")
    conn.commit()
    return(True,f'Deleted the info for {uniqueid} from {propertyname} successfully')
  except Exception as e:
    return(False,f'{e}')
  
def getinfo_ls(propertyname='OK',dbname='maindb.db',onlyvalue=False):
  """returns all the values from db from largest to smallest , can be int , str """
  try:
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {propertyname} ORDER BY othervalue DESC")
    ok = c.fetchall()
    if onlyvalue == False:
      return(True,ok)
    else:
      return ok
  except Exception as e:
    return(False,f'{e}')
  
def getinfo_sl(propertyname='OK',dbname='maindb.db',onlyvalue=False):
  """returns all the values from db from smallest to largest , can be int , str """
  try:
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {propertyname} ORDER BY othervalue ASC")
    ok = c.fetchall()
    if onlyvalue == False:
      return(True,ok)
    else:
      return ok
  except Exception as e:
    return(False,f'{e}')
  














  