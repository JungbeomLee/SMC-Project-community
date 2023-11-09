from ..utils.env_val import database_pwd
import pymysql

# connect mysql DataBase
register_db = pymysql.connect(
    host=   "localhost",
    user=   "root", 
    passwd= database_pwd, 
    db=     "smc_project_community_db", 
    charset="utf8"
)