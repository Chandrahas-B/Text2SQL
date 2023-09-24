import logging
import colorlog

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(log_color)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)


sql_keywords = {
    "SELECT", "FROM", "WHERE", "AND", "OR", "NOT", "ORDER", "GROUP", "BY",
    "HAVING", "AS", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL", "JOIN",
    "CROSS", "UNION", "INSERT", "INTO", "VALUES", "UPDATE", "SET", "DELETE",
    "CREATE", "TABLE", "ALTER", "DROP", "INDEX", "PRIMARY", "KEY", "FOREIGN",
    "UNIQUE", "CHECK", "DEFAULT", "NULL", "AUTO_INCREMENT", "TOP", "LIMIT",
    "OFFSET", "LIKE", "BETWEEN", "IN", "IS", "EXISTS", "COUNT", "SUM", "AVG",
    "MAX", "MIN", "DISTINCT", "CASE", "WHEN", "THEN", "ELSE", "END", "ALL",
    "ANY", "EXTRACT", "DATE", "TIME", "YEAR", "MONTH", "DAY", "HOUR", "MINUTE",
    "SECOND", "ASC", "DESC"
}

def postprocess(query: str) -> str:
    ans = []
    print(query.split())
    for q in query.split():
        if q.upper() in sql_keywords:
            q = q.upper()
                
        ans.append(q)
            
    ans = ' '.join(ans)
    
    return ans if ans[-1] == ';' else ans + ';' 