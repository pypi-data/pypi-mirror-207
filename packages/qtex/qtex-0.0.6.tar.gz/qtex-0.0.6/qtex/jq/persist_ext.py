import pandas as pd
import jqfactor as jqf
import qtc.utils.cipher_utils as cu
import qtc.utils.misc_utils as mu
import qtc.utils.datetime_utils as dtu

import qtex.jq.utils
import qtex.jq.utils as jqu
import logging
logger = logging.getLogger()


# DB_CONFIG = {
#     'HOST': '124.222.142.29',
#     'PORT': 7423,
#     'USER': 's_heimdal_etl',
#     'PASSWORD': '390f1c1c05140241445767',
#     'DATABASE': 'CN-EQUITY-VENDOR'
# }


def persist_target_positions(dateid, target_positions,
                             **kwargs):
    if target_positions is None or len(target_positions)==0:
        return None

    cols =['AccountId', 'StrategyId', 'DateId', 'SecurityCode', 'SideId',
           'Signal', 'Quantity', 'MV', 'Weight']
    cols = [col for col in cols if col in target_positions.columns]
    data = target_positions[cols]

    user_d, password_d, database_d = \
        qtex.jq.utils.DATA_TYPE_CONFIG.get('TARGET_POSITION',
                                           ('s_heimdal_trading', '390f1c1c05140241445767', 'TRADING'))
    if 'user' not in kwargs:
        user = user_d
    if 'password' not in kwargs:
        password = password_d
    if 'database' not in kwargs:
        database = database_d

    conn = jqu.get_conn(user=user, password=password, database=database)
    schema = 'signal'
    table_name = 'TargetPosition'
    # upsert_method = dbu.create_upsert_method(db_code=database, schema=schema,
    #                                          extra_update_fields={'UpdateDateTime': "NOW()"})

    num_rows = data.to_sql(table_name,
                           con=conn, schema=schema,
                           if_exists='append', index=False)

    logger.info(f'{table_name} with shape {data.shape} on dateid={dateid} '
                f'persisted into "{database}"."{schema}"."{table_name}" .')

    return data