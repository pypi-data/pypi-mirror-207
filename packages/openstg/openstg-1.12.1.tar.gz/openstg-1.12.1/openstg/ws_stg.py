# -*- encoding: utf-8 -*-
from spyne import Application, ServiceBase, Mandatory, Boolean, UnsignedInt, UnsignedInteger, Int, Integer, Iterable, ServiceBase, String, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from werkzeug.middleware.dispatcher import DispatcherMiddleware

import logging
from datetime import datetime
from os import path
import re
from flask import Flask
from osconf import config_from_environment


logger = logging.getLogger('ws_stg')


DEFAULT_SAVE_PATH = '/tmp'


dc_status = {
        '0': "SUCCESS: The request with ID {} for the concentrator {} have "
             "finished successfully. {}",
        '1': "WORKING: The request with ID {} for the concentrator {} is "
             "still in progress. {}",
        '2': "ERROR: The request with ID {} for the concentrator {} has "
             "been cancelled due to a timeout on the DC-Meter connection. "
             "{}",
        '3': "ERROR: The request with ID {} for the concentrator {} has "
             "been rejected for being outdated. {}",
        '4': "ERROR: The request with ID {} for the concentrator {} has "
             "been partially applied (success in some meters, failure in "
             "others). {}",
        '5': "ERROR: The request with ID {} for the concentrator {} is "
             "not properly formed."
             " Unable to process it. {}",
        '6': "ERROR: The request with ID {} for the concentrator {} has "
             "been cancelled due to a timeout on the DC-STG connection. "
             "{}",
        '7': "ERROR: The request with ID {} for the concentrator {} has "
             "asked information from a meter which does not exist in the"
             "DC database. {}",
        '8': "ERROR: The request with ID {} for the concentrator {} has an "
             "incompatibility with the protocol version. {}"
    }

meter_status = {
        '0': "SUCCESS: The meter {} have finished serving the request "
             "with ID {} successfully.",
        '1': "ERROR: The meter {} couldn't finish serving the request "
             "with ID {}.",
        '2': "WARNING: The meter {} have finished serving the request with "
             "ID {}. But any report after it is missing",
        '3': "ERROR: The meter {} couldn't finish serving the request with "
             "ID {}. Order partially applied (part of the data sent in the "
             "order were not correctly applied in the meter)."
    }


def get_report_path():
    try:
        return config_from_environment('PEEK')['report_path']
    except Exception as e:
        logger.info(
            'Error reading report save path. setting default {}'.format(
                DEFAULT_SAVE_PATH
            )
        )
        return DEFAULT_SAVE_PATH


class WSSTG(object):

    def __init__(self, filepath=DEFAULT_SAVE_PATH):
        self.save_filepath = filepath

    def manage_report(self, id_pet, id_dc, req_status, file_format, payload):
        status_txt = dc_status.get(str(req_status), '').format(id_pet, id_dc, '')
        txt = "{}:{}:{}:{} A Report has been received with status {}:\n {}".format(
            id_pet, id_dc, req_status, file_format, status_txt,
            payload
        )
        m = re.search('IdRpt="([^"]+)"', payload)
        report = m and m.group(1) or 'S00'

        filename = '{}_{}_{}_{}_{}'.format(
            id_dc, id_pet, report, file_format, datetime.now().strftime('%Y%m%d%H%M%S')
        )
        filepath = path.join(self.save_filepath, filename)
        logger.info('Saving {} to {}'.format(report, filepath))
        with open(path.join(self.save_filepath, filename),'w') as fp:
            fp.write(payload)
        logger.info(txt)

    def manage_request_status(self, id_pet, id_dc, req_status, reference=''):
        status_txt = dc_status.get(str(req_status), '').format(id_pet, id_dc, reference)
        txt = "{}:{}:{}:{} Request status received {}".format(
            id_pet, id_dc, req_status, reference, status_txt
        )
        logger.info(txt)

    def manage_meter_status(self, id_pet, id_dc, id_meters, meter_status, err_cat, err_code):
        status_txt = dc_status.get(str(meter_status), '').format(id_pet, id_dc, meter_status)
        txt = "{}:{}:{}:{}:{}:{} Meter status received {}".format(
            id_pet, id_dc, id_meters, meter_status, err_cat, err_code, status_txt
        )
        logger.info(txt)


class WSSTGService(ServiceBase):

    @rpc(Mandatory(UnsignedInt), String, Mandatory(Int), Mandatory(Int), String, _returns=Mandatory(Boolean))
    def Report(ctx, IdPet, IdDC, ReqStatus, Format, Payload):
        wsstg = WSSTG(filepath=get_report_path())
        wsstg.manage_report(IdPet, IdDC, ReqStatus, Format, Payload)
        return True

    @rpc(Mandatory(UnsignedInt), String, Mandatory(Int), String, _returns=Mandatory(Boolean))
    def UpdateRequestStatus(ctx, IdPet, IdDC, ReqStatus, Reference):
        wsstg = WSSTG()
        wsstg.manage_request_status(IdPet, IdDC, ReqStatus, Reference)
        return True

    @rpc(Mandatory(UnsignedInt), String(nillable=False), String(nillable=False), Mandatory(Int(min_occurs=1)), Int(nillable=True, min_occurs=1), Int(min_occurs=1, nillable=True), _returns=Mandatory(Boolean))
    def UpdateMetersStatus(ctx, IdPet, IdDC, IdMeters, MeterStatus, ErrCat, ErrCode):
        wsstg = WSSTG()
        wsstg.manage_meter_status(IdPet, IdDC, IdMeters, MeterStatus, ErrCat, ErrCode)
        return True


def create_app(**config):
    app = Flask(__name__)
    app.config.update(config)


    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('ws_stg')

    txt = "WS_STG version 0.1. GISCE-TI S.L"
    logger.info(txt)

    report_save_path = get_report_path()
    logger.info(' * Report save path: {}'.format(report_save_path))

    application = Application([WSSTGService],
        tns='http://www.asais.fr/ns/Saturne/STG/ws',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11()
    )

    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/ws': WsgiApplication(application)
    })

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
