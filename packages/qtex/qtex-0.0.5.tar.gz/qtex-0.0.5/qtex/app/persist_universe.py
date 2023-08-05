import os
import sys
import pandas as pd
# import qtc.utils.datetime_utils as dtu
import qtc.utils.db_utils as dbu
# import qtc.utils.misc_utils as mu
# import qtc.file.file_manager as fileman
# import qtc.ext.multiprocessing as mp
import qtex.env_config as ecfg
# import qtetl.tushare.data.dal
from qtc.ext.logging import set_logger
logger = set_logger()


DEFAULT_SEC_DATA_4_UNIV_DIR = os.getenv('CN_STOCK_DATA_ROOT',
                                        os.path.join(os.environ['HOME'], 'dw', 'cn_stock', 'sec_data_4_univ'))


def set_up_cli_options(parser=None):
    if parser is None:
        from optparse import OptionParser, IndentedHelpFormatter
        parser = OptionParser(formatter=IndentedHelpFormatter(width=200), epilog='\n')

    parser.add_option('-d', '--sec_data_4_univ_dir',
                      dest='sec_data_4_univ_dir', default=DEFAULT_SEC_DATA_4_UNIV_DIR,
                      help='Default: %default. ')
    parser.add_option('-v', '--connection_env',
                      dest='connection_env', default='RESEARCH',
                      help='Default: %default.')
    parser.add_option('-C', '--env_config_file',
                      dest='env_config_file', default=None,
                      help='Environment config file. Default: env config file contained in this package.')

    return parser

#
# def read_fc(dateid,
#             data_type,
#             cn_stock_data_root=DEFAULT_CN_STOCK_DATA_ROOT):
#     cn_stock_fm = fileman.FileManagerRegistry.get('CN-EQUITY-VENDOR.tushare',
#                                                   root=cn_stock_data_root)
#     data = cn_stock_fm._deserialize(
#         file_serializer=data_type,
#         dt=dateid
#     )
#
#     return data
#
#
# def download_vendor(dateid, data_type):
#     from qtetl.tushare.client import get_ts_client
#     import qtetl.tushare.data.dal.daily as dald
#     import qtetl.tushare.data.dal.financials as dalf
#     import qtetl.tushare.data.market_data as md
#
#     ts_client = get_ts_client()
#     datestr = str(dateid)
#     if data_type == 'SUSPENSION':
#         # data = ts_client.suspend_d(suspend_type='S', trade_date=str(dateid))
#         data = ts_client.suspend_d(trade_date=datestr)
#     elif data_type == 'RAW_MARKET_DATA':
#         data = md.download_daily_market_data(trade_date=datestr)
#     elif data_type == 'BASIC':
#         data = dald.request_daily_basic(trade_date=datestr)
#     elif data_type == 'MONEY_FLOW':
#         data = dald.request_daily_money_flow(trade_date=datestr)
#     elif data_type == 'INCOME':
#         data = dalf.request_income(start_date=datestr, end_date=datestr)
#     else:
#         raise Exception(f'data_type={data_type} not supported in '
#                         f'[RAW_MARKET_DATA|BASIC|SUSPENSION|MONEY_FLOW|INCOME] !')
#
#     data.sort_values('trade_date', inplace=True)
#     data['trade_date'] = data['trade_date'].astype(int)
#     return data
#
#
# def persist_fc(data, data_type,
#                dateid,
#                cn_stock_data_root=DEFAULT_CN_STOCK_DATA_ROOT):
#     if data is None or len(data)==0:
#         return
#
#     cn_stock_fm = fileman.FileManagerRegistry.get('CN-EQUITY-VENDOR.tushare',
#                                                   root=cn_stock_data_root)
#     file_path = cn_stock_fm.serialize(
#         data=data,
#         file_serializer=data_type,
#         dt=dateid
#     )
#
#     return file_path
#
#
# def persist_db(data, dateid, data_type):
#     if data is None or len(data)==0:
#         logger.warn(f'Skipping since data is None or len(data)==0 !')
#         return
#
#     db_code = 'CN-EQUITY-VENDOR'
#     schema = 'tushare'
#     conn = dbu.get_conn(db_code=db_code)
#     upsert_method = dbu.create_upsert_method(db_code=db_code, schema=schema,
#                                              extra_update_fields={'UpdateDateTime': "NOW()"})
#
#     if data_type == 'SUSPENSION':
#         pass
#     elif data_type == 'RAW_MARKET_DATA':
#         cols = ['trade_date','ts_code',
#                 'open','high','low','close','pct_chg',
#                 'vol','amount','adj_factor']
#         table_name = 'DailyMarketData'
#     elif data_type == 'BASIC':
#         cols = [
#             'trade_date', 'ts_code',
#             'total_share', 'float_share', 'free_share', 'total_mv', 'circ_mv',  # size
#             'turnover_rate', 'turnover_rate_f', 'volume_ratio',                 # technical
#             'pe', 'pe_ttm', 'pb', 'ps', 'ps_ttm', 'dv_ratio', 'dv_ttm'          # fundamental
#         ]
#         table_name = 'DailyBasic'
#     elif data_type == 'MONEY_FLOW':
#         pass
#     elif data_type == 'INCOME':
#         pass
#
#     cols = [col for col in cols if col in data.columns]
#     conn.execute(f'DELETE FROM "{schema}"."{table_name}" WHERE "trade_date"={dateid}')
#     num_rows = data[cols].to_sql(table_name,
#                                  con=conn, schema=schema,
#                                  if_exists='append', index=False,
#                                  method=upsert_method)
#     logger.info(f'{table_name} with shape {data.shape} on dateid={dateid} '
#                 f'persisted into "{db_code}"."{schema}"."{table_name}" .')
#
#     return None
#
#
# def run_tasks(dateid,
#               data_types='RAW_MARKET_DATA,BASIC,MONEY_FLOW,INCOME,SUSPENSION',
#               source='VENDOR',
#               destinations='DB',
#               cn_stock_data_root=DEFAULT_CN_STOCK_DATA_ROOT):
#     logger.info(f'===== Processing {dateid} =====')
#     data_types = set(mu.iterable_to_tuple(data_types, raw_type='str'))
#     destinations = set(mu.iterable_to_tuple(destinations, raw_type='str'))
#
#     for data_type in data_types:
#         logger.info(f'=== Processing data_type={data_type} ===')
#         if source=='FC':
#             data = read_fc(dateid=dateid,
#                            data_type=data_type,
#                            cn_stock_data_root=cn_stock_data_root)
#         elif source=='VENDOR':
#             data = download_vendor(dateid=dateid,
#                                    data_type=data_type)
#
#         for destination in destinations:
#             if destination=='FC':
#                 persist_fc(data=data, data_type=data_type,
#                            dateid=dateid,
#                            cn_stock_data_root=cn_stock_data_root)
#             elif destination=='DB':
#                 persist_db(data=data,
#                            dateid=dateid,
#                            data_type=data_type)
#
#
# ALL_TRADING_DATEIDS = None
# def get_all_trading_dateids():
#     global ALL_TRADING_DATEIDS
#     if ALL_TRADING_DATEIDS is None:
#         cn_stock_fm = fileman.FileManagerRegistry.get('CN-EQUITY-VENDOR.tushare',
#                                                       root=options.cn_stock_data_root)
#         dateid = dtu.curr_dateid(timezone='America/New_York')
#
#         while True:
#             trade_calendar = cn_stock_fm.deserialize(
#                 file_serializer='TRADE_CALENDAR',
#                 dts=dateid,
#                 log_error=True)
#             if trade_calendar is not None:
#                 break
#
#             dateid = dtu.prev_biz_dateid(dateid)
#
#         trade_calendar['cal_date'] = trade_calendar['cal_date'].astype('Int64')
#         trade_calendar['pretrade_date'] = trade_calendar['pretrade_date'].astype('Int64')
#         trade_calendar['is_open'] = trade_calendar['is_open'].astype(bool)
#
#         dateids = sorted(list(set(trade_calendar[trade_calendar['is_open']]['cal_date'])))
#         ALL_TRADING_DATEIDS = dateids
#
#     return ALL_TRADING_DATEIDS


if __name__ == '__main__':
    logger.info(' '.join(sys.argv))

    options, args = set_up_cli_options().parse_args()

    ecfg.get_env_config(env=options.connection_env,
                        env_config_file=options.env_config_file)

    for year in range(2016, 2024):
        sec_data_4_univ_file = os.path.join(options.sec_data_4_univ_dir,
                                            f'sec_data.{year}.pkl')
        sec_data = pd.read_pickle(sec_data_4_univ_file)

        logger.info(f'===== Processing {sec_data_4_univ_file} =====')

        for univ_id in [1]:
            if univ_id==1:
                universe = sec_data[(sec_data['price_no_fq'] > 4) &
                                    (sec_data['market_cap'] > 1e9) &
                                    (sec_data['TVMA20'] > 1e8) &
                                    (sec_data['circulating_market_cap'] >= 0.7 * sec_data['market_cap'])]

                universe['DateId'] = universe['trade_date'].dt.strftime('%Y%m%d').astype(int)
                universe['SecurityCode'] = universe['jq_code'].apply(lambda x: x.replace('.XSHE', '.SZ').replace('.XSHG', 'SH'))
                universe['UniverseId'] = univ_id

                db_code = 'TRADING'
                schema = 'universe'
                conn = dbu.get_conn(db_code=db_code)
                # upsert_method = dbu.create_upsert_method(db_code=db_code, schema=schema,
                #                                          extra_update_fields={'UpdateDateTime': "NOW()"})

                cols = ['DateId','UniverseId','SecurityCode']
                table_name = 'UniverseCN'
                num_rows = universe[cols].to_sql(table_name,
                                                 con=conn, schema=schema,
                                                 if_exists='append', index=False)
                                                 # method=upsert_method)
                logger.info(f'{table_name} with shape {universe[cols].shape} '
                            f'persisted into "{db_code}"."{schema}"."{table_name}" .')

