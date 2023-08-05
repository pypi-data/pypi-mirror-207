import os
import pandas as pd
import qtc.utils.db_utils as dbu
import qtc.utils.cipher_utils as cu


def get_conn(**db_config):
    db_type = db_config.get('db_type', 'POSTGRES')
    host = db_config.get('host', os.getenv('DB_HOST', None))
    port = db_config.get('port', os.getenv('DB_PORT', None))
    user = db_config.get('user', os.getenv('DB_USER', None))
    password = db_config.get('password', os.getenv('DB_PASSWORD', None))
    database = db_config.get('database', os.getenv('DB_DATABASE', None))

    conn = dbu._get_engine(
        db_type=db_type,
        host=host,
        port=port,
        user=user,
        password=cu.from_salted(secret_str=password),
        database=database
    )

    return conn


def get_conn_data_type(data_type, **db_config):
    import qtex.jq.etl.factor_info as etlfi
    import qtex.jq.etl.factor_values as etlfv
    import qtex.jq.sync.position as syncp

    DATA_TYPE_DB_CONFIG_MAP = {
        'FACTOR_GROUP': etlfi.DATA_TYPE_DB_CONFIG,
        'FACTOR_INFO': etlfi.DATA_TYPE_DB_CONFIG,
        'CNE5': etlfv.DATA_TYPE_DB_CONFIG,
        'FACTOR_VALUE': etlfv.DATA_TYPE_DB_CONFIG,
        'TARGET_POSITION': syncp.DATA_TYPE_DB_CONFIG
    }

    data_type_db_config = DATA_TYPE_DB_CONFIG_MAP.get(data_type, dict())

    db_type_d, host_d, port_d, user_d, password_d, database_d = \
        data_type_db_config.get(data_type,
                                ('POSTGRES', None, None, None, None, None))

    db_type = db_config.get('db_type', db_type_d)
    host = db_config.get('host', host_d)
    port = db_config.get('port', port_d)
    user = db_config.get('user', user_d)
    password = db_config.get('password', password_d)
    database = db_config.get('database', database_d)

    conn = get_conn(
        db_type=db_type,
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    return conn, database


def load_factor_scores(jq_codes, factors,
                       end_date, start_date=None, count=None,
                       transpose=False):
    import jqfactor as jqf
    scores = jqf.get_factor_values(
        securities=jq_codes,
        factors=factors,
        start_date=start_date, end_date=end_date, count=count
    )

    scores = pd.concat(scores)
    scores.index.names = ['factor_code', 'trade_date']

    if count==1:
        if transpose:
    #         scores = scores.droplevel(level='Date').T
            scores.index = scores.index.droplevel(level='trade_date')
            scores = scores.T
    else:
        if transpose:
            scores = scores.T.stack()

    return scores


def produce_factor_id(source_id, factor_code):
    return int(int(str(source_id).ljust(3, '0')) * 1e6 + hash(factor_code) % (1e6))
